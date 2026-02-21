# February Pebble Production and Software Updates

**来源:** [ericmigi.com](https://ericmigi.com)
**发布时间:** Wed, 18 Feb 2026 00:00:00 GMT
**链接:** https://repebble.com/blog/february-pebble-production-and-software-updates

---

#
Mega update on Pebble Time 2, Pebble Round 2 and Index 01
Things are busy in Pebbleland! We’re getting close to shipping 3 new hardware products and all the associated software that comes along with them. Overall, things feel good. I’d say the amount of last minute shenanigans is at the normal amount. Getting new hardware into ‘production’ is a pretty wild and exciting process. Building hardware is an exercise in balancing competing priorities of cost, quality and speed. In the last mile push to get into production, things can change quickly for the best (woohoo! the waterproof test finally passes, we can move to the next stage), or less good (uh, the production line needs 3 more test fixtures to test Index 01 mic performance, and a major production test software update…that’ll be a lot more money). Unlike with software, you can’t easily fix hardware issues after you ship! Making these last minute decisions is sometimes pretty stressful but hey, that’s the world of making hardware.
#
Pebble Time 2 Production Update
We’re in the Production Verification Test (PVT) phase right now, the last stop before Mass Production (MP). During this phase we manufactured hundreds of PT2s in a series of test builds, uncovered a bunch of issues, and fixed a bunch of issues. Just before the factories shut down for the lunar New Year, we got the good news that all the tests passed on the last build!
We focused most of January on improving the waterproofing on the watch (flash back to
last summer
when we worked on this for Pebble 2 Duo!). I traveled to visit the factory (
travelogue here
) and worked through a lot of open issues. Above is a video of the speaker waterproof testing from the production line. Good news is that we fixed all the issues, tests are passing and it looks like we’ll be able to certify PT2 with a waterproof rating of 30m or 3ATM! This means you can get your watch wet, wear it while swimming (but not in hot tubs/saunas) and generally not worry about it. It’s not a dive watch, though. Also, don’t expose it to hot water (this could weaken the waterproof seals), or high pressure water. It’s not invincible.
Entering PT2 Mass Production on March 9
Snapshot of our mass production plan (output counts are cumulative)
The factory is closed now for Lunar New Year and will reopen around the end of Feb. As of today, mass production is scheduled to start on March 9. It will take the production line a little while to spin up towards our target output of 500 watches per day. Finished watches ship from the factory once a week to our distribution center (which takes ~1 week), then get packed for shipping (a few days to a week), then get delivered to you (~7-10 days). These dates and estimates are ALL subject to change - if we run into a problem, production shuts down until we fix it. Delays can and most likely will happen.
What everyone’s been waiting for…when will your PT2 arrive 🙂
Based on current schedule, the first mass production PT2s will arrive on wrists during the beginning of April. We should wrap up delivering all pre-ordered Pebble Time 2s two months later by the beginning of June. If your watch had an initial date of December, it should arrive in April and if your initial date was April, it should arrive in June. Unfortunately we can’t predict when your specific watch will arrive - please don’t email to ask, we’ll just send you a link to this blog post.
A few weeks before your watch is scheduled to ship, we’ll email link for you to confirm your address (
change if now if you’d like
), pick optional accessories (extra chargers and straps) and pay any tariffs/VAT/taxes owed. For US orders, the tariff amount is $10 per watch. For other countries, VAT/taxes will be calculated and charged during order confirmation. When the watch is delivered you won’t need to pay anything else or deal with customs forms.
#
Index 01 Production Update
Index 01 is also in the Production Verification Test (PVT) phase. We’ve manufactured several hundred so far. Waterproof testing went well (it’s rated 1m of submersion, ipx8). You’ll be able to wash your hands, wash dishes, shower, get it wet etc but you can’t swim with it on. PTV is proceeding well, but we’re not finished yet. We’re still aiming to start mass production during March, but we don’t have a firm start date yet.
In order news, we’re working an Index 01 ring sizer kit that will be available for $10 (hopefully including worldwide shipping, working on that now). This will let you measure your index finger and find your exact Pebble-specific ring size. We will ask everyone to measure their ring size, either by ordering an Index 01 sizer kit or 3D printing the kit, because our sizes are different than Oura or other rings.
We’re also considering offering size 14 and 15. It’s a big upfront expense (~$50,000) to offer these sizes due to additional tooling that will be needed, so we’re collecting interest -
sign up here
if you would like Index 01 in these sizes!
#
Pebble Round 2 Update
Things are rolling along. We finished the Design Verification 1 (DVT1) phase just before the Lunar New Year holiday started. Work is progressing well. One of the huge speed-ups to the program overall is that the electrical design is almost identical to Pebble Time 2. This means our (two person) firmware team can code new features or bug fixes for PT2 and they work immediately on PR2! After the lunar new year, we’ll focus on waterproof testing and last minute tweaks before the current estimated production start date in late May.
#
So much software!
Our software output has been tremendous - we’re fixing bugs left, right and center and adding lots of new features to PebbleOS (
changelog
) and the Pebble mobile app (
changelog
).
Here are some highlights:
Weather now works (in sunrise/sunset timeline pins and the Weather app)
WhatsApp calls show up as calls (on Android)
Fixed a major background crash bug in Pebble iOS that caused weather and other apps to not fetch live data.
Added Websocket support to Pebble iOS
Many old Pebble apps/faces use weather APIs that no longer work (Yahoo, OpenWeather). The Pebble mobile app now catches these network requests and returns data from Open-Meteo - keeping old watchfaces working!
Pebble Appstore is now ‘native’ inside the Pebble mobile app (in v1.0.11.1 on
beta channels
today). We’ve also updated the Pebble Appstore on the web at
apps.repebble.com
. If you’re a developer and don’t see the latest version of your app or watchface, please make sure to
import them
(takes ~2 minutes).
Now you can
filter out older apps
with non-working settings pages or companion apps. Or filter specifically for apps that are open source!
Some PebbleKit 1.0 Android apps should work again (thanks Google for giving us back
com.getpebble.android.provider.basalt
). But devs - please upgrade your apps to PebbleKit 2.0 Android for new companion apps (
more info
and
repo
)
Watch settings can now be adjusted in the Pebble mobile app. Your settings are saved and synced to all your Pebble watches.
Thanks to many community contributions, there are now many new app icons for notifications for apps that didn’t exist 10 years ago!
Most PebbleOS work has been going into factory verification sw for Obelix
Left handed mode - wear your Pebble on right hand with buttons flipped (thanks Claudio!)
Health data is now synced from watch to phone (thanks
Michael
!)
We’ve also made some great advances on the SDK and developer front…expect an update very soon 😉
Stay in the loop
Get updates on Pebble news and products.
Subscribe

---

*抓取时间: 2026-02-21 00:09:53*
