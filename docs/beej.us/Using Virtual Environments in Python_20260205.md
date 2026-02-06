# Using Virtual Environments in Python

**来源:** https://beej.us
**链接:** http://beej.us/blog/data/python-venv/
**日期:** Sat, 11 Oct 2025 00:00:00 +0000

---

# [Beej's Bit Bucket  â¡ Tech and Programming Fun ](../..)

2025-10-11, 2025-10-12

# Using Virtual Environments in Python

![Virtualized Python Logo](images/virtpython.jpg) You wouldn't believe how long it took me to make this image in the [GIMP](https://www.gimp.org/).

Hi! This is an anti-slop blog that just presents some simple information without ads and a tremendous backstory about how my grandfather used Python back in the day or whatever. (He used [FORTRAN](https://en.wikipedia.org/wiki/Fortran) and [punch cards](https://en.wikipedia.org/wiki/Punched_card), for the record, but already I digress.)

And here I'm using the Zsh shell, but a generally-compatible one like Bourne or Bash will work. Check out the [official instructions](https://docs.python.org/3/library/venv.html) for other shells or tons more detail on this topic.

Let's go!

## What is a Virtual Environment?

It's a place you can install Python programs and libraries that are isolated from the rest of the system. So you can `pip install` things and not mess anything up elsewhere. A common use case is that you want to run someone's Python program and install its related packages but don't want to pollute your system with all these unmanaged tools and dependencies.

On [Arch Linux](https://archlinux.org/) (BTW) and others, this is the recommended way to install Python packages when they're not part of the official package manager.

There are four steps:

  1. Create the virtual environment (one-off step per environment).
  2. Activate it before use.
  3. Do things in it.
  4. Deactivate it when done.



You only have to create each environment once. After that it's a matter of activating it when you need it and deactivating it when you're done.

And you can have as many virtual environments as you want scattered around in various directories.

## Creating the Virtual Environment

The virtual environment will live in a directory. You specify the directory when creating it. Here I create one in a directory called `fooenv` out of my current directory:
    
    
    python -m venv fooenv
    

Or you can use a full path or whatever.

## Activating It

Switch into the directory and then source the shell script `bin/activate`.
    
    
    cd fooenv
    . bin/activate      # or "source bin/activate" if you prefer
    

The shell prompt will change to have a prefix with the name of the virtual environment in it; this is an in-your-face reminder that you're "inside" the virtual environment.

> ![Information Sidebar](../../common/images/goat50.png) All the `activate` script effectively does (besides change your prompt and a couple other things) is set your `PATH` so that when you run `python` or `pip` it uses the one in the environment's `bin/` directory instead of your system version. Run `which python` and see!

## Do Things In It

Now you can run `pip install` and install things that are only in this virtual environment. And when you run `python` you can see them.

Have fun!

## Deactivate It

When you're done having fun, you can get back to the real world by running this:
    
    
    deactivate
    

It's a secret function that the `bin/activate` script created. This gets you back to the non-virtual environment where everything is real and wholesome again. Run `which python` and see!

(You can also just exit the shell. That effectively deactivates it.)

## Deleting It

If you're done with the virtual environment and want to get rid of it, just carefully delete the directory that holds it. It will be as if it _never existed [spooky ghost noises]_.

## Bonus: Running from a Shell Script

What if you have a shell script and you want to call something in that virtual environment? Well, you just have to do the same steps.

  1. Create the environment somewhere that's relatively permanent. Maybe in a `~/.local/venvs/` directory where you keep them all.
  2. In your script, run `bin/activate` in that directory.
  3. In your script, do fun things.
  4. In your script, just exit when done. Or run `deactivate` then exit, either way.



Here's an example script that prints out the path to `python` in the virtual environment:
    
    
    # foo.sh
    . /home/beej/fooenv/bin/activate  # Change to your path
    which python
    deactivate
    

When I run that I get:
    
    
    $ sh foo.sh
      /home/beej/fooenv/bin/python
    

[Perfection](https://tremors.fandom.com/wiki/Perfection,_Nevada)!

## Bonus II: Running Python Scripts Directly

HT to [IrgndSonShreck](https://mastodon.sdf.org/@irgndsondepp@gts.da-miez.de/115360361989917317) for this one:

If you specify the path to `python` in the virtual environment, _even if it's not activated_ , you'll run it inside the virtual environment.

So if I have a Python program and I need it to run in the environment, I can do this:
    
    
    /home/beej/fooenv/bin/python foo.py
    

No need to `activate`.

> ![Information Sidebar](../../common/images/goat50.png) I dug around a bit to see how Python _knows_ that you've run it from the virtual environment in this way, since `VENV/bin/python` is just a symlink to the system Python. Apparently there's not a standard way to do this. [Linux has you look at the `/proc/PID/exe` symlink](https://stackoverflow.com/questions/606041/how-do-i-get-the-path-of-a-process-in-unix-linux) to determine the path to the executable, and other systems have other methods.
> 
> In any case, Python figures out where it's being run from and then tries to figure out if it's a virtual environment somehow. I suspect, but have not verified, this involves it looking for the `pyvenv.cfg` file that was created when the environment was made.

There's also nothing stopping you from putting the full path to the venv Python in a shebang in your script:
    
    
    #!/home/beej/fooenv/bin/python
    import sys
    print(sys.prefix)
    

When run, this will always use the virtual environment. So for me, it outputs:
    
    
    /home/beej/fooenv
    

But that's all pretty fragile and ugly. Though there's not any consensus I can find, people either do that or wrap the thing up in a shell script, it seems.

And one more related thing. If you want to shebang Python code that will run in the real environment if you're in it and also run in the virtual environment if you're in that, use this (which you should be generally using anyway):
    
    
    #!/usr/bin/env python
    import sys
    print(sys.prefix)
    

Here's an example of me running that outside and inside the virtual environment:
    
    
    $ ./foo.py
      /usr
    $ . fooenv/bin/activate
    (fooenv) $ ./foo.py
      /home/beej/fooenv
    

So that Python code will just run in whatever environment you're in at the time.

## Bonus III: Using a Third-Party Tool

HT to [Stephen Illingworth](https://mastodon.sdf.org/@JetSetIlly@mastodon.gamedev.place/115360124199348595) for this one. He suggests a tool called [`uv`](https://github.com/astral-sh/uv) to streamline this entire process and make your life easier.

The [README](https://github.com/astral-sh/uv?tab=readme-ov-file#highlights) has a pretty impressive list of highlights.

I've not tried it, but it definitely looks worth checking out. And I'm sure there are many others.

## Comments

[View Comments](https://mastodon.sdf.org/@beejjorgensen/115359964086061768) [Reply](https://mastodon.sdf.org/@beejjorgensen/115359964086061768)

Click on "View Comments" to see the comments.

[**Blog**](http://beej.us/blog/)  â¡  [**beej@beej.us**](mailto:beej@beej.us)  â¡  [**Home page**](http://beej.us/)
