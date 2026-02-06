# ‘Backseat Software’

**来源:** https://daringfireball.net
**链接:** https://blog.mikeswanson.com/backseat-software/
**日期:** 2026-01-29T21:50:32Z

---

[Mike Swanson's Blog](https://blog.mikeswanson.com)

  * [Posts](/)
  * [Projects](https://blog.mikeswanson.com/projects/)
  * [About](https://blog.mikeswanson.com/about/)
  * [Search](https://blog.mikeswanson.com/search/)



# Backseat Software

January 18, 2026

What if your car worked like so many apps? You’re driving somewhere important…maybe running a little bit late. A few minutes into the drive, your car pulls over to the side of the road and asks:

_“How are you enjoying your drive so far?”_

Annoyed by the interruption, and even more behind schedule, you dismiss the prompt and merge back into traffic.

A minute later it does it again.

_“Did you know I have a new feature? Tap here to learn more.”_

It blocks your speedometer with an overlay tutorial about the turn signal. It highlights the wiper controls and refuses to go away until you demonstrate mastery.

Ridiculous, of course.

And yet, this is how a lot of modern software behaves. Not because it’s broken, but because we’ve normalized an interruption model that would be unacceptable almost anywhere else.

I’ve started to think of this as **backseat software** : the slow shift from software as a tool you operate to software as a channel that operates on you. Once a product learns it can talk back, it’s remarkably hard to keep it quiet.

This post is about how we got here. Not overnight, but slowly. One reasonable step at a time.

## Software Came on Disks

There was a time when software shipped on physical media: floppy disks, CD-ROMs, sometimes even with a spiral-bound manual.

Software felt like a product back then. You bought it, installed it, and used it. If you upgraded, it was because you chose to. The software didn’t constantly change underneath you, and it didn’t have the opportunity to ask for your attention beyond whatever UI the developers shipped on day one.

That era had real downsides. If you shipped a serious bug, you lived with it until the next release, which could be weeks or months away. If security issues were discovered, your options ranged from “mail a patch” to “good luck.” In hindsight, it’s amazing we survived!

But something else was true too. When you were using the software, you were alone with it.

As a software developer, if something was wrong, you found out because users told you. Sometimes loudly. Sometimes angrily. Often on message forums or during support calls.

Feedback was slower and scarcer, but it was real. It was also “expensive” in the way that matters. You had to earn it, listen to it, and interpret it.

## Always Online

Then the internet arrived, and for a while it was almost entirely upside.

Software could finally be updated after it shipped. Bugs could be fixed. Security holes could be closed. Documentation got easier. Support got easier. The idea of “ship it and hope for the best” started to fade.

[Microsoft’s update infrastructure](https://en.wikipedia.org/wiki/Windows_Update) is a good example of the era. Updates moved from “go download this” toward automation over time, and by the early 2000s the industry was normalizing the idea that your machine could check for and apply updates regularly.

This was a genuine leap forward in quality and safety. If you’ve ever been on the receiving end of a serious bug report, you know how valuable it is to fix something _now_ rather than in the next boxed release.

So far, so good.

## The Back Channel

Once software could reliably connect to the internet, it no longer just received instructions. It could talk back to the company that made it.

At first, this too was mostly good. Crash reports made it easier to fix real problems, update checks were convenient, and license activation reduced some kinds of piracy. Teams could finally see patterns in failure modes instead of guessing.

Developers like me love this kind of feedback loop, and for good reason. A tool that improves over time is better than one that doesn’t.

But that back channel didn’t stay limited to “this crashed” and “there’s an update.” It expanded, quietly, because once you can send _some_ data home, the next question arrives right on schedule:

_“Since we’re already connected…what else can we learn?”_

## Everything Gets Measured

Once software could send data home, the next natural thought was:

_“Can we understand how people actually use this?”_

Again, that’s not an evil thought. In fact, it’s useful! Before analytics, if you wanted to understand user behavior, you had to ask people, watch them, or infer patterns from support tickets. That requires time, empathy, and effort.

Suddenly, you didn’t have to guess anymore.

Web analytics going mainstream is one of those quiet accelerants. [Google’s acquisition of Urchin in 2005](https://urchin.biz/urchin-software-corp-89a1f5292999), and the rise of Google Analytics shortly after, helped normalize the idea that instrumentation and dashboards were simply part of building software.

Instead of arguing in a meeting about which features mattered most, you could look at usage data. Instead of guessing where people struggled, you could see drop-offs. Instead of relying on the loudest customer, you could get a broader view.

**But somewhere along the way, the center of gravity shifted.**

Usage data stopped being a tool for improving software and became a tool for optimizing behavior. The question quietly changed from:

_“Is this good software?”_

to:

_“Does this increase engagement?”_

And that’s when the vocabulary starts to creep in. DAU. MAU. Retention. Funnels. Stickiness. Cohorts. Conversion. Gamification. Oh my!

If you’ve worked inside a modern product organization, you’ve heard these words so often they start to feel unavoidable.

## Metrics Can Be Correct and Still Be Wrong

One of the most dangerous things about analytics is that they feel objective. A chart is a chart. A number is a number. They have the aesthetic of truth.

I’ve always liked this quote by William Bruce Cameron ([often misattributed to Albert Einstein](https://quoteinvestigator.com/2010/05/26/everything-counts-einstein/))_:___

_“Not everything that can be counted counts, and not everything that counts can be counted.”_

Metrics don’t measure reality. They measure what your product currently makes easy.

There’s a well-known warning about this, often summarized as: _when a measure becomes a target, it stops being a good measure_. It’s commonly referred to as [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law), and the broader point shows up in multiple fields, because it keeps happening to humans in systems with incentives.

When I was at Microsoft, a team wanted to remove a feature because “the analytics show that nobody uses it.” If you looked at the UI, though, that feature had been moved deeper and deeper over time:

  * it used to be easy to find
  * then it moved into a menu
  * then into a submenu
  * then into a settings panel
  * then behind an “advanced” section
  * then it was basically invisible



Of course nobody used it!

The analytics didn’t prove the feature was unwanted. The analytics proved that we buried it.

Even worse, once a metric becomes a target, people get promoted for moving it. That doesn’t require anyone to be malicious. It just requires incentives and a dashboard.

## Experimenting in Production

Measuring behavior changes what feels possible:

_“What if we try two versions to see which one performs better?”_

This is where A/B testing enters the story.

On paper, it’s an engineering triumph! Instead of arguing about opinions, you can test ideas. Instead of debating copy or layout in a meeting, you can ship both and let real-world behavior decide.

But A/B testing quietly changes the role of the product team. You’re no longer just building a tool and observing how it’s used. You’re now running experiments on people…adjusting wording, placement, timing, friction, and flow to see what moves the metric.

At that point, the product stops being a finished artifact and starts behaving like a laboratory. Every screen becomes provisional, and every interaction becomes a hypothesis. Once that mindset takes hold, it’s very hard not to optimize for what moves fastest, even if it moves the wrong thing.

There’s a quieter consequence here that doesn’t get talked about much. When experimentation becomes the primary decision-making tool, a strong product vision becomes optional.

Not because anyone argues against _vision_ , but because you don’t strictly need it anymore, and because backing a chart is safer than backing an opinion. Metrics have numbers and experiments have winners. If a decision goes wrong, you can always point to the data and say, “we followed the evidence.”

Over time, this can change the role of a product team where judgment slowly gives way to iteration, and taste gives way to performance. The product still evolves, but it does so without a clear sense of direction…only a sense of momentum.

## Guidance Everywhere

Once experimentation becomes the default way decisions get made, changing behavior stops being theoretical and starts being procedural.

At that point, nudges aren’t a new idea. They’re the obvious next move. It usually starts reasonably:

_“We shipped a feature. Users might not notice it.”_

Fair.

So you add a little callout. Then a tooltip. Then an onboarding tour. Then a “What’s New” screen. Then a little survey. Then another survey, because you didn’t get enough responses the first time. By the time you’re done dismissing everything, the tool has already taken more time than the task itself.

If you’ve ever read about [“choice architecture” and nudging](https://yalebooks.yale.edu/book/9780300262285/nudge/), this will feel familiar. The modern language for it was popularized in the late 2000s, and the core idea is simple: how choices are presented changes what people do, even if nothing is technically forced.

Then product teams go one step further. Instead of just shaping choices, you can shape _timing_. Prompts start showing up in the middle of workflows because that’s when the user is “most engaged.”

The industry also has a whole discipline around persuasive design and how to move someone from intention to action with prompts, friction removal, and well-timed triggers. [B.J. Fogg’s behavior model](https://www.demenzemedicinagenerale.net/images/mens-sana/Captology_Fogg_Behavior_Model.pdf) is one of the more cited frameworks in this space.

Some nudges are genuinely helpful. But the same machinery that helps you discover a feature can also be used to push you into something you didn’t come here to do. And once the machinery exists, it gets reused.

It’s also why coming back to an app after you’ve been away for as little as a week can feel like a game of Whac-A-Mole. Not because you forgot how to use the tool, but because the tool has been busy while you were gone. There's new tips, new tours, new “what’s new” overlays, new announcements, new prompts that all want a click before you’re allowed to do the thing you actually opened it for.

## Push Notifications

Then the smartphone era arrived and made interruption cheaper. Once you can send push notifications, you no longer have to wait for the user to open the tool. You can tap them on the shoulder whenever you want.

[Apple’s push notification service](https://en.wikipedia.org/wiki/Apple_Push_Notification_service) arrived with iOS 3.0 in 2009, and it’s hard to overstate what a shift this was for the “who initiates the interaction?” question.

Some of this is legitimate and genuinely helpful:

  * messages you asked for
  * alerts you configured
  * reminders you chose



But we all know where it went:

  * “We miss you.”
  * “You haven’t finished setup.”
  * “You haven’t tried this feature.”
  * “Come back and see what’s new.”



All framed as helpful. All measured in engagement. And just like that, the tool starts acting less like a tool and more like a stalker.

## In Defense

To be fair, not every prompt is evil, and not every notification is marketing.

Some software is genuinely complicated, and a little guidance prevents real mistakes. Some categories are basically _made of_ alerts: messaging, security, banking, calendars, delivery tracking, anything where timing actually matters.

Telemetry exists because some problems can’t be found any other way. It’s often the only method that enables teams to find the weird crashes that happen on one driver version, one device model, or one edge case you’ll never reproduce in-house.

Even the “feature tour” has a defensible origin story. Users ask for improvements, teams ship them, and then users complain they didn’t know the improvements existed. In other words, the same people who hate popups also punish you when you make changes silently. If you’ve ever shipped a big UI redesign, you already know this.

So the problem isn’t that software _ever_ teaches, asks, or informs. The problem is that once a company builds the machinery to do it, that machinery becomes cheap to reuse, and the incentives gradually pull it away from “help the user succeed” toward “move the metric.”

What starts as an occasional heads-up becomes a permanent layer of UI exhaust. What starts as support becomes a funnel. What starts as a reminder becomes a habit-forming system.

That’s the drift I’m talking about. Not guidance existing at all, but guidance becoming the default posture of the tool…always talking, always nudging, always taking the first turn in the conversation.

And once the tool decides it should initiate the interaction, the rest of the story is mostly mechanics.

## Even the Builders Hate It

One of the most bizarre contradictions in modern software is that the people building these engagement systems don’t like them either!

Ask anyone who works on onboarding popups, feature tours, lifecycle messaging, or in-app announcements how they feel when an app interrupts them mid-flow to announce something they didn’t ask for. The answer is almost always the same.

They hate it! Or at least they’re annoyed.

Find me the telemarketer who likes being called during their own dinner. The job exists because it works _enough_ in aggregate, not because anyone enjoys being on either end of it.

So why does it keep happening? Because inside companies, the incentives are clear and the measurements are easy. You can measure clicks and track whether they led to a “completion.” You can measure whether a nudge led to the next step in the funnel.

You cannot easily measure the resentment. Or the rage clicks when they smash a button to dismiss another “did you know” pop-up. You cannot easily chart the moment a user thinks, “I used to like this product, and now it feels needy.” You cannot easily quantify the slow erosion of trust.

There’s an older framing for this that I like: _in an information-rich world, attention becomes the scarce resource_. [Herbert Simon wrote about this dynamic in 1971](https://gwern.net/doc/design/1971-simon.pdf), long before push notifications, app stores, or social media feeds.

If your business runs on attention, and attention is scarce, then the pressure to “capture” it becomes constant.

## Tools Are Supposed to Get Out of the Way

As the marketing adage goes:

_People don’t want a drill. They want a hole in the wall._

The drill is just the tool. The outcome is the job. Nobody wakes up and says, “I’d like to buy a new drill today!” Well, except drill enthusiasts, I suppose. Likewise, nobody wakes up and says, “I’d like to buy a new app today!” In fact, your app is in the way of their objective.

I could argue that nobody wants the hole either.

What they really want is what comes _after_ the hole. They want to hang photos of family and friends, souvenirs from trips, and artwork that makes a room feel like home. The drill and the hole are both just steps along the way.

That distance matters. The further a tool is from the real human outcome, the more invisible it should be. The drill doesn’t ask how you’re enjoying your experience drilling. It doesn’t upsell you on premium hole-making. It exists to disappear the moment it’s done its job.

This is a useful way to think about software. Most users don’t want “software.” They want the outcome:

  * write the document
  * edit the photo
  * pay the invoice
  * file the taxes
  * ship the code
  * communicate with the team



Great tools get out of the way so the user can accomplish their goal.

Your favorite products feel like they’re not there. You open them, do the thing you came to do, and close them again without ever feeling managed, marketed to, or delayed.

Your least favorite products tend to do the opposite. You use them because you have to, not because you want to.

## Everything Gets “Smart”

This pattern is spreading because “smart” is spreading. Smart TVs. Smart speakers. Smart thermostats. Smart appliances. Anything that joins your Wi-Fi can:

  * update itself (often good)
  * send diagnostics (often good)
  * collect usage data (sometimes defensible)
  * interrupt you (almost always annoying)
  * market to you (almost never what you bought it for)



It’s the same story as software, just with plastic and a power cord.

One more backchannel: some “smart” TVs use [Automatic Content Recognition](https://en.wikipedia.org/wiki/Automatic_content_recognition) (ACR) to identify what’s on the screen and turn that into data. It’s basically a pixel-sampled fingerprint of anything that shows up on your screen whether streamed, broadcast, or just played back locally.

If you want a more academic version of how “data collection leads to prediction which leads to intervention” becomes a business model, this is adjacent to what [Shoshana Zuboff describes as surveillance capitalism](https://news.harvard.edu/gazette/story/2019/03/harvard-professor-says-surveillance-capitalism-is-undermining-democracy/). It's not just observing behavior, but intervening to shape it.

## How We Got Here

None of these events ruined software by themselves. They just made the next step easier.

  * 1990s: consumer internet connectivity becomes mainstream, and “online” stops being a special mode.
  * 1996–1997: PointCast popularizes [“push” to the desktop](https://www.wired.com/1997/03/ff-push/) (including ads): software starts initiating the interaction.
  * 1997: [pop-up ads](https://www.forbes.com/sites/jaymcgregor/2014/08/15/the-man-who-invented-pop-up-ads-says-im-sorry/) arrive and interruption becomes a business model.
  * 1997: [Office 97 ships](https://news.microsoft.com/source/1996/11/19/microsoft-office-97-released-to-manufacturing/) with “Clippy” the Office Assistant, the friendly ancestor of in-app nudges.
  * 2000: “automatic updates” becomes a normal expectation for consumer operating systems.
  * 2005: [Urchin](https://googlepress.blogspot.com/2005/03/google-agrees-to-acquire-urchin_28.html) → Google Analytics: instrumentation and dashboards go mainstream.
  * July 10, 2008: [the App Store launches](https://www.apple.com/newsroom/2008/07/10iPhone-3G-on-Sale-Tomorrow/) and app distribution becomes frictionless.
  * June 17, 2009: [push notifications](https://en.wikipedia.org/wiki/Apple_Push_Notification_service) arrive at scale on iOS (even if they weren’t first): the app no longer has to wait for you to open it.
  * Nov 4, 2009: Apple announces [2 billion push notifications](https://www.apple.com/newsroom/2009/11/04Apple-Announces-Over-100-000-Apps-Now-Available-on-the-App-Store/) already delivered, early proof that “tap on the shoulder” scales.
  * 2010s: “[growth hacking](https://www.sciencedirect.com/science/article/pii/S0040162523007965)” becomes a discipline; nudges, tours, overlays, and lifecycle messaging become standard product surface area.
  * By 2011, Apple’s review rules explicitly forbade using push for “advertising, promotions, or direct marketing.”
  * Mar 4, 2020: Apple changes course and [allows marketing push](https://www.theverge.com/2020/3/4/21165087/ios-apple-push-notification-advertising-marketing-now-allowed-app-store), but only with explicit opt-in.
  * 2020s: “[enshittification](https://www.wired.com/story/tiktok-platforms-cory-doctorow/)” becomes a word people recognize because enough people feel the pattern.



People use “enshittification” to describe platform decay. What I’m describing here is one of the mechanisms that makes that decay feel personal. It's the constant conversion of your attention into a [KPI](https://www.kpi.org/kpi-basics/).

## Designing for Quiet

I don’t want to go back to floppy disks. I like fast updates. I like security patches. I like sync. I like crash reports when they help fix real issues.

What I want is for “phone home” to be treated like a privileged capability, not an assumed right. In other domains, we treat privileged capabilities with care. We put them behind intentional choices. We build guardrails. And we treat abuse as a bug, not a growth opportunity.

Here are a few practical ways out. And yes, we’ve heard many of these before.

### 1) Make interruptions opt-in, and make opt-out permanent

If you want to announce a feature, fine. Put it somewhere predictable.

If you want to educate, fine. Let me ask for help.

If you want to survey me, fine. Ask at a sensible moment and accept “no” as a real answer.

Most importantly, if I turn something off, it should stay off! A tool should not require me to keep saying “not now.” Or conveniently “forget” my choices in its next update.

### 2) Separate product health telemetry from growth telemetry

Crash reports, performance metrics, and error logs are about stability.

Engagement nudges are about behavior.

When those get mixed together, the growth incentives win, because they produce the cleanest charts and the easiest wins. If you can’t draw a clear line between “this helps us fix bugs” and “this helps us juice numbers,” the product will drift toward the numbers.

### 3) Use analytics as a flashlight, not a steering wheel

Analytics are useful for asking better questions. They are not answers by themselves. Before removing a feature because “nobody uses it,” ask:

  * Is it discoverable?
  * Did we move it?
  * Did we rename it?
  * Is it used rarely because it solves rare but important problems?
  * Is it used by a small set of power users who keep the whole system running?



Then talk to humans. Analytics can reduce guessing, but it can also create false certainty.

### 4) Optimize for trust, not just return visits

Short-term engagement can be increased by annoyance. [Long-term loyalty is harder and more valuable](https://www.tandfonline.com/doi/full/10.1080/23311975.2024.2361321).

The best products I use don’t constantly remind me to use them. They quietly do their job so well that I come back when I need them. That’s what tools are supposed to do.

### 5) Ship a real “quiet mode”

Not “quiet except for what we care about.”

_Quiet_.

No popups. No tours. No surveys. No “news.” No nudges.

If the product is genuinely valuable, quiet mode should improve retention, because it respects the user’s attention and intent.

Also, it’s a nice forcing function. If your product can’t stand on its own without constantly poking the user, that’s a signal. Maybe not the signal you want, but definitely a signal.

Software didn’t break all at once. It eroded slowly, one reasonable justification at a time.

Each step made sense in isolation, and each step could be defended. Together, they reshaped the priorities of an entire industry. Once software became measurable in this way, it became optimizable in this way. And optimization has a way of eating everything else.

Instead, let’s make software that respects your attention, does its job well, and lets you get on with your life. That’s what good software used to feel like and what it could feel like again. Good software is a tool that you operate, not a channel that operates on you.

As always, [I love hearing from you](https://blog.mikeswanson.com/contact/).

## Comments

### 38 responses to "Backseat Software"

  1. ![John Avatar](https://secure.gravatar.com/avatar/81131fa9f8c9ea2d6fbdd8c54bfdd1d72a75e4eb7c3f2a22d808ebc58c7e0272?s=40&d=mm&r=g)

John

[January 19, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1405)

Thank you for the historical perspective on how we got here. I am almost willing to pay extra money for truly quiet mode. 

There's a reason that Clippy is one of the most hated 'features' ever shipped by Microsoft. And I think you've nailed it.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1405#respond)

     1. ![Christian R. Conrad Avatar](https://secure.gravatar.com/avatar/c13c01c85100c8df4de04f6cb63809ac77fe923fda6fcd6d04f1a36126376dbc?s=40&d=mm&r=g)

Christian R. Conrad

[February 1, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1448)

The phrase "Clippy only wanted to help" and the Clippy icon as a profile picture has become something of a meme on YouTube recently. And, as I understand it (OK, mostly a WAG), for many of thses users that is not ironic, but sincere.

Which (again, AIUI) is quite understandable and reasonable: In Mike's timeline, Clippy is still — as annoying as it could be — mostly on the side of "sincerely trying to help", as opposed to the current metrics-über-alles "nudging" and Total Telemetry™.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1448#respond)

  2. ![John Avatar](https://secure.gravatar.com/avatar/e6c4232e4e6eef8718049a1c3300c4e12c7e8f1c0c9b33810be4d4eaad67c45d?s=40&d=mm&r=g)

John

[January 29, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1412)

“By 2011, Apple’s review rules explicitly forbade using push for ‘advertising, promotions, or direct marketing.”‘

…what happened to that? mainstream iOS apps spam us all the time now

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1412#respond)

  3. ![Barry Avatar](https://secure.gravatar.com/avatar/8f8d20ff11738e8475e11206c455c5357144ade9c8c0198012c49cd58ac445cb?s=40&d=mm&r=g)

Barry

[January 29, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1413)

Excellent. And true about more than software design. There are universal truths underneath all this behavior, instructive of how humans behave with each other generally. 

My role has been the mediator between marketing, creatives, software development, and the C Suite – across several industries. Yet each company consisted of this team of critical players. 

Over time, the people who rose to the C Suite came exclusively from a Marketing background. This meant that eventually, in product meetings, Marketing people dominated every discussion. The bosses and the marketers speak the same lingo. And did not understand or value the input of the other teams.

Unsurprisingly, each company as a whole came to over-valued click metrics over product development. They actively de-valued the harder to measure qualities of good UI and software design – the actual elements that customers pay money for, and judge quality with every interaction. The skills and expertise of those teams were seen as cost centers to be reduced whenever possible. While more and more got invested in Marketing programs.

Once this dynamic takes over, it's almost impossible to turn around. I watched three formerly successful companies wither into bankruptcy by strangling loyal customers with marketing plans, instead of delivering good products. As the numbers continued down, in every meeting the solution was always more Marketing (popups, emails, surveys, discount codes, etc.), because they could measure clicks, and they wanted more clicks.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1413#respond)

     1. ![Guy V. Avatar](https://secure.gravatar.com/avatar/c0f0e987229346849e9bbb4daedc6d061502f706acc21d5230ff24f97238e6b5?s=40&d=mm&r=g)

Guy V.

[January 31, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1444)

I fully agree that this is the root of the problem. What you are saying in your comment needs to be widely known.  
Unfortunately it now seems to have infected Apple as well.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1444#respond)

  4. ![J. Bee Avatar](https://secure.gravatar.com/avatar/bf744b59618ceba447af0fa915e06a68aa6b335996a0c77138b2daa5c4ad0b63?s=40&d=mm&r=g)

J. Bee

[January 29, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1414)

I think this article is somewhat refusing to put it's finger on the simpler version of what's "going wrong" here. It's advertising. 

All of these bad practices are a result of trying to *advertise* products and features to the end user, without their consent. Because of course, the nature of advertising is to operate explicitly *without* consent. 

All this stuff happens because of the monetary incentive, and the view that users are just undifferentiated purchase bots that will probably buy more stuff if you throw it in their faces. 

It's *not* actually morally OK to advertise to people without giving them the option to refuse. It's not OK for instance, for Apple to advertise it's products and services within the OS as they now do, and not allow people to opt out from those advertisements. 

This is exactly what made Microsoft of the 90's and early 2000's so absolutely vile. The fact that they extended themselves into services, and then sold their souls by advertising those services, (as well the 'cool features' of their own OS's), within the OS itself. The whole system became a nightmare of pop up suggestions and requests to buy into their services. Apple is definitely moving strongly in that direction. 

Switching to Apple *was* the breath of fresh air at the time, but now they're just doing the exact same thing that we all hated Microsoft for back then. 

because: money

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1414#respond)

     1. ![Miles Thatsme Avatar](https://secure.gravatar.com/avatar/906df724320ab21a2875690e13e264a1aadaf234d6094e432ed36e37ca4664a4?s=40&d=mm&r=g)

Miles Thatsme

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1422)

Agree with the insidiousness of advertising: I have trouble thinking of another industry where people pay to *not* receive your product (ads). Why not let people “vote with their feet/wallets”—well, what if your primary source of intel about their votes is the ad industry?

The subscription service model amplifies these problems, built upon entrenched platforms. 

But I think this was a clear-eyed, more focused piece—terrific.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1422#respond)

     2. ![walter Avatar](https://secure.gravatar.com/avatar/b72710d2793eea5e885577d45ab431fbbcf3ae092c030a8cd1fc748d11052d1a?s=40&d=mm&r=g)

walter

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1430)

100% in agreement. Apple has in fact become that ogre that the hammer was thrown at in that classic 1984 Super Bowl Ridley Scott commercial Ad. Apple has lost its soul.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1430#respond)

  5. ![Ian Davies Avatar](https://secure.gravatar.com/avatar/c5865e0dff8d2d1599f819bb43a7baea2e6b3707832044eab97c51b37b7b27ad?s=40&d=mm&r=g)

Ian Davies

[January 29, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1415)

Adobe is the cursed poster child for this now, IMO. Tours, surveys, the repulsive blue pop-ups, the utterly pointless crash windows that offer to look for a solution, but have yet to offer a single one in 23 years. The relentless disrespect for their users is one of the most miserable examples of enshittification.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1415#respond)

     1. ![Sam Schlesinger Avatar](https://secure.gravatar.com/avatar/71373b5c5d4d892484a917430f7e22f5cebb96bfe616075b06bea165823f2b58?s=40&d=mm&r=g)

Sam Schlesinger

[January 31, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1443)

Exactly. I pay for tools to do my job, not to be treated like a KPI. Every Adobe launch feels like running a gauntlet of promos, tours, upsells, counter-intuitive feature bars and useless crash dialogs before I can touch my actual work. It’s not software anymore, it’s internal metrics wearing a toolbar. Painfully ridiculous.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1443#respond)

  6. ![Dmitri Zdorov Avatar](https://secure.gravatar.com/avatar/a69eb07324343dfac4b4c373c7f34a29b9bc0c88747e9671f61bef6610708441?s=40&d=mm&r=g)

[Dmitri Zdorov](https://dimka.com)

[January 29, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1416)

It’s not just advertisement, it’s hustling culture in general. Hustlers just do better overall. They sell more, they earn more, they get more prizes, they’re more popular. And you can say that is chasing a quick buck, short-term profits, or maybe it’s just what you get when there is too much competition, which is not as bad as too little, but still not optimal.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1416#respond)

  7. ![Scott H Avatar](https://secure.gravatar.com/avatar/6333b7101081867835354f2e428a25ef0d9a2143925aa2c5e53b2cc570e9d3e7?s=40&d=mm&r=g)

Scott H

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1417)

The part that discourages me is that I think we've reached the point where half or more of the people working on products no longer remember how it was in the before times. They don't realize that pooping popups and sign-ups and surveys and tutorials all over your carefully-crafted UI is a choice - for them, this is just the way things are.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1417#respond)

  8. ![Caitlin Steele Avatar](https://secure.gravatar.com/avatar/b9baff1e42db4760ce7dae4220b0c75a63d95e3cd983fdfa3f76d9c0d8366065?s=40&d=mm&r=g)

[Caitlin Steele](https://www.caitlinsteele.com/)

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1418)

Wonderful article. I have struggled with a lot of this myself as a designer, developer, product owner and leader. A few months ago Vivianne Castillo said something about commerce not being capitalism and it stuck with me.

I wrote a few articles last year about how tech has gone from being like startups panning for gold to open pit mining for mass extraction. I think the core of this is that software used to be about creating value and exchanging that value for money (commerce). Give me money and I give you a box of software you own. We have pivoted to models of extraction of value, from employees and from customers. Yay capitalism. 

I miss building software that makes me proud to ship.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1418#respond)

  9. ![Neal Avatar](https://secure.gravatar.com/avatar/406894dbe567818d5df16d2ef36a141e59a5c951e572924d3eddd96035f28659?s=40&d=mm&r=g)

Neal

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1420)

Lovely perspective and insight. I'll add another snippet from another thread. Pre-iPhone we had Symbian. Pre the onslaught of apps, social networks, attention economy, etc.  
It had this terrible activity where when the battery got below (from memory) 20%, the screen would blast on with an alert for low power. And do it continuously every couple of percent or minutes - even though though the phone was still going to run for another few days more likely! A constant distraction.  
(Little did we know what would come 15 years later of course and how simple this was!). The iPhone arrived - Apple (or perhaps Steve Jobs) had obviously put attention into those details of how to get out of your way and there was no way they were going to annoying you with alerts such as this.  
Of course, what you described above occurred - they added the App Store, push notifications (all great ideas) - and then they themselves fell down this slope in the recent years with 'new feature' announcements, incessant pushing, along with everyone else. 

Honestly, the original few iterations of iOS were your point number 5……

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1420#respond)

  10. ![Foo Bar McGrath Avatar](https://secure.gravatar.com/avatar/1ce585b1f2e13082b6c983c26559a28061eb4ba0c3ae6d2efa75f84100138035?s=40&d=mm&r=g)

Foo Bar McGrath

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1423)

A great read - thanks for putting down so clearly what we have been experience for so long.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1423#respond)

  11. ![Philip Avatar](https://secure.gravatar.com/avatar/48dea2af86a2048e97fdc5054ccf98cd1244427535f1cf498dac7f0a932696cc?s=40&d=mm&r=g)

Philip

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1424)

You don't mention the disappearance of user manuals.

It used to be that if I,  
* Wanted to learn a new application, I work through the whole manual  
* Wanted to understand a feature, I'd look it up in the manual.  
* Couldn't work out how to do something, I'd go to the manual

I'd look in the manual. I'd love it if user manuals were brought back. Then if I want to I'll refer to it, if I don't I won't.

Now everything is supposed to be intuitive and we don't need any information on how to use an app. It's all common sense, until it isn't.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1424#respond)

  12. ![Denver Fletcher Avatar](https://secure.gravatar.com/avatar/66e844beae909ba23ac8d54e619014caa6984e3389377e923d639d97fc6fecaa?s=40&d=mm&r=g)

Denver Fletcher

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1425)

Very good. Thank you very much for writing it.  
And also, as attributed to Henry Ford, "if I had asked people what they wanted, they would have said 'faster horses' ".  
This illustrates the fatal allure of local optimization as the sole determinant of action. It forecloses innovation because what could be better than "data-driven decisions"?  
Regarding Trust and Consent I would really like to send you something I think you would appreciate. Email me if so.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1425#respond)

  13. ![Khürt Louis Francis Elliot Williams Avatar](https://secure.gravatar.com/avatar/2f88c80005db8d6bc27301a3023cc557e267ae64b6ccd8dd5773120511910312?s=40&d=mm&r=g)

[Khürt Louis Francis Elliot Williams](https://islandinthenet.com)

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1426)

I loved this because it names a feeling I’ve had for years. I launch an app to do a job, not to be coached, nudged, or surveyed. Notifications for trivial things make me irrationally angry. The best tools vanish. They finish, quietly, and let me get on with my actual life.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1426#respond)

  14. ![tim Avatar](https://secure.gravatar.com/avatar/f807b5609eae64257bf4877652ea49fee40ac2451c152c12fa596ffeda647157?s=40&d=mm&r=g)

tim

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1427)

“Here are a few practical ways out.”

For whom, though? You admit that users hate it, and engineers do, too, and companies are incentivized to do it anyway. Who exactly is this advice for?

This reads about like advice to “Don’t cause oil spills — nobody likes them”. Not untrue, but this fact alone doesn’t suggest a path forward for anyone caught in the system.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1427#respond)

     1. ![Bruce Avatar](https://secure.gravatar.com/avatar/b436f42030da2297ddeeca9ac4b4df6cbaeb9b8431e2fe21547b90a6776b3405?s=40&d=mm&r=g)

Bruce

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1435)

@tim It's an educated rant, sometimes you just need to get things off your chest, you never know who reads it, could make a difference

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1435#respond)

        1. ![tim Avatar](https://secure.gravatar.com/avatar/37102125b390509c367181cf5df2791502ea1cbfb484db8234d1392031c9a12b?s=40&d=mm&r=g)

tim

[February 2, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1456)

I appreciate righteous indignation as much as anyone, and I am on board with that.

I'm just not sure "practical" is the correct word here.

If companies wanted to optimize for happy users, we wouldn't be here in the first place. And if they suddenly decided they wanted to, it's trivial to remove the annoyances, like turning off A/B testing and (non-urgent) notifications.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1456#respond)

  15. ![g Avatar](https://secure.gravatar.com/avatar/24d3033ff5b0700b421d06af099ece6ec6b598ef02bbccdc9104d7e6babdbe91?s=40&d=mm&r=g)

g

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1428)

Also Sparkle on Mac furthered the implementation of notifications

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1428#respond)

     1. ![g Avatar](https://secure.gravatar.com/avatar/24d3033ff5b0700b421d06af099ece6ec6b598ef02bbccdc9104d7e6babdbe91?s=40&d=mm&r=g)

g

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1432)

I mean, the initial idea was great, allow updates, but later on it got abused

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1432#respond)

     2. ![Gordon Meyer Avatar](https://secure.gravatar.com/avatar/ca871b3caae791a6a4b969195738f187bc7e993d13e98d522153a21885557fb6?s=40&d=mm&r=g)

Gordon Meyer

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1438)

Sparkle is horrible because, due to its tech and design, it can only interrupt what you’re doing. I never launch an app to perform and update, I launch an app to accomplish some task, yet Sparkle rudely inserts itself at the worst possible moment.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1438#respond)

  16. ![Peter Kankowski Avatar](https://secure.gravatar.com/avatar/2242d51b48453b453d4f7485f966654e9fe1c71f9d620a7c10f3d19aa312cbd6?s=40&d=mm&r=g)

[Peter Kankowski](https://www.abareplace.com)

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1429)

Many tools are implemented as SaaS now, so the developers have more options to watch users' behavior and experiment with surveys, CSAT, and cross promotions. Desktop software is still relatively quiet and private by design; at least, I don't collect any telemetry in my own program.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1429#respond)

  17. ![Jim Avatar](https://secure.gravatar.com/avatar/37833876c75e94d91f1defe51d41b9bc872783414a220fa4b7193b8afdcb4db4?s=40&d=mm&r=g)

Jim

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1431)

"It blocks your speedometer with an overlay tutorial … Ridiculous, of course."

My 2017 Chevy has been doing this for nearly a decade already! It will block my speedometer while driving to let me know that a Bluetooth device briefly disconnected and then reconnected. It's got another popup that hides my speedometer every time it notices the outdoor temperature is near-or-below freezing, reminding me that ice may exist. No hysteresis either, so in spring and fall I'll sometimes get that popup several times during a single short drive when the temperature is hovering right around their alerting threshold. There's even a long wordy message that appears completely at random, including while driving, whose sole purpose is to remind me not to use the touchscreen while driving. It won't time out on its own, and dismissing it requires interacting with the touchscreen -- unlike all other popups, you can't close this one with the buttons on the steering wheel.

And of course, not a single one of these blatantly dangerous distractions can be disabled. I just have to live with them, which I can only assume is observed by the car's built-in telemetry and reported back to GM as a signal of "acceptance".

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1431#respond)

  18. ![Conan Avatar](https://secure.gravatar.com/avatar/09c5273f76594116d9c0496632a6e82ff564efa3497270042b625848d1e6a136?s=40&d=mm&r=g)

Conan

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1433)

I find it hard to think of a more evil job than advertising. Especially in the modern form using massive data and servers to slide in the advert of the bid winner.

But it's all a consequence of our economic system and greed based system.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1433#respond)

  19. ![MacHobbes Avatar](https://secure.gravatar.com/avatar/35eb7baf1e0ff1e812f4bdae55f9ecdbf2a059dc439a03d34e5ddd6f4627ef71?s=40&d=mm&r=g)

MacHobbes

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1434)

So great software is like great typography. You enjoy it without noticing it.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1434#respond)

  20. ![Mark Avatar](https://secure.gravatar.com/avatar/e64431d3a896f2e2ef0c9e6977f51791eeb3bb296540b4174478f8455f99e20a?s=40&d=mm&r=g)

Mark

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1436)

Interesting history, but this seems incorrect: 

'2000: “automatic updates” becomes a normal expectation for consumer operating systems.'

In Windows XP automatic updates were not enabled by default until service pack 2 was released in 2004. Prior to that the average user was not even aware they needed updates

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1436#respond)

  21. ![Houss Avatar](https://secure.gravatar.com/avatar/74c24f1e2bffb4d821c8413cc4cf25742ed743ebe901b4e2248a800f05d17d99?s=40&d=mm&r=g)

Houss

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1437)

Great article

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1437#respond)

  22. ![Erik J. Barzeski Avatar](https://secure.gravatar.com/avatar/4ed9b19e58b018cca65b9330b413c1b3d4917d4b05262d32a80d5a04b6062396?s=40&d=mm&r=g)

[Erik J. Barzeski](https://analyzrgolf.com/)

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1439)

Thank you for writing this. The best software is the one that lets you discover — at your own pace — its features.

I can look things up (on YouTube, Reddit, etc.) if I need to find out how to do something, but even then the truly great software will guide you through doing something without needing to truly hold your hand. It'll name menus with obvious and good titles. It'll put the tools in the right place. It'll have a good Help menu (oh how I miss those!). It won't try to do too much.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1439#respond)

  23. ![Don Barth Avatar](https://secure.gravatar.com/avatar/a82ef607f04b65cbe4e5febc42c496532a5959a55f962ed008f801da672d96d0?s=40&d=mm&r=g)

Don Barth

[January 30, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1440)

Thank you for this excellent article

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1440#respond)

  24. ![Leon Zandman Avatar](https://secure.gravatar.com/avatar/c14d4d08fc76a68afef803bcca8dd4ac427c3ce6cc666b15d82e596f42064b4d?s=40&d=mm&r=g)

Leon Zandman

[January 31, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1442)

Fun fact regarding push notification spam: On early Windows Phones (7/8), there actually was a technical reason to send push notifications regularly.  
The push channel (MPNS) could expire after inactivity, often without clear errors.  
If you didn’t send anything for a while, pushes would just stop working until the app was reopened.  
So many apps sent “keep-alive” notifications—not for engagement, but to keep push delivery functional. Functional spam 😉

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1442#respond)

  25. ![Christian R. Conrad Avatar](https://secure.gravatar.com/avatar/c13c01c85100c8df4de04f6cb63809ac77fe923fda6fcd6d04f1a36126376dbc?s=40&d=mm&r=g)

Christian R. Conrad

[February 1, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1447)

"Software didn’t break all at once. It eroded slowly, one reasonable justification at a time."

Heh… "Reasonable", as in "well-intentioned"? As the saying goes, "the road to Hell…"

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1447#respond)

  26. ![Marius Avatar](https://secure.gravatar.com/avatar/7263c5ed3527f4d0da3f93562c265f9f9d31351454b4c3baf03828090a84dcde?s=40&d=mm&r=g)

Marius

[February 1, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1450)

Thank you, I’m always so annoyed when e.g. I have not used a ride hailing app for quite some time, but now need a car quickly and any app I try gives me several interruptions before I can get started using it.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1450#respond)

  27. ![Madhu Vudali Avatar](https://secure.gravatar.com/avatar/64fec7d5022e4f882540998a7ba5c629ea32e27463a4e304657d3ef8919e5d8c?s=40&d=mm&r=g)

Madhu Vudali

[February 1, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1453)

Love this. Thanks, Mike! 

Sadly, too many PMs (& teams) are measured on how they are driving growth using these tactics. And, I confess I was part of some of these product efforts.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1453#respond)

  28. ![Peter S Avatar](https://secure.gravatar.com/avatar/e604089d913370a5d27cf0313256fd37e7c1cb44063fc9baee4ac3198cd16732?s=40&d=mm&r=g)

Peter S

[February 2, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1458)

Thank you for this much needed reflection on what's wrong with a lot of modern software. I'll just add another observation:

Great user experiences don't waste your time on things you don't need or want. I think of it as "criminal time wasting or theft". You can make it easy for users to discover new features, search for answers, or ask for help. Don't insist on interrupting and taking their time without asking for permission first. That's just rude.

It's not enough to examine analytics. Take the time to understand what users are trying to do and how you can reduce the friction they experience.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1458#respond)

  29. ![Peter Harvey Avatar](https://secure.gravatar.com/avatar/8ce48e4d8dfb638b65547ccfe79750d8b5b39b917f396e6dc064b9b981a517f7?s=40&d=mm&r=g)

Peter Harvey

[February 3, 2026](https://blog.mikeswanson.com/backseat-software/#comment-1459)

This article reminded me of "obliquity" - achieving goals indirectly as per John Kay. Success - however you'd like to define it be that money, reputation or even joy - found through people making something they're passionate about rather than chasing the numbers.

Shout out to Tim Harford's "Cautionary Tales" podcast which recently covered this in the story of Zappos and Tony Hsieh.

[Reply](https://blog.mikeswanson.com/backseat-software/?replytocom=1459#respond)




### Leave a Reply [Cancel reply](/backseat-software/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

Δ

Click to Copy
