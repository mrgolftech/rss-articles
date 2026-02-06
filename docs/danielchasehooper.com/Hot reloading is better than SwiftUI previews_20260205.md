# Hot reloading is better than SwiftUI previews

**来源:** https://danielchasehooper.com
**链接:** https://danielchasehooper.com/posts/hot-reloading-swiftui/
**日期:** Mon, 13 Oct 2025 00:00:00 +0000

---

[Daniel Hooper](https://danielchasehooper.com/)

[Home](https://danielchasehooper.com/) ・ [Articles](https://danielchasehooper.com/posts) ・ [Projects](https://danielchasehooper.com/#projects) ・ [About](https://danielchasehooper.com/about) ・ [X.com ](https://x.com/danielchooper)[Bluesky ](https://bsky.app/profile/danielchooper.bsky.social)[Mastodon](https://mastodon.gamedev.place/@danielchooper) [RSS](https://danielchasehooper.com/feed.xml)

# Hot reloading is better than SwiftUI previews

October 13, 2025・14 minute read

There is a better way than Xcode Previews to quickly iterate on your app. It's called "Hot Reloading". Here you can see it in action: the macOS app on the left is changing dynamically in response to my code changes on the right.

Your browser does not support the video tag. ![](todo.png)

That hot reloading experience is better than Xcode Previews because:

  * No need to create mock preview data, that's the _real_ app with _real_ data
  * Both the UI _and_ the business logic can be updated
  * The app doesn't reset to the root screen after each code edit. That means you can edit popups, panels, and deeply nested screens in the context they get shown in.
  * Xcode isn't required — that app on the right is Sublime Text



I'll show you how it's done by making a Todo app

## The Plan

The key to hot reloading is "dynamic libraries", which allow a running program to load and call new functions without restarting. The plan for using dynamic libraries to hot reload is roughly:

  1. Compile the app's UI and logic into a library
  2. Make a host app that uses the library's UI
  3. When the library changes, reload it in the host app
  4. Give the new library the old library's state



I like this approach because it doesn't require any dependencies and is only 120 lines. While it does require a certain project structure, that's simpler and more understandable than patching an unmodified program at runtime1. You can do this in [other languages](https://github.com/karl-zylinski/odin-raylib-hot-reload-game-template) and on other operating systems2. I'll walk you through it line by line. If you just want to read the finished code, you can get it at the end of this article.

## The Naïve Approach

Let's start with step 1 of the plan: build a dynamic library that contains our UI. The library we build here will get loaded by the app we create in step 2. We won't be using Xcode, so create `library.swift` in a new empty directory and with this code:

library.swift
    
    
    import SwiftUI
    
    public func createView() -> some View {
      return Text("Hello World!")
    }
    

And we can compile that with a `build_library.sh` shell script:

build_library.sh
    
    
    #!/usr/bin/env bash
    set -euo pipefail
    swiftc -emit-library -o UIPreview.dylib library.swift
    

Make it executable with `chmod +x build_library.sh`, and give it a run with `./build_library.sh`. That creates our dynamic library `UIPreview.dylib`.

The library can be loaded with `dlopen()`, which asks dyld (macOS's dynamic linker) to load the library's code into our process's address space. Then to call functions in the library, we look up the function's address by name with `dlsym()`.

In Swift that looks like this:

loader.swift
    
    
    import SwiftUI
    guard 
      let lib = dlopen("UIPreview.dylib", 0),
      let symbol = dlsym(lib, "createView") 
    else {
      fatalError(String(cString: dlerror()))
    }
    let createView = unsafeBitCast(symbol, to: (() -> View).self)
    

Let's run it
    
    
    $ swift loader.swift 
    Fatal error: dlsym(0x721c7f70, createView): symbol not found
    

Uh oh.

There is no symbol named "createView" thanks to Swift's [name mangling](https://en.wikipedia.org/wiki/Name_mangling), which renames every function to ensure [overloaded functions](https://en.wikipedia.org/wiki/Function_overloading) have unique names3. This is a problem for us because we need the name of the function as it appears in the library in order call it. Let's see what the mangled name is using `nm`:
    
    
    $ nm -g --defined-only UIPreview.dylib
    0000000000000cc0 T _$s9UIPreview10createViewQryF
    0000000000000dd8 S _$s9UIPreview10createViewQryFQOMQ
    

We can use `swift demangle` to see what that alphabet soup means (the leading underscore is not part of symbol names):
    
    
    $ swift demangle '$s9UIPreview10createViewQryF'
    $s9UIPreview10createViewQryF ---> UIPreview.createView() -> some
    
    $ swift demangle '$s9UIPreview10createViewQryFQOMQ'
    $s9UIPreview10createViewQryFQOMQ ---> opaque type descriptor for 
        opaque return type of UIPreview.createView() -> some
    

Looks like `$s9UIPreview10createViewQryF` is our function. We can update `loader.swift` with that name and try again

loader.swift
    
    
    import SwiftUI
    guard 
      let lib = dlopen("UIPreview.dylib", 0),
      let symbol = dlsym(lib, "$s9UIPreview10createViewQryF") 
    else {
      fatalError(String(cString: dlerror()))
    }
    let createView = unsafeBitCast(symbol, to: (() -> View).self)
    

Running that reveals the second problem:
    
    
    $ swift loader.swift 
    Fatal error: Can't unsafeBitCast between types of different sizes
    

What's happening is `dlsym()` returns an 8 byte pointer to the function, but Swift functions require 16 bytes4 of information to call (an 8 byte function pointer plus 8 bytes of context about captured variables). Rather than reverse engineer the 16 byte Swift function type, I went another route…

## Bridging Through C

We can avoid both the name mangling and Swift function type by exporting `createView` as a C function. This is done using Swift's `@_cdecl()` attribute. We'll keep the exported name the same as the Swift function name.

library.swift
    
    
    @_cdecl("createView")
    public func createView() -> some View {
    

Now we have to change the return type because C functions aren't able to return Swift types, and `some View` is a Swift type. The workaround is to place the SwiftUI View inside a `NSHostingView`5 and return that:

library.swift
    
    
    @_cdecl("createView")
    public func createView() -> NSView {
      return NSHostingView(rootView: Text("Hello World!"))
    }
    

That works because `NSHostingView` is an Objective‑C type, and those _can_ be returned from a C function.

Now for the interesting stuff: making the App.

## The App

Now for Step 2 of the plan: making an app to host our library from step 1. Make `app.swift` and start with the basics: showing a window and terminating when it closes.

app.swift
    
    
    import SwiftUI
    import AppKit
    
    @main
    struct Main: App {
      var body: some Scene {
        Window("Hot Reloading", id:"") {
          DylibView()
          .onAppear {
            NSApplication.shared.setActivationPolicy(.regular)
            NSApplication.shared.activate(ignoringOtherApps: true)
          }
          .onDisappear {
            NSApplication.shared.terminate(nil)
          }
        }
      }
    }
    

The `onAppear` code brings the window to foreground on launch. macOS does that automatically for app bundles, but for simplicity we'll compile to a plain executable.

Now we implement `DylibView`:

app.swift
    
    
    struct DylibView: NSViewRepresentable {
      func makeCoordinator() -> DylibViewCoordinator {
        return DylibViewCoordinator()
      }
    
      func makeNSView(context: Context) -> NSView {
        return context.coordinator.container
      }
    
      func updateNSView(_ nsView: NSView, context: Context) {}
    }
    

That uses the `NSViewRepresentable` protocol to bridge the gap between the NSView from our library and the SwiftUI window of the host app. `NSViewRepresentable` "undoes" what `NSHostingView` did in `library.swift`, completing the SwiftUI → NSView → SwiftUI round trip.

We don't do anything in `updateNSView` because our updates will happen outside of SwiftUI's typical update cycle.

That was mostly boilerplate code, the interesting stuff is in `DylibViewCoordinator`:

app.swift
    
    
    class DylibViewCoordinator {
      let dylibName = "UIPreview.dylib"
      var library:UnsafeMutableRawPointer?
      var container = NSView()
    
      init() {
        update()
      }
    
      func update() {
        guard let newLibrary = openLibrary() else {
          print(String(cString: dlerror()))
          return
        }
    
        guard let viewSym = dlsym(newLibrary, "createView")
        else {
          print(String(cString: dlerror()))
          dlclose(newLibrary)
          return
        }
    
        typealias CreateViewFn =
          (@convention(c) () -> NSView)
        let createView  = unsafeBitCast(viewSym, 
                                        to: CreateViewFn.self)
        
        let dylibView = createView()
        dylibView.autoresizingMask = [NSView.AutoresizingMask.width, NSView.AutoresizingMask.height]
        dylibView.frame = container.bounds
        container.addSubview(dylibView)
      }
    

As we've seen before, that opens the library, finds the `createView` symbol, and casts it to a C function type with `@convention(c)`.

The `dylibView` is placed inside `container`, which is what we handed to SwiftUI in `DylibView.makeNSView()`. When we implement reloading later on, the container view makes it possible to switch out `dylibView` right under SwiftUI's nose.

Here's the code for `openLibrary`:

app.swift, in DylibViewCoordinator
    
    
    func openLibrary() -> UnsafeMutableRawPointer? {
      return dlopen(dylibName, RTLD_LOCAL | RTLD_FIRST);
    }
    

For now it's just a wrapper around `dlopen`. It'll grow when we add hot reloading.

And finally we get rid of the view and close the library in `deinit`. We have to close the library after getting rid of the view because the view may be using the library's code.

app.swift, in DylibViewCoordinator
    
    
      deinit {
        container.subviews.first?.removeFromSuperview()
        if library != nil { dlclose(library) }
      }
    } // end of DylibViewCoordinator 
    

let's make `run.sh` to compile and run the app:

run.sh
    
    
    #!/usr/bin/env bash
    set -euo pipefail
    ./build_library.sh
    swiftc -o UIPreview -parse-as-library src/app.swift
    ./UIPreview
    

After `chmod +x run.sh` and running it, you should see this:

![The host app showing the text 'hello world'](/posts/hot-reloading-swiftui/hello.png)

Woo! It's not very interesting, but we'll build it out. Let's get reloading working first.

## Reloading

So far all we've done is make a normal app but with a lot more steps. It will all be worth it once hot reloading works.

The first change is to call `update()` on a timer:

app.swift
    
    
    class DylibViewCoordinator {
      let dylibName = "UIPreview.dylib"
      var library:UnsafeMutableRawPointer?
      var container = NSView()
      var timer: Timer?
    
      init() {
        update()
        timer = .scheduledTimer(withTimeInterval: 1.0,
                                repeats: true)
        { [weak self] _ in
          self?.update()
        };
      }
    

Now that update gets called multiple times, we need to remove the old view before adding the new one. We also need to close the old library:

app.swift, in update()
    
    
      guard let viewSym = dlsym(newLibrary, "createView")
      else {
        print(String(cString: dlerror()))
        dlclose(newLibrary)
        return
      }
      
      container.subviews.first?.removeFromSuperview()
    
      if library != nil { dlclose(library) }
      library = newLibrary
    
      typealias CreateViewFn =
        (@convention(c) () -> NSView)
      let createView  = unsafeBitCast(viewSym, 
                                      to: CreateViewFn.self)
    

The timer gets cleaned up in `deinit`:

app.swift, in DylibViewCoordinator
    
    
    deinit {
      timer?.invalidate()
      container.subviews.first?.removeFromSuperview()
      if library != nil { dlclose(library) }
    }
    

If you ran the app now, it still wouldn't update when the library changes. That's because of this `dlopen` feature:

> A second call to dlopen() with the same path will return the same handle, but the internal reference count for the handle will be incremented.
> 
> — dlopen man page

So even if the `UIPreview.dylib` file changed, `dlopen` will see it's the same path as last time, and it won't load the new version. I worked around this by copying the library to a new file before every update.

We need two more properties in `DylibViewCoordinator` to support that:

app.swift
    
    
    class DylibViewCoordinator {
      let dylibName = "UIPreview.dylib"
      var library:UnsafeMutableRawPointer?
      var container = NSView()
      var timer: Timer?
      var fileNameToggle = false
      let fm = FileManager.default
    

And we update `openLibrary` to do the copying:

app.swift, in DylibViewCoordinator
    
    
    func openLibrary() -> UnsafeMutableRawPointer? {
      let tmpDylibName = "\(fileNameToggle).dylib"
      try? fm.removeItem(atPath: tmpDylibName)
      do {
        try fm.copyItem(atPath: dylibName,
                        toPath: tmpDylibName)
      } catch {
        print("Error: couldn't copy dylib':  \(error)")
        return nil
      }
      fileNameToggle.toggle()
    
      return dlopen(tmpDylibName, RTLD_LOCAL | RTLD_FIRST);
    }
    

It alternates between the arbitrary names "true.dylib" and "false.dylib", which is enough to cause `dlopen` to consider the path "new" and open it.

Let's test:

  1. Run `./run.sh`
  2. Change the `Text("Hello World")` string in `library.swift` and **save the file**
  3. In another terminal window, run `./build_library.sh`



You should see the changes take effect in the app within one second of rebuilding the library!

## Conservative Updates

It feels a little wasteful to reload the UI every second even if nothing changed. The "right" way to do this would be to use the [FSEvents API](https://developer.apple.com/documentation/coreservices/file_system_events) to monitor the library's file path, but that takes more code than I'm willing to cover in this article. As a compromise, we can check the file modification time and only update if it changes.

We remember the file's last modification time:

app.swift, in DylibViewCoordinator
    
    
    var timer: Timer?
    var lastModified: Date?
    
    init() {
    

And only proceed through `update()` if the file modification time changed:

app.swift, in DylibViewCoordinator.update()
    
    
      func update() {
        guard
          let attrs = try? fm.attributesOfItem(atPath: dylibName),
          let modified = attrs[.modificationDate] as? Date,
          lastModified != modified
        else { return }
        lastModified = modified;
    
        guard let newLibrary = openLibrary() else {
    

If you restart the app with `./run.sh`, it should only reload the library when it changes.

## A Full Todo App

Since hot reloading "hello world" is boring, let's write a todo app while using hot reloading. Start the app with `./run.sh` and leave it running while you write the following code.

This is the state we'll need in `library.swift`:

library.swift
    
    
    struct Todo: Identifiable, Equatable {
      let id = UUID()
      var title: String
    }
    
    class AppState: ObservableObject {
      @Published var newItem = ""
      @Published var todos: [Todo] = [
        Todo(title: "Read 'Computer Systems: A Programmer's Perspective'"),
        Todo(title: "Learn C"),
        Todo(title: "Study algorithms and data structures"),
      ]
    }
    

If there were a real app, the todo items would be loaded from disk or the network, but we'll just hardcode three items for this example. Hot reloading is especially nice because data is loaded once at startup, and not every time you make a change.

That state is used by the view:

library.swift
    
    
    struct TodoListView: View {
      @ObservedObject var state: AppState
    
      var body: some View {
        // todo
      }
    }
    

And we have to update `createView` to return the `TodoListView`:

library.swift
    
    
    @_cdecl("createView")
    public func createView() -> NSView {
      return NSHostingView(rootView: TodoListView(state: AppState()))
    }
    

Now there is enough code in place that we can hot reload as we build out the `body` of `TodoListView`. You may want to set up your editor to make reloading easier — I configured mine so the cmd + b shortcut both saves the current file and runs `./build_library.sh`

library.swift, in TodoListView
    
    
    var body: some View {
      List {
        ForEach(state.todos) { todo in
          Text(todo.title).padding()
        }
        .onDelete { indexSet in
          state.todos.remove(atOffsets: indexSet)
        }
        .onMove { from, to in
          state.todos.move(fromOffsets: from, toOffset: to)
        }
    
        HStack {
          TextField("New todo", text: $state.newItem)
          Button("Add") {
            if !state.newItem.isEmpty {
              state.todos.append(Todo(title: state.newItem))
              state.newItem = ""
            }
          }
        }
        .padding()
      }
    }
    

I like typing that in bit by bit and running `./build_library.sh` so I can experience the magic of hot reloading.

You should end up with this: ![The host app showing the text 'hello world'](/posts/hot-reloading-swiftui/todo.png)

# Preserving State

Try adding a todo item in the running app and triggering a hot reload. The item will disappear! Every time the library is reloaded, `createView` creates whole a new app state.

We can fix that by remembering the state between reloads. I did this by adding two functions to our library: `createState`, which initializes the state and returns it to the host app for safe keeping, and `createStatefulView`, which initialize the UI using the saved state.

library.swift
    
    
    @_cdecl("createState")
    public func createState() -> UnsafeMutableRawPointer? {
        return Unmanaged.passRetained(AppState()).toOpaque()
    }
    
    @_cdecl("createStatefulView")
    public func createStatefulView(state_ptr: UnsafeMutableRawPointer) -> NSView {
      let state = Unmanaged<AppState>.fromOpaque(state_ptr).takeUnretainedValue()
      return NSHostingView(rootView: TodoListView(state: state))
    }
    

And then we need to change `DylibViewCoordinator.update()` to use these new functions. Here's the `update()` function with changes highlighted:

app.swift, in DylibViewCoordinator.update()
    
    
    func update() {
    
      guard let newLibrary = openLibrary() else { return }
    
      guard 
        let createViewSym = dlsym(newLibrary, "createStatefulView"),
        let createStateSym = dlsym(newLibrary, "createState")
      else {
        print(String(cString: dlerror()))
        dlclose(newLibrary)
        return
      }
    
      container.subviews.first?.removeFromSuperview()
    
      if let old = library {
        dlclose(old)
      }
    
      if state == nil {
        typealias CreateStateFn = 
        @convention(c) () -> UnsafeMutableRawPointer?
        let createState = unsafeBitCast(createStateSym, to: CreateStateFn)
        state = createState()
      }
    
      library = newLibrary
    
      typealias CreateViewFn = 
        @convention(c) (UnsafeMutableRawPointer) -> NSView
      let createView  = unsafeBitCast(createViewSym, to: CreateViewFn)
      let dylibView = createView(state!)
      dylibView.autoresizingMask = [NSView.AutoresizingMask.width, NSView.AutoresizingMask.height]
      dylibView.frame = container.bounds
      container.addSubview(dylibView)
    }
    

`update()` now creates a new state if we don't have one already. On every reload the state is passed to the new `createView` function.

You can now run the app, make changes to the todo list, trigger a hot reload, and have the app update — all without clearing the todo list changes.

## State Format Consistency

If you change the in-memory representation of `AppState`, such as by adding or removing a property, the app will probably crash. It happens because the new library code expects to work with the new `AppState`, but the app gives it an instance of an old `AppState`.

There's 2 ways you could deal with this:

  1. Accept that if you change the memory layout you'll have to restart the app
  2. Add a `version` property to the state that you increment whenever you edit the state. The library can check it and create a new state if it's handed an old version. That will reset the app, but it's better than crashing or having to manually restart it.



## Hot Reloading Xcode Projects

It is possible to use these techniques in an Xcode project. I didn't cover that because I wanted to focus on the underlying techniques. The gist is:

  1. Create a new App target that builds `app.swift` from this page.
  2. Create a new Library target consisting of your UI and logic files
  3. Add the `createState` and `createStatefulView` functions from this page's `library.swift` to your library target. Update them to use your app's state and root View.
  4. Look in the Xcode products folder to get the path to the compiled library, and set `dylibName` in `app.swift` to that path.
  5. In Xcode, run the scheme for the app target from step #1.
  6. Switch to the library scheme and build whenever you want to hot reload.



## Sample code 

Get the code by joining my mailing list and confirming your email. Unsubscribe from future articles at any time.

Join Mailing List

## See also

I'm making a build visualizer to help speed up slow builds. [Read more](/posts/syscall-build-snooping)

I wrote about [Why Swift's Type Checker Is So Slow](/posts/why-swift-is-slow/)

Use hot reloading for graphics programming in "[Learn Shader Programming with Rick and Morty](http://localhost:1313/posts/code-animated-rick/)"

* * *

  1. [HotSwiftUI](https://github.com/johnno1962/HotSwiftUI) uses a combination of [dyld interposition](https://www.emergetools.com/blog/posts/DyldInterposing), [method swizzling](https://www.nutrient.io/blog/swizzling-in-swift/), and memory scanning/patching to do hot reloading in a generic way. It may not require splitting your project into a library and host, but the setup process is involved. It requires installing a 3rd party app, adding a dependency, modifying all SwiftUI code, and modifying build settings. ↩︎

  2. For information about hot reloading on windows, see handmade hero days [21 through 23](https://guide.handmadehero.org/code/). ↩︎

  3. Name mangling isn't unique to Swift. C++ is one example of another language that does it. ↩︎

  4. You can see that Swift function pointers are 16 bytes with this bit of Swift: `typealias FnPtr = () -> Void; print("size \( MemoryLayout<FnPtr>.size)")` ↩︎

  5. Returning a `NSHostingView` also sidesteps the issue of having the `some View` type at the interface between two compilation units. `some View` is just a convenience feature that is like saying "There is a specific type here that conforms to the View protocol, but I don't feel like writing the full type out, figure it out at compile time and use it in all the places that refer to this function.". The host app couldn't use a function pointer that returns `some View` because it doesn't have access at compile time to the dynamic library's implementation in order to figure out the concrete type. ↩︎




❖

Get notified about my next article:

Join Newsletter

[More articles by Daniel](https://danielchasehooper.com/)
