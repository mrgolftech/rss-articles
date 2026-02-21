# CloudPebble Returns! Plus New Pure JavaScript and Round 2 SDK

**来源:** [ericmigi.com](https://ericmigi.com)
**发布时间:** Fri, 20 Feb 2026 00:00:00 GMT
**链接:** https://repebble.com/blog/cloudpebble-returns-plus-pure-javascript-and-round-2-sdk

---

As mentioned in our
software roadmap
, we’ve been working on many improvements to Pebble’s already pretty awesome SDK and developer environment.
#
CloudPebble Returns!
Fresh from several years in hibernation,
CloudPebble
is back! Everyone’s favourite way to write Pebble apps and faces in the browser with no downloads/setup needed is now on
cloudpebble.repebble.com
. Go give it a try right now!
Some notes:
Most things work, but there will surely be some rough edges, please
report any issues
you spot
Or better yet, fix the bugs or add new features yourself. It’s all
open source
!
Syncing to Github, tab completion and JShint/linting is not working yet (PR welcome!)
Unfortunately the original CloudPebble database got wiped a long time ago, you’ll need to re-import your projects
Apps built using the new SDK still work on older Pebbles (aplite to diorite), but
flint
(Pebble 2 Duo) require PebbleOS v4.9.127 (available now to
sideload
, will be pushed to everyone in a few days)
Thank you to Katharine Berry for creating CloudPebble!
#
Round 2 support
You can now build apps/faces for Pebble Round 2 and test them in the emulator. The new platform is called
gabbro
(formed from cooling liquid magma). The Round 2 display is 260x260 pixels, up from 180x180 on Pebble Time Round. Old PTR apps/faces automatically scale and work great on PR2 without any changes, but they will look even better if devs update them for the new display 😉 Download the
latest SDK
and use
pebble install emulator --gabbro
or try it out in
CloudPebble
.
Dive down memory lane and watch this 2015 Pebble Developer Retreat presentation on how to develop for round Pebble watches. Jump to
this specific time
to learn about Round-specific APIs  or watch the full video:
#
Now you can code Pebble apps in pure JavaScript
Since the dawn of time, developers could code apps and watchfaces for Pebble using C. Many people learned C just to write Pebble apps. There’s even a
book
!
Other options were available starting with Hui’s
Pebble.js
, where JS runs inside the Pebble mobile app and controls a fixed UI framework on the watch. Not to be confused with
PebbleKit JS
, which is also JS code running on the phone that provides data over Bluetooth to apps running on the watch.
In 2016, we began to work on a JavaScript SDK called
Rocky.js
that enabled devs to write watchfaces in JavaScript that ran entirely on the microcontroller inside Pebble. It was never completed and was missing a lot of features, but showed a glimmer of a new world.
Fast-forward to 2025 - I was having lunch with my friend Peter in Palo Alto (the same friend who wrote a
Doom demo
for my first watch inPulse in 2011)  who recommended I chat with his similarly named friend. Turns out the other Peter created
Moddable
, a popular JavaScript SDK for microcontrollers used in many consumer and industrial products. We hit it off and Moddable began porting their
SDK
to PebbleOS. It was not an easy lift, I really appreciate the time, effort and care that Peter and his team put into this project.
Thank you so much, team Moddable!
Alloy - the new Pebble JavaScript SDK
We’re extremely pleased to announce
Alloy
, the new JavaScript SDK for Pebble powered by Moddable. Now you can write apps and watchfaces for Pebble entirely in JavaScript (or TypeScript!), with full support for standard, modern JavaScript (ES2025) - the same language used in web browsers and Node.js. These apps run natively on the watch, using Moddable’s
XS engine
which is now built into PebbleOS. Alloy’s JavaScript APIs are designed to be familiar to JavaScript developers - a blend of Web Standard APIs like fetch() and WebSocket(), standard ECMA-419 Embedded JavaScript APIs for sensors, storage, and, networking, and new APIs just for Pebble
It’s now in
Developer Preview
, here’s how you can try it out:
On
CloudPebble
, or
Download the latest Pebble sdk
uv tool install pebble-tool --python 3.13
(
full instructions
). Then run
pebble sdk install latest
,
pebble new-project --alloy my-app
,
pebble build
,
pebble install --emulator emery
and voila - your new JS Pebble app is up and running!
Documentation is still in progress, but please read our
Alloy tutorial
and check out the dozens of
example JS example apps
. Moddable also has
full documentation
available for their JavaScript engine and SDK.
A few notes:
Both Emery and Gabbro platforms (Time 2 and Round 2) are already supported
You can mix JS and C in the same app (more details and examples to come)
Suggestions are welcome - please let us know which other Pebble capabilities should be exposed through JavaScript APIs
This is a preview, please set your expectations accordingly. Feedback and bug reports are extremely appreciated! Moddable also has a
blog post
with more details.
How to provide feedback
Please download the latest SDK and take it for a spin.
If you have questions, feedback or suggestions on how we should improve the SDK, please create a post on the
forum
.
If you need help writing an Alloy app, please post your code and problem to the
forum
.
If you think you’ve found a bug or issue with the Alloy SDK or Pebble tool, please post a Github issue for the
pebble-tool
.
Need some inspiration? You can now filter the
Pebble Appstore
for open source apps at
apps.repebble.com
. Or check out the dozens of
JavaScript examples
.
#
Much more SDK news to come in Part 2
Here’s the full changelog for
Pebble SDK 4.9.127
. We’re working on lots more developer/SDK related projects. Expect more news soon!
Stay in the loop
Get updates on Pebble news and products.
Subscribe

---

*抓取时间: 2026-02-22 00:02:39*
