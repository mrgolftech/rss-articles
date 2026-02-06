# Everyone knows your location, Part 2: try it yourself and share the results

**来源:** https://timsh.org
**链接:** https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/
**日期:** Thu, 17 Apr 2025 10:05:43 GMT

---

[ tim.sh ](https://timsh.org)

  * [blog](https://timsh.org/)
  * [about](https://timsh.org/about/)
  * [Bluesky](https://bsky.app/profile/timsh.org)



sign in subscribe

# Everyone knows your location, Part 2: try it yourself and share the results

[ ![tim](/content/images/size/w160/2025/01/wg21-2.jpg) ](/author/tim/)

#### [tim](/author/tim/)

17 Apr 2025 — 11 min read

![Everyone knows your location, Part 2: try it yourself and share the results](/content/images/size/w1200/2025/04/Screenshot-2025-04-16-at-20.21.31.png)

It's been more than 2 months now since my first post on the topic of location data sharing between various 3rd parties came out – in case you haven't seen it, you should definitely start from there: 

[Everyone knows your locationHow I tracked myself down using leaked location data in the in-app ads, and what I found along the way.![](https://timsh.org/content/images/icon/wg-4.jpg)tim.shtim![](https://timsh.org/content/images/thumbnail/dataflow_upd-1.png)](https://timsh.org/tracking-myself-down-through-in-app-ads/)

Since then I had a chat with a lot of people working in this field – both members of non-profit organisations, fighting for data privacy rights in various countries, and employees of adtech companies, proving my words right or wrong (but mostly right). I was even invited to "[Lock and Code](https://www.malwarebytes.com/blog/podcast/2025/03/how-ads-weirdly-know-your-screen-brightness-headphone-jack-use-and-location-with-tim-shott-lock-and-code-s06e05?ref=timsh.org)" podcast to talk about geolocation data and privacy. Ok, enough with the bragging. 

I went through the process described in my initial post and decided to make it faster and more scalable: manually going through hundreds of requests in Charles was very cool for research and educational purposes, but it also took me a lot of time to find "interesting" requests coming from a single app. 

I've significantly upgraded my approach (though it could definitely be more efficient), and in this post I wanted to share it with you.

### TL;DR

I have created a small guide and a Python notebook that allow anyone to record mobile app traffic and find surprising things in it. 

Here's [the link to a GitHub repo](https://github.com/tim-sha256/analyse-ad-traffic/?ref=timsh.org) with it. 

The initial setup takes 10-30 minutes.   
Analysis using this algorithm took me about 10 minutes per app - you can definitely dig deeper and get lost for hours if you find something interesting in there..   
Follow the [`readme`](https://github.com/tim-sha256/analyse-ad-traffic/blob/main/README.md?ref=timsh.org) or the guide below if you'd like to try!

**I came up with an idea** : it would take me hundreds of hours to go through each app and record the traffic, though I would love to do that – let's not blindly trust some table from the internet, but find out for ourselves.   
I copied the Gravy Analytics Google Sheet and created a simple form that you can fill in (no personal info is collected) that writes to that Google Sheet  
[Link to the table](https://docs.google.com/spreadsheets/d/1fJbNT-kmfuWUlIpYr9sduvjZS1ggrmhydCzoDlqaMaA/edit?usp=sharing&ref=timsh.org)  
  
Look up any app you already have on your phone or just a random one in the table, check if others have commented on it already and record the traffic.  
  
Finally, if you want to help crowdsource the information on the kinds of data the apps from the list collect and share – [fill in the form](https://forms.gle/Wyj1K54B5NQw3Vxt7?ref=timsh.org): 

[I found something interesting in the app trafficHey! I don’t know how much people will go through with all the instructions and analysis, but since you’re here, you probably already did it and found something. Thanks for being here and doing this. Fill in the form below and your response will be recorded to a shared spreadsheet. PLEASE CHECK ALL OF YOUR INPUTS FOR YOUR PERSONAL INFORMATION. This form is set in a way that I collect nothing personal from you (like email or Google account or whatever), but your response will be viewable by virtually anyone - so be aware!![](https://timsh.org/content/images/icon/android_192.png)Google Docs![](https://timsh.org/content/images/thumbnail/jRCp4Akn5TH6KUw5HNa4mv0XrSReregDtVFTKJDD2eOqZtk6c3J69uGb5z85mbBlNu4ACbHFWRkUTBA-w1200-h630-p)](https://forms.gle/Wyj1K54B5NQw3Vxt7?ref=timsh.org)

Please edit all the private information in your submission (in case it's there). 

* * *

## Visualising "domain power"

Before jumping into the guide, I wanted to share a few cool-looking visualisations with you.   
Long story short: lately I've been obsessed with graph visualisations of things, especially branchy-embedded ones. 

While analysing the traffic I found myself curious: how are the adtech companies domains distributed across all of the requests?   
So I joined these two together and created a visualisation using `PyVis` that would answer that question:

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-16-at-20.26.37.png)

Here's some context: 

  1. Every circle is a domain or a subdomain.   
The hierarchy is represented by the inclusion of circles into others.   
Example: `o-sdk.ads.unity3d.com` is represented by 3 circles: `o-sdk` inside of `ads` inside of `unity3d`. 
  2. Colors represent the app (I analysed 5) that the request corresponds to.   
I used low opacities for better visibility, and it turns out that in my mix of colors and their opacities purple is the combination of all of them. 
  3. Circle sizes, or masses, represent the frequency: how often did this or that domain appear in the requests data.   
See any insights?



> **Unity** rules the mobile game app traffic scene.   
> For comparison, the `g / doubleclick` thing is Google Ad Network. 

Take a look at it in motion: 

I included the code for it – [`visualise_domains.ipynb`](https://github.com/tim-sha256/analyse-ad-traffic/blob/main/visualise_domains.ipynb?ref=timsh.org) in the same repo so that you could create the same visualisation out of the data you record.   
I also included the [`ad_domains.html`](https://github.com/tim-sha256/analyse-ad-traffic/blob/main/sample_ad_domains.html?ref=timsh.org) file with this sample (mine) graph – simply open it in your browser if you want to play around with it.

I also was curious of the density of the requests – in my last post, I mentioned that hundreds of requests happen in just a few seconds, and now I could finally take a look at them:

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-17-at-15.32.48.png)

Filenames in the legend are flows collected from 5 different games.   
I cut it at 60s for better visibility, but obviously there were requests after that as well. 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-17-at-15.50.19.png)

This one is again a different view of the domain power – look at the list on the right.

  * It should be obvious by now that Unity is the leader in this strange contest – it has the most subdomains called and the most requests made to. 
  * Applovin is a Palo Alto-based company that acquired above mentioned Adjust in 2021, has shown [$1.58 bln net income in 2024](https://investors.applovin.com/news/news-details/2025/AppLovin-Announces-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx?ref=timsh.org), and decided to get rid of it's mobile games development products and focus on its advertising business just a few months ago.
  * Doubleclick.net is Google Ads
  * And surprisingly, Facebook, that I've seen in the requests from every single game, is in the last place among these. Well, at least based on this strange metric observed on 5 examples 



Now that you've seen these obscure but good-looking graphs - let's move on to the actual guide that you could follow to analyse any app traffic. 

* * *

## Getting started

### Step 1: Install mitmproxy on your PC

`mitmproxy` is an open-source tool for intercepting traffic with wide capabilities and a surprisingly nice web version called `mitmweb`.  
Be aware that `mitmproxy` is recognised as malware by some anti-virus apps - looks scary, but it's not. 

Go to their [official downloads page](https://mitmproxy.org/downloads/?ref=timsh.org) and choose whatever installation way you like more.   
On Mac, for example, you can simply run `brew install mitmproxy` . 

After installation run this command to start `mitmweb` (mitmproxy + web interface): `mitmweb --listen-host 0.0.0.0 --listen-port 8080`  
  
You can also use `mitmproxy` CLI, but I prefer mitmweb because it is actually very helpful for initial discovery (and understanding the scale of the RTB requests).

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-13-at-21.31.52.png)

We use `--listen-host 0.0.0.0` to avoid `mitmproxy` starting in the default location, which is localhost `128.0.0.1` – this way, you don't record your PC traffic and will see 0 requests until you complete the next step. 

### Step 2: prepare your mobile device

What you'll need to do is to then setup proxy on your iPhone / Android device and install + trust a certificate.   
I focused on iOS in my instruction, but setting up an Android phone for the same experiment is even easier and is well-documented - for example, [here](https://medium.com/@williamxyz/monitoring-network-on-android-with-mitmproxy-bfb8722191ee?ref=timsh.org).

I believe you might need to turn on the developer mode, otherwise you won't have Certificate Trust in your settings. Or maybe not.   
Anyway, if it's missing from your settings - [here's a guide](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device?ref=timsh.org) on how to do it.   
By the way, your iPhone and computer must be in the same wifi network for all of this to work.

### Step 3: start collecting requests! 

  1. Run `ipconfig getifaddr en0` to find your PC local IP address.
  2. Next, open the wifi network settings on iPhone, scroll down and setup manual proxy with:  
`server` = the ip address you just found  
`port` = 8080



On iPhone, open browser and go to `mitm.it`  
further instructions are described here:  
[https://jasdev.me/intercepting-ios-traffic](https://jasdev.me/intercepting-ios-traffic?ref=timsh.org)  
or here: [https://support.apple.com/en-us/102390](https://support.apple.com/en-us/102390?ref=timsh.org)

> ** _What is this for?_**  
>  You need to install the certificate and enable full trust to be able to decrypt TLS-encrypted traffic.   
> Otherwise you'll just see a bunch of encrypted packets flowing in and out. 

Congrats! If you completed all the steps correctly, you should now see requests in the `mitmweb` interface.  
If you only want to record traffic coming from a specific app, close all apps, "Clear flows" and then open the desired app.

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-13-at-21.34.21.png)

If you don't have an app installed yet, you might have to turn off proxy on iPhone, download the app and then turn it on again and clear the flows - AppStore refused to work with proxy on for me. 

If you don't have anything specific on your mind – pick any app with "Checked = False" in the "original list" sheet. [https://docs.google.com/spreadsheets/d/1fJbNT-kmfuWUlIpYr9sduvjZS1ggrmhydCzoDlqaMaA/](https://docs.google.com/spreadsheets/d/1fJbNT-kmfuWUlIpYr9sduvjZS1ggrmhydCzoDlqaMaA/?ref=timsh.org)

* * *

## Let's find something interesting

All right, now we can record the data! 

You can already find interesting requests manually - for example, I'm pretty sure you'll see this Facebook request no matter what app you analyse: 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-07-at-11.49.09.png)

But looking through the requests in `mitmweb`, even with ok (not advanced) filtering is a very slow process. And you'll see – there will be hundreds (if not thousands) of requests in just a few minutes. 

When you feel like there's enough (you could even leave it open or play for an hour or so to collect more data), close the app and switch off the phone, then in `mitmweb` press File → Save.

This will give you a `flows` file - rename it as `appname.flow`.

### Filtering & analysing the data

Open the [`mitm_test.ipynb` ](https://github.com/tim-sha256/analyse-ad-traffic/blob/main/mitm_test.ipynb?ref=timsh.org)\- either in a local Jupyter Notebook or in Google Colab (or wherever you work with `.ipynb`s).  
Personally, I feel much more comfortable working with this kind of data in the local environment.   
However, if you don't code at all / don't use python, e.t.c. – believe me, there's nothing faster and easier than opening up [Colab](https://colab.research.google.com/?ref=timsh.org) and importing the file. 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-14-at-17.11.12.png)

There are quite clear and broad instructions in the file, so I won't repeat the full process, but just highlight a few things: 

A very important step - fill in as many keywords as you have on your mind.   
I was strictly focused on IP and geo data, but you might want to look for other things, like "screen_brightness", "IDFA" or whatever.   
Please note that these will only return the exact matches (imagine an amount of words / strings where "lat" or "lon" would be substrings). 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-14-at-17.18.04.png)

Now that you've put all the keywords in the list, run the cells below and it will create a `df_filtered` table with the requests (or responses) that match the keywords.

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-15-at-13.27.01.png)

Here you'll see a snippet of the match (`matched_in_request` and `matched_in_response`), as well as the "reason" for both cases - the keyword(s) that are in the match. 

Below is a simple `.loc` where you can input the index of the row (the first column on the left) and see the full value of a given column – in the example below, `"full_reponse"`.  
If the string was too long, I just copied it to Sublime Text and use their built-in search to find more context or other surprising data points in the request or response text. 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-15-at-13.29.55.png)

And that's it! 

Finally, if you want to help crowdsource the information on the kinds of data the apps from the list collect and share – [fill in the form](https://forms.gle/Wyj1K54B5NQw3Vxt7?ref=timsh.org): 

[I found something interesting in the app trafficHey! I don’t know how much people will go through with all the instructions and analysis, but since you’re here, you probably already did it and found something. Thanks for being here and doing this. Fill in the form below and your response will be recorded to a shared spreadsheet. PLEASE CHECK ALL OF YOUR INPUTS FOR YOUR PERSONAL INFORMATION. This form is set in a way that I collect nothing personal from you (like email or Google account or whatever), but your response will be viewable by virtually anyone - so be aware!![](https://timsh.org/content/images/icon/android_192.png)Google Docs![](https://timsh.org/content/images/thumbnail/jRCp4Akn5TH6KUw5HNa4mv0XrSReregDtVFTKJDD2eOqZtk6c3J69uGb5z85mbBlNu4ACbHFWRkUTBA-w1200-h630-p)](https://forms.gle/Wyj1K54B5NQw3Vxt7?ref=timsh.org)

Please edit all the private information in your submission (in case it's there). 

### Room for improvement?

I know this is a very primitive way of doing things – I could've done this all with `mitmdump` and automated saving / filtering straight to .csv, but I deliberately kept it semi-manual.   
The format and structure of all these requests and responses is very diverse and the further you go from looking at them manually, the higher chance you'd miss something.   
At first I tried filtering out by content type and encoding, but I've noticed that some of the matching requests are missing from the list. 

So I turned off the filters... and found this: 

![](https://timsh.org/content/images/2025/04/Screenshot-2025-04-15-at-13.49.10.png)

`gs-loc.apple.com` is an endpoint used by Apple to request user's location information.   
It was called during a 3-minute recording of the traffic from a single opened app - Make More game. It didn't turn up ever before [when I was analysing other apps] + this game is on the Gravy list.   
  
However, I don't want to make false claims saying that this app was responsible for Apple's request – that endpoint is not accessible directly for any app except for iOS itself, so in order to get the information from it an app needs to call a dedicated Apple API method and have corresponding permissions. Or maybe not? 

Anyway, the response to this request was encoded in protobuf format, so I had to find a way to decode it, obviously. And I found it. 

But that's a topic for another post – stay tuned!

## Sign up for tim.sh

Thoughts, stories and ideas.

Subscribe

Email sent! Check your inbox to complete your signup. 

No spam. Unsubscribe anytime.

I really hope some people find this interesting enough to check at least 1 app and contribute to this process, or just to experiment and have fun. 

If you have any comments, ideas or just want to chat about it – hit me up at [[email protected]](/cdn-cgi/l/email-protection#caa2afa6a6a58abea3a7b9a2e4a5b8ad). 

## Read more

[ ![Scam Telegram: Uncovering a network of groups spreading crypto drainers](/content/images/size/w600/2025/11/PREVIEW-1.png) Scam Telegram: Uncovering a network of groups spreading crypto drainers I accidentally discovered a network of hundreds of fake DeFi support chats spreading various phishing sites with wallet stealers and drainers, including infamous Inferno Drainer. TL;DR While searching for a contact of a member of one DeFi project, I found a fake "Official Support" group with botted By tim 05 Dec 2025 ](/scam-telegram-investigation/) [ ![Why you should self-host your \(vibecoded\) app](/content/images/size/w600/2025/10/self-hosting.png) Why you should self-host your (vibecoded) app Intro Over the last 5 years I had to deploy more than 50 different services, both at the companies I used to work at, my personal projects and at my now-dead startup, Track Pump. I started this journey with almost 0 knowledge about servers, dockers, CI/CDs and so on By tim 07 Oct 2025 ](/why-you-should-self-host/) [ ![Switching to Claude Code + VSCode inside Docker](/content/images/size/w600/2025/07/new-d.png) Switching to Claude Code + VSCode inside Docker Last night I finished a transition from my old AI coding setup I've been using for a while to running Claude Code in Docker using VSCode's "Dev Container" feature. In this post I lay out a few of my thoughts on why I wanted By tim 11 Jul 2025 ](/claude-inside-docker/) [ ![Github scam investigation: Thousands of "mods" and "cracks" stealing your data](/content/images/size/w600/2025/02/github-scams-flow.png) Github scam investigation: Thousands of "mods" and "cracks" stealing your data While looking through the articles on a "social engineering" themed forum I discovered a relatively new scam scheme that shocked me. People create thousands of GitHub repositories with all sorts of things - from Roblox and Fortnite mods to "cracked" FL Studio and Photoshop. As soon By tim 27 Feb 2025 ](/github-scam-investigation-thousands-of-mods-and-cracks-stealing-your-data/)

tim.sh 

  * Subscribe



Powered by [Ghost](https://ghost.org/)

##  tim.sh 

privacy, security and self-hosting related stuff 

Subscribe
