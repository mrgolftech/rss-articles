# The cost of running OpenBenches.org

**来源:** [shkspr.mobi](https://shkspr.mobi/blog/feed)
**发布时间:** Tue, 03 Feb 2026 12:34:16 +0000
**链接:** https://shkspr.mobi/blog/2026/02/the-cost-of-running-openbenches-org/

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
After my recent presentation at FOSDEM, someone asked a pretty reasonable question. What does it cost to run
OpenBenches
?
\n\n
It is, thankfully, surprisingly cheap! In part, that\'s because it is a relatively simple tech stack - PHP, MySQL, a couple of API calls to external services. It was designed to be as low cost while also being useful. Here\'s the breakdown:
\n\n
Hosting - £171 per year
\n\n
Our biggest expense but, I think, our most reasonable.
Krystal
charges around £342 for a 2 year contract. That includes unlimited bandwidth and storage, as well as the domain name.  We have nearly 400GB of photos and bot scraping means we can use over 900GB of bandwidth per month - so Krystal give us a rather good deal!
\n\n
\n\n
Use
this affiliate link and code
EDENT
to get a small discount.
\n\n
Stadia Maps - US$20 / month
\n\n
Geocoding is surprisingly hard to do locally. We need to transform latitude and longitude into addresses, and then back again.
Stadia Maps
cost about the same as our hosting! What\'s rather annoying is that we only use about half the API calls in our plan. We need to find a cheaper solution.
\n\n
Mapping - Free!
\n\n
When we used Stadia for drawing maps, we regularly ran over our quota. So we switched to
OpenFreeMap
which produces gorgeous interactive maps.
\n\n
The service has been rock solid and very responsive to bugs on GitHub.
\n\n
Logo - US$5
\n\n
I\'m not a good designer, so we bought a
logo from The Noun Project
and then coloured it in. Bargain for a fiver!
\n\n
Image CDN - Free!
\n\n
Although we have unlimited bandwidth with Krystal, we\'re only located in one region - the UK.
WeServ
. It\'s also pointless serving full resolution images to small screens.
\n\n
So WeServ offers free image resizing and global CDNs. Personally, I\'m not a fan of CloudFlare (their CDN partner) so I\'m looking to change provider.
\n\n
OCR - Free!
\n\n
People don\'t want to type in the inscription of the photo, so we use
Google Cloud Vision
.
\n\n
We send less than 1,000 requests per month -
so we\'re inside their free tier
. If we get more popular, that\'ll get more expensive. But I don\'t know of a local-first OCR which is as good as Google\'s. Sadly, Tesseract is rubbish for extracting text from photos.
\n\n
Authentication - Free!
\n\n
We don\'t want to store anyone\'s passwords. The
free tier of Auth0
allows us to do social login for up to 25,000 monthly users. Which is more than enough for us.
\n\n
Sadly, Auth0 don\'t support the Fediverse,
so I had to build my own "Log-in with Mastodon" service
.
\n\n
As much as we\'d like to run social login locally, we simply don\'t want to be responsible for securing users\' details & API keys.
\n\n
Software - Free!
\n\n
As per
the OpenBenches colophon
we use a lot of cool FOSS. Small JS libraries, big PHP frameworks, and everything in between.
\n\n
Income
\n\n
Thanks to
GitHub Sponsors
we make a whopping US$3 per month!
\n\n
Similarly, our
OpenCollective Sponsors
brings in about £3 per month.
\n\n
Merchandising! You can
buy OpenBenches branded t-shirts, mugs, and hats
. That nets us about £20 per year
\n\n
Call it roughly £80 income. OK, it is better than nothing - but doesn\'t even cover a quarter of our costs. Sometimes people give us a higher donation privately, which is also very welcome. These people are
listed on our README
.
\n\n
Total
\n\n
On the assumption that our time is worthless (ha!) and that we only rarely go over our providers\' API limits, and we get in
some
revenue, the cost of running OpenBenches is less than £300 per year.
\n\n
That\'s not bad for a fun little hobby. People certainly spend more than that on Funkopops, vaping, and mechanical keyboards!
\n\n
Nevertheless, I\'m always slightly worried that we\'ll go viral and have an unexpectedly high bill from our API providers.
\n\n
I would love to be able to hire a proper designer to make the site look a bit nicer. I also want to be able to buy a modern iPhone so that I can test it in the latest Safari.
\n\n
If you have any suggestions for cutting costs, or non-scummy ways to help us raise funds, please drop a comment below.
'}

---

*抓取时间: 2026-02-05 12:59:04*
