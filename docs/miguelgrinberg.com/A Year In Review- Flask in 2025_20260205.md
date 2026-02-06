# A Year In Review: Flask in 2025

**来源:** https://miguelgrinberg.com
**链接:** https://blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025
**日期:** Thu, 01 Jan 2026 12:00:26 GMT

---

[miguelgrinberg.com](/index)

  * [Home](/index)
  * [My Courses and Books](/post/my-courses-and-books)
  * [Consulting](/post/hire-me)
  * [About Me](/post/about-me)
  *     * [   Light Mode ](javascript:updateTheme\('light'\); setThemeUI\(\);)
    * [   Dark Mode ](javascript:updateTheme\('dark'\); setThemeUI\(\);)
    * * * *

    * [   System Default ](javascript:updateTheme\('auto'\); setThemeUI\(\);)


  * [![GitHub](/static/social/github.png)](http://github.com/miguelgrinberg) [![LinkedIn](/static/social/linkedin.png)](http://www.linkedin.com/in/miguelgrinberg) [![Bluesky](/static/social/bluesky.png)](https://bsky.app/profile/miguelgrinberg.com) [![Mastodon](/static/social/mastodon.png)](https://mstdn.social/@miguelgrinberg) [![Twitter](/static/social/twitter.png)](https://twitter.com/miguelgrinberg) [![YouTube](/static/social/youtube.png)](https://youtube.com/miguelgrinberg) [![Buy Me a Coffee](/static/social/buymeacoffee.png)](https://www.buymeacoffee.com/miguelgrinberg) [![Patreon](/static/social/patreon.png)](https://patreon.com/miguelgrinberg) [![RSS Feed](/static/social/rss.png)](/feed)



# [A Year In Review: Flask in 2025](/post/a-year-in-review-flask-in-2025)

##  Posted by  on 2026-01-01T12:00:26Z under 

Like I did [last year](https://blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2024), I reserved some time during my holiday break to prepare an independent report of the Flask ecosystem in 2025.

![Flask logo](/static/images/flask-logo.png)

## Project activity

Before I start showing you numbers, I feel it is necessary to clarify that I have not used large language models (LLMs) or other generative AI tools to help me create the reports you will see in this article. Consequently, the chance I'm showing you hallucinated data is zero. The chance of me having made a mistake is not zero, however, so please do check my work and if you find any errors let me know so that I can correct them!

Okay, let's get to it. The Flask project released twice during all of 2025, and both releases were patch releases to the 3.1.0 release that came out in November 2024. In short, not much has happened in Flask during 2025.

To put this into perspective, here is a table that shows the releases since 2018, the year in which version 1.0.0 came out:

Year | Major.Minor | Patch release count | Total releases  
---|---|---|---  
2018 | 1.0 | 4 | 5  
2019 | 1.1 | 3 | 4  
2020 |  | 2 | 2  
2021 | 2.0 | 4 | 5  
2022 | 2.1, 2.2 | 6 | 8  
2023 | 2.3, 3.0 | 6 | 8  
2024 | 3.1 | 3 | 4  
2025 |  | 2 | 2  
  
But of course, the releases do not tell the complete story. I also like to look at GitHub activity to see how things are going with the project. Below is a table that shows the number of pull requests that were merged per year, also since 2018:

Merged PRs | Flask | Werkzeug | Total  
---|---|---|---  
2018 | [111](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2018-01-01..2018-12-31) | [93](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2018-01-01..2018-12-31) | 204  
2019 | [142](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2019-01-01..2019-12-31) | [103](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2019-01-01..2019-12-31) | 245  
2020 | [120](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2020-01-01..2020-12-31) | [162](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2020-01-01..2020-12-31) | 282  
2021 | [178](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2021-01-01..2021-12-31) | [175](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2021-01-01..2021-12-31) | 353  
2022 | [134](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2022-01-01..2022-12-31) | [92](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2022-01-01..2022-12-31) | 226  
2023 | [111](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2023-01-01..2023-12-31) | [133](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2023-01-01..2023-12-31) | 244  
2024 | [58](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2024-01-01..2024-12-31) | [73](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2024-01-01..2024-12-31) | 131  
2025 | [26](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aclosed+merged%3A2025-01-01..2025-12-31) | [17](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aclosed+merged%3A2025-01-01..2025-12-31) | 43  
  
It is likely that there are a small number of commits that are not counted in this table because they were made directly and not through a pull request, but from a quick review of the commit log it does not appear this is something that the Flask maintainers do very often. So I feel this is an accurate representation of the project activity that confirms the decreasing trend that I also noted in my review of last year.

This time I thought it would be a good idea to also look at pull requests that were closed without merging. 

Unmerged PRs | Flask | Werkzeug | Total | %  
---|---|---|---|---  
2018 | [64](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2018-01-01..2018-12-31) | [52](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2018-01-01..2018-12-31) | 116 | 36%  
2019 | [68](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2019-01-01..2019-12-31) | [19](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2019-01-01..2019-12-31) | 87 | 26%  
2020 | [76](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2020-01-01..2020-12-31) | [35](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2020-01-01..2020-12-31) | 111 | 28%  
2021 | [109](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2021-01-01..2021-12-31) | [50](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2021-01-01..2021-12-31) | 159 | 31%  
2022 | [90](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2022-01-01..2022-12-31) | [36](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2022-01-01..2022-12-31) | 126 | 36%  
2023 | [81](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2023-01-01..2023-12-31) | [34](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2023-01-01..2023-12-31) | 115 | 32%  
2024 | [53](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2024-01-01..2024-12-31) | [24](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2024-01-01..2024-12-31) | 77 | 37%  
2025 | [99](https://github.com/pallets/flask/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2025-01-01..2025-12-31) | [14](https://github.com/pallets/werkzeug/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2025-01-01..2025-12-31) | 113 | 72%  
  
And this is quite interesting. Historically, the percentage of all pull requests that ended up closed without merging was hovering around 30%, but in 2025 it jumped to 72%. I guess one possible explanation to this large increase could be that the Flask maintainers consider that the project is now fairly complete, so they are less interested in accepting contributions from the community.

Another explanation is that in 2025 many developers started using generative AI tools to create pull requests. This is a new trend that I noticed on my own projects as well. These pull requests are almost always bad, and the contributors that submit them do not have the interest nor the knowledge to improve them. One example that supports this theory is this simple [documentation issue](https://github.com/pallets/flask/issues/5825). There is currently an [open pull request](https://github.com/pallets/flask/pull/5827) for it that is awaiting review from the maintainers, but I counted 7 closed PRs from people who submitted their own versions of this fix, most of them dated after the currently in-progress one, and all failing to properly address the reported issue.

## What's new in Flask

This was an extremely slow year for Flask, so there is nothing really new and exciting to report. There is a fix for an issue that prevented the `stream_with_context` from working in asynchronous routes. Aside from this, there were a handful of Python typing fixes and a change in the order in which rotated secret keys are tried. The changes that went into Werkzeug during 2025 were also minor and equally uninteresting.

I reviewed the list of 43 pull requests that were merged during 2025 for the Flask and Werkzeug projects, to see if I could find anything worth reporting that is not reflected in the change logs or that maybe hasn't been released yet. And I did find a couple of nuggets.

In the [2024 review](https://blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2024), I reported that there was a plan to merge the application and request contexts into a single context. This change has already been made, and will be included in the 3.2.0 release, which does not have a date yet. Overall, my opinion of this change can be summarized in three letters: "meh". It is a large internal change that simplifies and restructures the context handling logic, but for Flask users this does not appear to bring any substantial benefits. At least I fail to see them if they exist.

There are good news and bad news about this change. The good news is that there are only very minor externally facing behavior changes planned for the upcoming 3.2 release. The functionality of the request context was moved to the app context, but in 3.2 there will still be a request context, although it will be deprecated. You may see some deprecation warnings from your own code or from Flask extensions that access the request context directly, but aside from that everything will hopefully continue to work as before.

The bad news is that the request context will be removed completely when 4.0 is released, so at that point I expect some applications will stop working and will need code changes or dependency updates before they can be upgraded to the latest version of Flask. What's unclear to me is when will 4.0 be released, what will be in it besides this, and how much time and how many more minor releases there will be between 3.2 and 4.0. At the current pace of development it is really hard to find justification for a new major release anyway, so maybe this isn't going to be a problem for a while. We'll have to see how the Flask maintainers handle this transition.

Another interesting change that isn't mentioned in the change log is that since the 3.1.1 release Flask and Werkzeug have switched to the [uv](https://docs.astral.sh/uv/) package manager for its continuous integration and release jobs on GitHub Actions.

## What about Quart?

As I'm sure most of you know, [Quart](https://quart.palletsprojects.com/en/latest/) is an async-native port of Flask, created by Phil Jones and also maintained by the Flask core developers, a group that includes Phil as well.

Sadly, Quart did not have any releases in 2025. The last release is 0.20.0, which came out in December 2024.

Looking at the [Quart repository](https://github.com/pallets/quart) on GitHub, there have been only 14 commits in all of 2025, and they were all for minor things such as adding a new logo, improving type hints or fixing documentation typos. 

## Flask extensions

This time around I thought it would be good to take a quick look at the most frequently used extensions for Flask and see how active they have been.

Extension | Last release | Last commit  
---|---|---  
[Flask-Login](https://github.com/maxcountryman/flask-login) | October 2023 | August 2025  
[Flask-Security](https://github.com/pallets-eco/flask-security) | November 2025 | December 2025  
[Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth) (*) | August 2023 | December 2025  
[Flask-SQLAlchemy](https://github.com/pallets-eco/flask-sqlalchemy) | September 2023 | June 2025  
[Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) (*) | January 2025 | December 2025  
[Flask-Session](https://github.com/pallets-eco/flask-session) | March 2024 | April 2024  
[Flask-WTF](https://github.com/pallets-eco/flask-wtf) | October 2024 | December 2025  
[Flask-Mail](https://github.com/pallets-eco/flask-mail) | May 2024 | June 2025  
[Flask-Admin](https://github.com/pallets-eco/flask-admin) | November 2025 | December 2025  
[Flask-Babel](https://github.com/python-babel/flask-babel) | October 2023 | June 2024  
[Flask-CORS](https://github.com/corydolphin/flask-cors) | December 2025 | December 2025  
[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) (*) | December 2025 | December 2025  
[Flask-Moment](https://github.com/miguelgrinberg/Flask-Moment) (*) | January 2025 | December 2025  
  
I came up with this list from memory, so please don't be offended if I missed some of your favorite extensions. Also, inclusion in this list doesn't mean I'm making an endorsement. In fact, some of these extensions I do not like and never use in my projects. I do, however, fully endorse the ones that are marked with (*), as these are maintained by myself.

Something that is important to mention is that several of these extensions are currently maintained by the [pallets-eco](https://github.com/pallets-eco) organization, a group of volunteers dedicated to keeping extensions updated after their original creators or maintainers move on to other things.

## Flask vs. other web frameworks

Let's see how Flask stands against competing Python web frameworks.

First we can compare download counts. For this I'm using the [PyPI BigQuery dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=pypi&page=dataset), which has download counts for all PyPI packages.

Downloads | Flask | Django | FastAPI  
---|---|---|---  
2023 | 1001M (73%) | 135M (10%) | 228M (17%)  
2024 | 1160M (58%) | 225M (11%) | 612M (31%)  
2025 | 1577M (46%) | 313M (9%) | 1523M (45%)  
  
From this table you can see that the three leading frameworks all gained downloads, but FastAPI did it at an incredible pace. In practical terms, Flask and FastAPI are now tied at the top.

But of course, the download numbers for Django are suspiciously low. I noticed this last year, and couldn't find an explanation, so if you have any theories let me know. Below you can see the queries that I used to get the 2025 download counts, in case you want to debug them and investigate this difference in downloads:
    
    
    SELECT COUNT(*) FROM `bigquery-public-data.pypi.file_downloads` WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP("2025-01-01") AND TIMESTAMP("2026-01-01") AND file.project = "flask"
    SELECT COUNT(*) FROM `bigquery-public-data.pypi.file_downloads` WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP("2025-01-01") AND TIMESTAMP("2026-01-01") AND file.project = "django"
    SELECT COUNT(*) FROM `bigquery-public-data.pypi.file_downloads` WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP("2025-01-01") AND TIMESTAMP("2026-01-01") AND file.project = "fastapi"
    

We can also have a look at the last [Python developer survey](https://lp.jetbrains.com/python-developers-survey-2024), which was conducted in Q4 of 2024, but is the last one available at the time I'm writing this in December 2025. Here is how the top three web frameworks split among developers in the last two surveys:

Survey | Flask | Django | FastAPI  
---|---|---|---  
2023 | 33% | 33% | 29%  
2024 | 34% | 35% | 38%  
  
Here we can see once again that FastAPI is unstoppable at the moment. And before this is asked in the comments, the answer is no, I'm not currently planning a FastAPI Mega-Tutorial. But I never say never...

And with this, I conclude this review of the Flask project in 2025. I hope you find this analysis useful. Happy 2026, and I hope you'll be back in one year for another Flask review!

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through [Buy me a coffee](https://www.buymeacoffee.com/miguelgrinberg). Thanks!

[![Buy Me A Coffee](/static/buymeacoffee-yellow.png)](https://www.buymeacoffee.com/miguelgrinberg)

## Share this post

[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025&t=A%20Year%20In%20Review%3A%20Flask%20in%202025) [ Reddit ](https://reddit.com/submit/?url=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025&resubmit=true&title=A Year In Review: Flask in 2025) [ Twitter ](https://twitter.com/intent/tweet/?text=A%20Year%20In%20Review%3A%20Flask%20in%202025&url=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025&title=A%20Year%20In%20Review%3A%20Flask%20in%202025&summary=A%20Year%20In%20Review%3A%20Flask%20in%202025&source=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025) [ Facebook ](https://facebook.com/sharer/sharer.php?u=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025) [ E-Mail ](mailto:?subject=A%20Year%20In%20Review%3A%20Flask%20in%202025&body=https%3A//blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025)

[4 comments](/post/a-year-in-review-flask-in-2025#comments)

  * ![](https://gravatar.com/avatar/89af003084a57fba080580a721ae071d?s=60&d=identicon)

#1 Bhavesh Kakwani said 2026-01-01T20:11:24Z

It could be the Django downloads are low because it’s rarely the framework of choice in beginner tutorials. For e.g. the Harvard CS50 online course is based on Flask. Project starter templates on beginner friendly services like Replit are also based on Flask. So I’m wondering if we have a super large number of students using Flask, thus contributing to the number of downloads. I don’t have a theory for FastAPI though

  * ![](https://gravatar.com/avatar/26ccd6073f401813f7e915babd80a49d?s=60&d=identicon)

#2 Eric Mesa said 2026-01-02T21:29:35Z

Thanks for putting this together. I have also had some of my personal projects achieve a "done" state, so I can understand Flask not having much more added to it in 2025. The only "bad" thing is that sometimes a lack of updates in Github can be seen as a bad thing. On the other hand, I've read/heard a lot about a move towards AI coding leading to a recommendation of older frameworks. This may advantage Flask over FastAPI or anything else that comes in the future. 

If I could wave a magic wand in the world of Python frameworks, I would have flask/quart merge "already" OR flask deprecated in favor of quart. I think the async story is only getting more and more important as time goes on and having a non-async web framework will eventually hurt Flask. Then again, maybe I'm wrong. I am not using Flask professionally and maybe in the real world it's less of an issue than it seems to be from tech blogs and tech podcasts.

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#3 Miguel Grinberg said 2026-01-02T23:45:49Z

@Eric: If merging Flask and Quart were easy, it would have happened already. The fact is that there are technical problems that make this really hard, bordering on impossible. And Flask not having good asyncio support is less of a problem than people make it to be, in my opinion.

  * ![](https://gravatar.com/avatar/97baa9284d0e84dc97fe5796e9e8a6e1?s=60&d=identicon)

#4 Adam Bhogal said 2026-01-09T18:48:12Z

Good to see SQL Alchemy in fourth place in the extensions list. Although the official website is useful, the language and explanation can be quite daunting. I personally find your books very helpful in this regard and believe your resources are possibly contributing to debunking and simplifying the mapping of python objects to a database. Pre-Covid it was also a straight choice between Flask or Django fro Python web development. Don't know much about FastAPI but it certainly seems to have broken through in a big way.




  * [««](/post/a-year-in-review-flask-in-2025/page/1#comments)
  * [«](/post/a-year-in-review-flask-in-2025/page/0#comments)
  * [»](/post/a-year-in-review-flask-in-2025/page/0#comments)
  * [»»](/post/a-year-in-review-flask-in-2025/page/0#comments)



### Leave a Comment

Name

Email

Comment

Captcha

The Flask Mega-Tutorial

##### [New 2024 Edition! ](/post/announcing-the-flask-mega-tutorial-2024-edition)

[ ![The New Flask Mega-Tutorial](/static/mega-tutorial-2024-small.png) ](https://amzn.to/3MQffrm)

If you would you like to support my work on my [Flask Mega-Tutorial series](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) on this blog and as a reward have access to the complete tutorial nicely structured as a book and/or a set of videos, you can now order it from my [Courses](https://courses.miguelgrinberg.com/p/flask-mega-tutorial) site or from [Amazon](https://amzn.to/3MQffrm).

[Click here to get the Book!](https://amzn.to/3MQffrm)  
[Click here to get the Video Course!](https://courses.miguelgrinberg.com/p/flask-mega-tutorial)

About Miguel

![](/static/miguel.jpg)

Welcome to my blog!

I'm a software engineer and technical writer, currently living in Drogheda, Ireland.

You can also find me on [Github](https://github.com/miguelgrinberg), [LinkedIn](http://www.linkedin.com/in/miguelgrinberg), [Bluesky](https://bsky.app/profile/miguelgrinberg.com), [Mastodon](https://mstdn.social/@miguelgrinberg), [Twitter](https://twitter.com/miguelgrinberg), [YouTube](https://youtube.com/miguelgrinberg),  [Buy Me a Coffee](https://www.buymeacoffee.com/miguelgrinberg), and [Patreon](https://patreon.com/miguelgrinberg).

Thank you for visiting!

Categories

[![AI RSS Feed](/static/rss-small.png)](/category/AI/feed) _3_

[![Arduino RSS Feed](/static/rss-small.png)](/category/Arduino/feed) _7_

[![Authentication RSS Feed](/static/rss-small.png)](/category/Authentication/feed) _10_

[![Blog RSS Feed](/static/rss-small.png)](/category/Blog/feed) _1_

[![C++ RSS Feed](/static/rss-small.png)](/category/C++/feed) _5_

[![CSS RSS Feed](/static/rss-small.png)](/category/CSS/feed) _1_

[![Cloud RSS Feed](/static/rss-small.png)](/category/Cloud/feed) _11_

[![Database RSS Feed](/static/rss-small.png)](/category/Database/feed) _23_

[![Docker RSS Feed](/static/rss-small.png)](/category/Docker/feed) _5_

[![Filmmaking RSS Feed](/static/rss-small.png)](/category/Filmmaking/feed) _6_

[![Flask RSS Feed](/static/rss-small.png)](/category/Flask/feed) _130_

[![Games RSS Feed](/static/rss-small.png)](/category/Games/feed) _1_

[![IoT RSS Feed](/static/rss-small.png)](/category/IoT/feed) _8_

[![JavaScript RSS Feed](/static/rss-small.png)](/category/JavaScript/feed) _37_

[![MicroPython RSS Feed](/static/rss-small.png)](/category/MicroPython/feed) _10_

[![Microdot RSS Feed](/static/rss-small.png)](/category/Microdot/feed) _1_

[![Microservices RSS Feed](/static/rss-small.png)](/category/Microservices/feed) _2_

[![Movie Reviews RSS Feed](/static/rss-small.png)](/category/Movie Reviews/feed) _5_

[![Personal RSS Feed](/static/rss-small.png)](/category/Personal/feed) _3_

[![Photography RSS Feed](/static/rss-small.png)](/category/Photography/feed) _7_

[![Product Reviews RSS Feed](/static/rss-small.png)](/category/Product Reviews/feed) _2_

[![Programming RSS Feed](/static/rss-small.png)](/category/Programming/feed) _197_

[![Project Management RSS Feed](/static/rss-small.png)](/category/Project Management/feed) _1_

[![Python RSS Feed](/static/rss-small.png)](/category/Python/feed) _175_

[![REST RSS Feed](/static/rss-small.png)](/category/REST/feed) _7_

[![Raspberry Pi RSS Feed](/static/rss-small.png)](/category/Raspberry Pi/feed) _8_

[![React RSS Feed](/static/rss-small.png)](/category/React/feed) _19_

[![Reviews RSS Feed](/static/rss-small.png)](/category/Reviews/feed) _1_

[![Robotics RSS Feed](/static/rss-small.png)](/category/Robotics/feed) _6_

[![Security RSS Feed](/static/rss-small.png)](/category/Security/feed) _13_

[![Video RSS Feed](/static/rss-small.png)](/category/Video/feed) _22_

[![WebSocket RSS Feed](/static/rss-small.png)](/category/WebSocket/feed) _2_

[![Webcast RSS Feed](/static/rss-small.png)](/category/Webcast/feed) _3_

[![Windows RSS Feed](/static/rss-small.png)](/category/Windows/feed) _1_

(C) 2012- by Miguel Grinberg. All rights reserved. [Questions?](mailto:webmaster _at_ miguelgrinberg _dot_ com)
