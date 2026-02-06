# CSRF Protection without Tokens or Hidden Form Fields

**来源:** https://miguelgrinberg.com
**链接:** https://blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields
**日期:** Sun, 21 Dec 2025 15:54:28 GMT

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



# [CSRF Protection without Tokens or Hidden Form Fields](/post/csrf-protection-without-tokens-or-hidden-form-fields)

##  Posted by  on 2025-12-21T15:54:28Z under 

A couple of months ago, I received a [request](https://github.com/miguelgrinberg/microdot/issues/321) from a random Internet user to add [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection to my little web framework [Microdot](https://github.com/miguelgrinberg/microdot), and I thought it was a fantastic idea.

When I set off to do this work in early November I expected I was going to have to deal with anti-CSRF tokens, double-submit cookies and hidden form fields, pretty much the traditional elements that we have used to build a defense against CSRF for years. And I did start along this tedious route. But then I bumped into a new way some people are dealing with CSRF attacks that is way simpler, which I describe below.

## Implementing a security feature

An often shared piece of advice is that you should never implement security features yourself. Instead, you should look for well established solutions built by people who think about security day in and day out.

Unfortunately, as the lead (and only) maintainer of Microdot, I do not have an ecosystem of existing solutions available to me. Even though I gladly accept external contributions, most of the framework has been built by myself out of nothing. So in this case, like many other times before, I felt I had no choice but to go against the standard advice and write CSRF protection code by myself, because if I didn't do it then the feature would not be built.

What is the first step when you need to build a security feature? Check out what [OWASP](https://owasp.org/) has to say about the matter.

So, in early November, I opened OWASP's [CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) page to see what was new and interesting in the world of CSRF protection. And I found that nothing of significance had changed.

According to OWASP, the best CSRF protection you could get (at the time I checked) was still built around the idea of using anti-CSRF tokens. So I set off to implement this for Microdot.

## A disturbance in the (CSRF) force

I was happily making progress on my CSRF implementation, and then in early December, another random Internet user dropped [an issue](https://github.com/pallets/flask/issues/5863) on the Flask repository, proposing that Flask adds support for "modern" CSRF protection. Modern? How could there be a new way to protect against CSRF that isn't mentioned by OWASP?

This led me down a rabbit hole of blog posts and discussions spanning the Go and Ruby communities, plus a [long discussion](https://github.com/OWASP/CheatSheetSeries/issues/1803) about this method on the OWASP GitHub repository itself, resulting in a [pull request](https://github.com/OWASP/CheatSheetSeries/pull/1875) that added a [mention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#fetch-metadata-headers) of this method to the CSRF Cheat Sheet, only a couple of weeks after I went to this page looking for guidance for my own implementation.

## Modern CSRF Protection

The so called "modern" method to protect against CSRF attacks is based on the [Sec-Fetch-Site](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Site) header, which all modern desktop and mobile browsers include in the requests they send to servers. According to Mozilla, all browsers released since March 2023 have support for this header.

The `Sec-Fetch-Site` header can have one of four values:

  * `same-origin`, when the request comes from the same origin as the target server
  * `same-site`, when the request comes from the same site, but not exactly the same origin (e.g. a different subdomain) as the target server
  * `cross-site`, when the request comes from an origin that does not match the target server
  * `none`, when the request is originated by the user



The value of this header cannot be set via JavaScript, so the server can assume that a) if this header is present, then the client is a web browser, and b) the value of the header can be trusted. So basically, the server can reject requests that come with this header set to `cross-site`, and in essence that is all you need to do to protect against CSRF!

After seeing this, I paused my work on the token-based CSRF implementation and spent a few hours to implement this modern approach. As always, the devil is in the details, so let's see what else I needed to do to build a complete solution.

First of all, in some cases subdomains sharing the same registered domain may operate independently, and as such, it is not out of the question that one subdomain may attempt to attack another through CSRF. Depending on the level of trust an application has for other subdomains, a server may want to block requests that come with the `Sec-Fetch-Site` header set to `same-site`. In Microdot, I have added an argument `allow_subdomains` to cover this case. I decided to err on the side of security, so the default is `False`, meaning that requests from subdomains are also blocked.

The other big problem is that not everyone is using a recent browser that implements this header. Looking at the [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Site#browser_compatibility) for the `Sec-Fetch-Site` header, you can see that most browsers implemented this feature long ago, between 2019 and 2021, with one notable exception: Safari. Apple added this header to its browser in 2023, so it is reasonable to assume that there are still users out there running older browsers that do not support it.

One option is to reject all requests that do not have the `Sec-Fetch-Site` header. This keeps everyone secure, but of course, there's going to be some unhappy users of old devices that will not be able to use your application. Plus, this would also reject HTTP clients that are not browsers. If this is not a problem for your use case, then great, but it isn't a good solution overall.

From what I gathered from looking at other implementations of this method, an accepted solution is to use the `Origin` header as fallback when `Sec-Fetch-Site` is not implemented, since this header has been around for [much longer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin#browser_compatibility). The last of the major browsers to add it were Firefox desktop in 2019 and Edge and Firefox mobile in 2020. Like `Sec-Fetch-Site`, the `Origin` header is also a restricted header that is set by the browser, so it can also be used to determine from where a request is coming from.

The problem with using the `Origin` header is that it isn't always easy to know what is the correct origin that applies to a web application. The standard option is to compare the value of the `Origin` header against the value of the `Host` header, but `Host` only includes the hostname and port, while `Origin` also includes the scheme. Also, the `Host` header is overwritten as it passes through reverse proxies. So comparing these two headers is actually not easy.

Another, more direct option is to ask the user to configure the expected origin name explicitly. To keep things simple, in Microdot I opted for the explicit configuration, for which I linked to the existing Cross-Origin Request Sharing (CORS) support. The CORS feature already maintains a list of allowed origins, so my CSRF logic automatically trusts these. I decided to not complicate myself adding support for `Host` header checks at this time, but maybe I'll add this in the future.

Filippo Valsorda, a security developer active in the Go ecosystem (and author of the popular [mkcert](https://github.com/FiloSottile/mkcert) tool) wrote a [blog post](https://words.filippo.io/csrf/) about this method that you may want to check out if you want to learn more details about it. He seems to be the first to propose this method and has implemented it for the Go standard library.

Also if you are interested, feel free to review my implementation of CSRF protection in Microdot. Have a look at the [documentation](https://microdot.readthedocs.io/en/latest/extensions/csrf.html), the [code](https://github.com/miguelgrinberg/microdot/blob/main/src/microdot/csrf.py) and an [example](https://github.com/miguelgrinberg/microdot/tree/main/examples/csrf), and let me know if you have any improvements or fixes to suggest.

## Let's revisit OWASP

_Note: this section is now out of date. As of December 24th 2025 the OWASP CSRF Cheat Sheet page lists the Fetch Metadata method as a complete solution that can be used as an alternative to token-based approaches._

As I mentioned above, the CSRF Prevention Cheat Sheet page from OWASP was updated in early December to include the use of the `Sec-Fetch-Site` header in the list of prevention methods. But this method is currently listed as a [defense in depth](https://en.wikipedia.org/wiki/Defence_in_depth) mechanism, and not a complete solution, which I thought was odd.

I referenced the [discussion](https://github.com/OWASP/CheatSheetSeries/issues/1803) in the OWASP GitHub repository that resulted in the recent changes made to the Cheat Sheet page. Several participants in that discussion have suggested that this method should be upgraded to a complete alternative to the standard token-based approaches. The OWASP maintainer was initially skeptical, but towards the end of the thread they have agreed. The [pull request](https://github.com/OWASP/CheatSheetSeries/pull/1875) that closed the discussion added this solution as an alternative to the token-based approaches, but then a later change made significant updates, including the downgrade to defense in depth. My hope is that this is just a misunderstanding, and that the OWASP folks will restore the content as it was agreed by all the parties involved.

In any case, I consider that in Microdot, going from no CSRF support at all to this is a great step forward that is also consistent with the minimalist ethos of the project. I will be keeping an eye on the OWASP CSRF Cheat Sheet page to see what is their final word on this new protection method, and if they end up keeping it as defense in depth, I still have a mostly complete implementation of double-submit anti-CSRF tokens that I can bring into my project.

## Conclusion

What I like the most about working in open source is that all the work happens in the open, so it is a permanent record that can be searched and reviewed. My CSRF protection journey started as a somewhat tedious exercise in the use of cryptography and cookies, but then thanks to an unexpected lead it turned into a fun and exciting learning opportunity for me.

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through [Buy me a coffee](https://www.buymeacoffee.com/miguelgrinberg). Thanks!

[![Buy Me A Coffee](/static/buymeacoffee-yellow.png)](https://www.buymeacoffee.com/miguelgrinberg)

## Share this post

[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields&t=CSRF%20Protection%20without%20Tokens%20or%20Hidden%20Form%20Fields) [ Reddit ](https://reddit.com/submit/?url=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields&resubmit=true&title=CSRF Protection without Tokens or Hidden Form Fields) [ Twitter ](https://twitter.com/intent/tweet/?text=CSRF%20Protection%20without%20Tokens%20or%20Hidden%20Form%20Fields&url=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields&title=CSRF%20Protection%20without%20Tokens%20or%20Hidden%20Form%20Fields&summary=CSRF%20Protection%20without%20Tokens%20or%20Hidden%20Form%20Fields&source=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields) [ Facebook ](https://facebook.com/sharer/sharer.php?u=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields) [ E-Mail ](mailto:?subject=CSRF%20Protection%20without%20Tokens%20or%20Hidden%20Form%20Fields&body=https%3A//blog.miguelgrinberg.com/post/csrf-protection-without-tokens-or-hidden-form-fields)

[10 comments](/post/csrf-protection-without-tokens-or-hidden-form-fields#comments)

  * ![](https://gravatar.com/avatar/52e856d4944bdff26afc59f123c48adf?s=60&d=identicon)

#1 Bot said 2025-12-25T02:28:06Z

While the Go standard library needs to cover all the edge cases (who uses http nowadays?). For any normal use case, you can just use sameSite=Lax and check the Referer value.

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#2 Miguel Grinberg said 2025-12-25T08:41:42Z

@Bot: The OWASP folks consider the SameSite cookie a defense in depth mechanism, not full protection. Read what they have to say [here](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#samesite-cookie-attribute).

  * ![](https://gravatar.com/avatar/b482000b6e3554ee69d69fddea82cf4e?s=60&d=identicon)

#3 Albert Peschar said 2025-12-25T11:08:31Z

One potential vulnerability that a token embedded in a hidden form field protects against, is where an attacker is able to inject HTML into a page on the same origin. A form tag pointing to the endpoint would let the attacker trick the user into submitting an attacker-controlled payload. This is the case even with a restrictive CSP preventing XSS.

If you use a token to protect against CSRF, an attacker would be unable to generate a form that could be successfully submitted.

  * ![](https://gravatar.com/avatar/92ac5b788c2deba6f814b149001ace53?s=60&d=identicon)

#4 lmao said 2025-12-25T12:48:50Z

let's hope some browser or a bad addon "accidentally" doesn't enforce this, lmfao

What happened to never trust user/(browser) supplied values?

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#5 Miguel Grinberg said 2025-12-25T16:37:54Z

@Albert: If you are vulnerable to XSS then you don't have much hope, even when you use CSRF tokens.

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#6 Miguel Grinberg said 2025-12-25T16:44:57Z

@lmao: if the user's browser is compromised, then there isn't really much you can do. The "bad addon" as you call it can also steal your CSRF token and submit a malicious form with it. But if you assume that the browser is not compromised, then the values of the `Sec-Fetch-First` and `Origin` headers cannot be forged except when the client is not a browser. Given that CSRF attacks are browser-specific, this isn't really a problem.

  * ![](https://gravatar.com/avatar/a68da6e6ffe44f0165b2992d15f46990?s=60&d=identicon)

#7 adeadfed said 2025-12-26T09:20:53Z

Howdy and Merry Christmas :) I was just passing by this post, so I don't have much of an insight into your web framework, but as Bot already mentioned, there are a lot of other tricks to prevent CSRF that might be useful, and I'm not sure why OWASP fails to mention them. Lax cookies would only fail to protect against CSRF in edge cases if someone decides to add a sensitive GET endpoint action (or if your framework does not respect HTTP verb when processing the request). Plus you can also add a custom static HTTP header to the frontend, e.g. X-Csrf: 1 and require it on the backend. The header will trigger a CORS preflight request which would block the actual request in the browser unless the CORS allows it explicitly. This would cut any CSRF attempts at all unless there is a flaw in your CORS allowlist. Any "non-standard" content type by CORS documentation on MSDN (e.g. application/json) would do the same job btw, so, honestly, a lot of stars need to align for a CSRF to happen in 2025 :) Nonetheless, great post! I haven't had much of an insight into Sec-* headers myself up to this point!

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#8 Miguel Grinberg said 2025-12-26T09:55:42Z

@adeadfed: if OWASP does not mention something, it is because they do not recommend it. They do mention lax cookies however. And injecting a random header does not work for regular forms, so it isn't a complete solution.

  * ![](https://gravatar.com/avatar/d5839961d3314fe5655fb63abbb96c15?s=60&d=identicon)

#9 theodore said 2026-01-21T19:09:09Z

What about using a custom header which should trigger pre-flight request and prevent CSRF. A technique also mentioned in the cheatsheet.

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#10 Miguel Grinberg said 2026-01-21T20:44:48Z

@theodore: same answer as above. You cannot insert a custom header in a web form, so this isn't a solution that you can use across the board for all types of requests.




  * [««](/post/csrf-protection-without-tokens-or-hidden-form-fields/page/1#comments)
  * [«](/post/csrf-protection-without-tokens-or-hidden-form-fields/page/0#comments)
  * [»](/post/csrf-protection-without-tokens-or-hidden-form-fields/page/0#comments)
  * [»»](/post/csrf-protection-without-tokens-or-hidden-form-fields/page/0#comments)



### Leave a Comment

Name

Email

Comment

Captcha

The React Mega-Tutorial

[ ![](/static/react-book-small.png) ](https://amzn.to/3LK7Skg)

If you would you like to support my [React Mega-Tutorial series](https://blog.miguelgrinberg.com/post/introducing-the-react-mega-tutorial) on this blog and as a reward have access to the complete tutorial in book and/or video formats, you can now order it from my [Courses](https://courses.miguelgrinberg.com/p/react-mega-tutorial) site or from [Amazon](https://amzn.to/3LK7Skg).

[Click here to get the Book!](https://amzn.to/3LK7Skg)  
[Click here to get the Video Course!](https://courses.miguelgrinberg.com/p/react-mega-tutorial)

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
