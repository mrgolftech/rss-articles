# How to Securely Store Secrets in Environment Variables

**来源:** https://miguelgrinberg.com
**链接:** https://blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables
**日期:** Sun, 14 Dec 2025 15:33:33 GMT

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



# [How to Securely Store Secrets in Environment Variables](/post/how-to-securely-store-secrets-in-environment-variables)

##  Posted by  on 2025-12-14T15:33:33Z under 

You may have seen the recent reports of a [malware](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/) that stole API keys, tokens and other secrets from a large number of developers. From where were these secrets stolen from? You guessed it, they were mostly stolen from environment variables.

We use environment variables to configure information that processes need to run, but this type of storage was not designed for security, so using the environment for secrets always comes with risk. Given how serious this recent attack was, I thought it would be good to write a short article describing how I manage my secrets as part of my open source work.

## How I protect secrets in my computer

The measures that I take to protect secrets from being stolen by malware from my own computer come from the idea that it is impossible to steal something that isn't there to be stolen. Let me try to explain what I mean by this.

Let's assume that one day I'm installing a JavaScript or Python package that I need for a project, and that this install also brings a transitive dependency that has been compromised. Let's say that the compromised package includes malicious code that looks for secrets that it can exfiltrate in the environment and in files, and that it does this inconspicuously while it is being installed. When running on my machine, this malicious code would not find anything that is worth stealing, or at least that is what I expect, if I'm doing this right.

The environment variables that I maintain in my shell sessions are only the ones that allow my machine to work. Boring things such as `PATH`, `HOME`, `TERM` and the like. In addition, I avoid storing secrets in files, and when I can't avoid it, I use encryption. This is because disk files are also an easy target for malware.

So where do I keep my secrets then, if they are not stored on environment variables or in files? My secrets are all stored in my [Bitwarden](https://bitwarden.com/) account.

Bitwarden is a password manager that stores all your secrets with strong encryption in the cloud. It is not special in any way, so if for whatever reason you don't like Bitwarden, there are [many other password managers](https://en.wikipedia.org/wiki/List_of_password_managers) to choose from. I actually was inspired to write this article by Hugo van Kemenade's [blog post](https://hugovk.dev/blog/2025/secrets-in-env-vars/), in which he shows how he uses [1Password](https://1password.com/) for a similar purpose. The point is, if you aren't using a password manager yet, I strongly suggest that you pick one and start.

To inject secrets into the applications that need them, I use `bw`, the Bitwarden CLI. Here is an example script that I use to securely run the `twine` utility to publish a package to PyPI, the Python package registry:
    
    
    #!/bin/bash -e
    source <(bw get notes pypi)
    TWINE_USERNAME=__token__ TWINE_PASSWORD=$PYPI_TOKEN exec twine $*
    

The `bw get notes pypi` command retrieves the `notes` field of a secret stored with the name `pypi` in my Bitwarden vault. To retrieve this secret, the `bw` command needs to ask for my Bitwarden passphrase. This is necessary because my account needs to be unlocked for a short moment to retrieve the secret. The account is locked back after the secret is retrieved.

What I store in these notes are one or more variable assignments, whatever this specific secret needs. Here is an example of what the `notes` field looks like for my `pypi` entry:
    
    
    PYPI_TOKEN=xxxxxxxx
    

The `source` command imports the contents of the `notes` field that were retrieved from the password manager. This is done using a feature of UNIX shells called [process substitution](https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html), which allows the `source` command to treat the output of `bw` as if it was coming from a file. The result of importing this is that the `PYPI_TOKEN` environment variable defined in the `notes` field of my secret is now set in the private environment of the bash script.

Then comes the `exec`, which starts `twine` with all the arguments that were given to the script plus two additional variables, `TWINE_USERNAME` and `TWINE_PASSWORD`, which I set explicitly. The `exec` command causes the `twine` process to take the place of the bash script itself, so the bash process that was holding my `PYPI_TOKEN` variable is gone and in its place now there is `twine` with the two environment variables I gave it, which enable it to do the publishing. As soon as `twine` ends, the environment goes away, and at that point my PyPI token disappears from my computer.

That's really all there is to it! But note that this isn't the only way to integrate `bw` with applications. I have evolved this method over a long time, and keep evolving it. Keep in mind that there are many other ways to do this, and some ways are possibly better than mine. If you spot any issues with my method I'd like to know.

I expect there will be questions, so I'll just ask and answer the ones I expect that are likely to come up.

### Do you have to type your Bitwarden passphrase every time you need to use a secret?

Yes, that is how I set up my current workflow.

Bitwarden allows you to keep your account unlocked for a longer period of time, and during that time secrets can be retrieved without entering credentials. I don't feel comfortable running a terminal session that has access to all my secrets without authentication, so I do not do this. My Bitwarden account is locked at all times.

### Why don't you use Trusted Publishing with PyPI?

[Trusted Publishing](https://docs.pypi.org/trusted-publishers/) is a relatively recent solution that has been devised for package maintainers to publish their packages to a registry. It works in GitHub Actions or other similar cloud-based build environments. When a release needs to be made, the maintainer kicks off a release job. This job requests a short-lived token from PyPI (or npm and other registries that implement this solution) and uses it to publish the package, all in the cloud. The token expires shortly after.

The interesting part of this method is that because GitHub has an established trust relationship with PyPI that it can use to prove its identity, there is no need for the package owner to actively authenticate during a release. This is great in terms of convenience, but it makes me a bit nervous. I get into this later in the article, but the cloud is a very dangerous environment to run processes that require authentication.

I consider trusted publishing fairly secure, don't get me wrong, but I'm not sure I can go as far as saying that it is more secure than the method based on local publishing that I described above. Even though I hold a long-lived PyPI token in my Bitwarden account, I never expose it inside my computer except in the environment of the `twine` process, and only for the few seconds it takes to publish a package. That is extremely secure!

On the other hand, the security of trusted publishing is guaranteed by PyPI and GitHub, and is outside of my control. I feel I can trust PyPI about doing a good job security-wise, but I sadly cannot say I have the same level of trust on GitHub and Microsoft, and especially on their GitHub Actions product, which is buggy and unstable. I imagine these days the engineers working on GitHub Actions are under a mandate to use generative AI for everything, which in my view increases the risk of security issues.

The sad truth is that GitHub Actions is a complex product. Even without security issues, it is easy to make mistakes that a clever hacker can exploit. A while ago, the popular [Ultralytics](https://pypi.org/project/ultralytics/) Python package [was hacked](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection) and several compromised releases with cryptocurrency miners were published on PyPI. They were using trusted publishing, but that did not protect them. In fact, the compromised release job was able to legitimately obtain PyPI tokens using the trusted publisher system that was already in place before the attack took place. I will go into more detail on the challenges of protecting secrets in the cloud later in this article.

### Wouldn't it be more secure to use short-lived tokens to publish to PyPI?

You bet. Unfortunately, only trusted publishers such as GitHub Actions can request tokens through the PyPI API. For regular users I believe the only way to get a token is to request it manually on the PyPI website. And if I wanted the token to be good only for a short time, then I would need to remember to go back to the website to revoke it after I'm done using it. A process that relies on a sequence of manual steps is less secure than a process that is fully scripted, because the chance of the user making mistakes or forgetting a step is far from zero. I really don't feel manually managing tokens achieves the goal of increased security. Using a long-lived token that is safely stored in my Bitwarden account with a fully automated process that only requires me to type my master password is not perfect, but I think it is the most secure option I have available.

What I would really like is for PyPI to offer short-lived tokens that I can request via their API in the same way GitHub can do it as a trusted publisher client. If I could get a brand new token that is only good for a couple of minutes, and is scoped to a specific package each time I need to do a release, that would be fantastic, as that would remove the need to store a long-lived token in my Bitwarden account. I feel this is especially important now, with projects starting to migrate away from GitHub. Sadly, the list of cloud platforms that PyPI supports for trusted publishing is quite small, so there aren't really a lot of options. If anyone working on PyPI is reading this, please let me know if you want to chat!

### How do you avoid storing secrets in files? What about your SSH private key and .env files for projects?

I do have an SSH private key on my computer. It is protected with a passphrase, so it would be useless to an attacker if stolen. SSH comes with a tool called `ssh-agent` that manages your keys and reduces the number of times you have to type passphrases to decrypt them.

For many of the projects I have on my computer I use _.env_ files to store configuration. On these files I feel it is okay to store local development database credentials, because I do not keep anything of value in these databases. I do not store credentials to production databases or databases that are in the cloud. Likewise, I do not store any tokens or API keys for cloud services, or any tokens that would generate usage charges if stolen and used (or abused) by someone other than myself.

### How can I protect my AWS, Azure, Digital Ocean or similar credentials using your method?

The nice thing about publishing a package to a registry is that this takes a few seconds, so the token that makes this action possible needs to be available just for a quick moment. When you are developing an application that needs access to cloud services, however, you may need to have access to your secrets every time you launch it, and having to unlock your password manager every time can become tedious and time consuming.

Unfortunately there are no great solutions for this use case. The only secure option is to not connect to cloud services during development, which eliminates the need to have secrets installed permanently on your computer. This isn't always possible, of course, but in many cases you can install local versions of the services you need to use while developing your applications. I often install Docker container versions of the services I need, be it a database or an [emulated AWS](https://github.com/localstack/localstack).

Many cloud services offer the option to create temporary credentials that you can use while you work. This is good because it avoids the need to have your long-term credentials exposed in your environment. Using `bw` you can create a wrapper script that uses the long-term credentials stored in the password manager to request short term credentials that are only valid for the time that you expect to need them each day. Short-term credentials do not eliminate your risk, but they reduce it significantly.

For cases where it is really impossible to avoid using secrets, I open a dedicated shell session for them. To make this easier you can use tools such as [direnv](https://direnv.net/) or [mise](https://mise.jdx.dev/) in combination with `bw`. These tools associate secrets with your project directory and ensure that the variables are removed from the environment automatically when you `cd` out of it. 

Are there any other questions about protecting secrets inside your computer? Feel free to ask below in the comments.

## How I protect secrets in the cloud

Protecting secrets in the cloud is much harder than doing it on your own computer. For processes that run in the cloud it is not possible to use a password manager, because operations are often automated and triggered by external events. You can't really have a person available to unlock a password manager each time a cloud process needs to be launched with access to some secrets.

If you are managing your own server, then you can harden the server's external perimeter. If you are reasonably confident that an attacker will not be able to penetrate this perimeter, then you have some flexibility to store secrets inside the server, either by having them directly inserted in the environment by your shell, in _.env_ files that your processes import when they start, or for added security, in a deployment platform that offers secret management, such as [Kubernetes](https://kubernetes.io/).

What does server hardening entail? Here are some ideas:

  * A firewall that blocks external access through all ports except the ones that are needed for operation (typically, port 22 for administration via SSH, and ports 80 and 443 for HTTP)
  * SSH access only via private key
  * No root account logins
  * Routine OS updates
  * Routine audits that ensure that applications running on the server are not vulnerable to web-based attacks such as [XSS](https://owasp.org/www-community/attacks/xss/) and [CSRF](https://owasp.org/www-community/attacks/csrf)
  * No development work ever performed on the server (to avoid the risk of installing compromised dependencies)



But of course, in many cases you cannot control the server on which your cloud processes run. GitHub Actions and other cloud process runners are a good example of this. These services run on large farms of servers that are assigned to processes on the fly, and they use environment variables as the main method to pass information, including secrets. These platforms are tricky because they have some features that while convenient, are insecure by design, and are often exploited by malware to access secrets.

I don't think there are any great methods to protect secrets in the cloud, sadly. Cloud runner platforms have a lot of complexity, which makes it hard to assess risk. I mentioned above when I was discussing trusted publishing the example of a well known Python package that was hacked through a vulnerability in their GitHub Actions configuration, and in that state it was able to engage with the PyPI trusted publishing APIs to legitimately publish several compromised releases.

My way to address this risk is to design my cloud processes so that they don't need secrets to run, as much as possible. I run continuous integration jobs for my open source projects in GitHub Actions, for example, but these do not need any secrets aside from the standard GitHub token provisioned by GitHub Actions and a [Codecov](https://about.codecov.io/) token to store code coverage stats for my tests.

The token that GitHub Actions provisions for jobs can be configured to use a set of [permissive or restrictive](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository?versionId=free-pro-team%40latest&productId=actions&restPage=tutorials%2Cauthenticate-with-github_token#setting-the-permissions-of-the-github_token-for-your-repository) permissions. For recent repositories the default is the restricted set, but I found I have a lot of older repositories created more than a year ago that are set to permissive, so my guess is that GitHub decided to change the default at some point. When I learned about this I made sure all my projects use the restrictive set of permissions, which give read-only access to the GitHub API. It is always important to give your tokens the least amount of permissions they need.

If you are working with GitHub Actions, you can also use [Zizmor](https://github.com/zizmorcore/zizmor) to check your action definitions for vulnerabilities. This is a very useful tool, but keep in mind that a clean bill of health from Zizmor only means that your actions do not have _known_ problems. It is quite possible that there are attack vectors that aren't known or disclosed yet, so Zizmor may not know about them.

## Conclusion

If you are going to remember one thing about this article, be it that if you aren't using a password manager yet, the right time to start is now. Get yourself a Bitwarden account or one from one of their competitors, and start migrating your secrets over to keep them safe. It is going to be tedious and awkward at first, but eventually you'll get used to it!

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through [Buy me a coffee](https://www.buymeacoffee.com/miguelgrinberg). Thanks!

[![Buy Me A Coffee](/static/buymeacoffee-yellow.png)](https://www.buymeacoffee.com/miguelgrinberg)

## Share this post

[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables&t=How%20to%20Securely%20Store%20Secrets%20in%20Environment%20Variables) [ Reddit ](https://reddit.com/submit/?url=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables&resubmit=true&title=How to Securely Store Secrets in Environment Variables) [ Twitter ](https://twitter.com/intent/tweet/?text=How%20to%20Securely%20Store%20Secrets%20in%20Environment%20Variables&url=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables&title=How%20to%20Securely%20Store%20Secrets%20in%20Environment%20Variables&summary=How%20to%20Securely%20Store%20Secrets%20in%20Environment%20Variables&source=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables) [ Facebook ](https://facebook.com/sharer/sharer.php?u=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables) [ E-Mail ](mailto:?subject=How%20to%20Securely%20Store%20Secrets%20in%20Environment%20Variables&body=https%3A//blog.miguelgrinberg.com/post/how-to-securely-store-secrets-in-environment-variables)

[2 comments](/post/how-to-securely-store-secrets-in-environment-variables#comments)

  * ![](https://gravatar.com/avatar/d8fe6bf5db82a3c9ce2da2c2a5083736?s=60&d=identicon)

#1 Madflier said 2025-12-17T08:24:00Z

My worry with this sort of (vastly superior to default!) setup is that the actual script is compromised and other credentials are requested from your bitwarden account, which you then unlock.

This is starting to move into the realm of targeted attacks of course.

But do you use an entirely separate "Dev only" bitwarden account? Or is this your main account containing also bank logins and email passwords / 2FA tokens etc? Can you flag only some of the bitwarden entries as accessible from the cli application?

I'm curious because, while a bitwarden user, I've never used it for this sort of function. It contains all the "keys to the kingdom" and I'm very wary about allowing scripted access, even if I'm needing to enter a key each time (which additionally adds the risk of my cli prompt being spoofed or hijacked to steal my bitwarden password).

I'm sure it's a great system, but I'm curious about how much potential attack surface you are exposing, even if well protected.

  * ![](https://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon)

#2 Miguel Grinberg said 2025-12-17T19:15:05Z

@Madflier: I have arrived to similar conclusions as you. This is great to defend against generic attacks of the sort we have been seeing lately, but if someone wanted to target myself specifically (or maybe the subset of users who work with the `bw` CLI program) then the risk is a tad higher, because then the attacks could target my own scripts, or even `bw`.

As far as I know the entire contents of the Bitwarden account are accessible from the CLI once you run the `unlock` command. I do not know if it is possible to create subsets of secrets that you can unlock independently, but in any case, I use a dedicated Bitwarden account to address this problem and keep different use cases completely separate.




  * [««](/post/how-to-securely-store-secrets-in-environment-variables/page/1#comments)
  * [«](/post/how-to-securely-store-secrets-in-environment-variables/page/0#comments)
  * [»](/post/how-to-securely-store-secrets-in-environment-variables/page/0#comments)
  * [»»](/post/how-to-securely-store-secrets-in-environment-variables/page/0#comments)



### Leave a Comment

Name

Email

Comment

Captcha

The React Mega-Tutorial

[ ![](/static/react-book-small.png) ](https://courses.miguelgrinberg.com/p/react-mega-tutorial)

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
