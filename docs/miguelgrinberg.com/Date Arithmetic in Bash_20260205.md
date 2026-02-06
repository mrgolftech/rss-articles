# Date Arithmetic in Bash

**来源:** https://miguelgrinberg.com
**链接:** https://blog.miguelgrinberg.com/post/date-arithmetic-in-bash
**日期:** Wed, 04 Feb 2026 11:09:06 GMT

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



# [Date Arithmetic in Bash](/post/date-arithmetic-in-bash)

##  Posted by  on 2026-02-04T11:09:06Z under 

Date and time management libraries in many programming languages are famously bad. [Python's datetime module](https://dev.arie.bovenberg.net/blog/python-datetime-pitfalls/) comes to mind as one of the best (worst?) examples, and so does [JavaScript's Date class](https://fjolt.com/article/javascript-date-is-weird/). It feels like these libraries could not have been made worse on purpose, or so I thought until today, when I needed to implement some date calculations in a backup rotation script written in bash.

So, if you wanted to learn how to perform date and time arithmetic in your bash scripts, you've come to the right place. Just don't blame me for the nightmares.

## Why bash?

This is a valid question. Why bother doing this in bash when you can drop into Python or Node? In my particular case, I needed to expand a backup rotation script that I run in an old [NAS](https://en.wikipedia.org/wiki/Network-attached_storage) that I have here in my home. This device has been very reliable, but in terms of scripting options it is fairly limited, only offering SSH access, bash and a core set of UNIX commands. I could probably figure out how to cross-compile Python for it, but calculating dates directly in my existing bash script seemed like a more direct option, and a more interesting challenge as well.

## How to work with numbers in bash

Did you know that bash supports numbers? I didn't for many years, so assuming this may also be news to some of you, let's review how that works first.

### Evaluating numerical expressions

There are actually several ways to evaluate expressions in bash. The one I'm going to demonstrate here is my favorite, called [arithmetic expansion](https://www.gnu.org/software/bash/manual/html_node/Arithmetic-Expansion.html). If you put any expression between `$((` and `))`, then bash will treat it as numbers and will evaluate it:
    
    
    > echo $((2+3))
    5
    

You can use `+`, `-`, `*`, `/`, `%` (modulus) and `**` (exponentiation) as operators, and if you are interested in more, you can see [the complete list](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html) in the documentation.

An important limitation in bash is that only integers can be used. If you can use zsh instead of bash, then you can also work with decimal numbers.

### Variables

You can include variables inside the expressions:
    
    
    > A=10
    > B=$(($A * 100))
    > echo $B
    1000
    

Here you can see that bash does not treat numbers stored in variables in any special way. Conversions between string and numbers are done implicitly when needed. This can actually produce confusing results, as the next example demonstrates:
    
    
    > A=2+2
    > echo $(($A * 10))
    22
    

In this example you probably expected the result would be 40, but the value of `$A` is replaced literally in the expression, so bash sees `2+2 * 10`, which evaluates to 22 when using standard operator precedence rules. To do this correctly, you have to remember to evaluate all intermediate expressions with `$(( ... ))`:
    
    
    > A=$((2+2))
    > echo $(($A * 10))
    40
    

### Looping over sequences of numbers

Another very useful thing you can do is looping over a range of numbers. For this I like to use the `seq` command, which is technically not internal to bash, but it should be available in all UNIX distributions:
    
    
    > for INDEX in $(seq 1 10); do echo $INDEX; done
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

As you probably figured out already, the `seq` command takes the start and end numbers, and generates all the numbers in between, including those two. Another form of `seq` uses three arguments, where the middle one is interpreted as the increment. The next example shows a loop that counts from 1 to 10 by 3:
    
    
    > for INDEX in $(seq 1 3 10); do echo $INDEX; done
    1
    4
    7
    10
    

I hope these examples give you an idea that working with numbers in bash is not only possible, but quite reasonable. Refer to the bash documentation and your friendly search engine if you want to learn other math tricks.

## The date command

Similarly to `seq`, UNIX systems include a utility called `date` to work with dates and times. Note that you may have seen this command used to change the computer's clock. This is just one of its functions. In this article I'm not going to change the clock, I'm only going to use `date` to format dates and do math with them.

Something important I should warn you about is that there are two versions of the `date` command. If you use a Linux distribution, then you have [GNU date](https://www.man7.org/linux/man-pages/man1/date.1.html). But if you use a BSD-derived operating system, including macOS, then you have [BSD date](https://man.freebsd.org/cgi/man.cgi?date). These two commands have some similarities, but in terms of date math they are incompatible with each other. This article uses the GNU flavor that is common on Linux. If you have the BSD date, you can install the [coreutils](https://www.gnu.org/software/coreutils/coreutils.html) package (`brew install coreutils` on your Mac), and then you can access GNU date with the name `gdate`.

### Printing dates

In its simplest form, the `date` command can be used to show the current time:
    
    
    > date
    Tue 03 Feb 2026 07:50:27 PM GMT
    

The default format in which the date is printed is not very useful if you want to use the date in a script. To change the format, you can add an argument beginning with `+`, followed by a template that describes the format you want the date to be printed in. Below is a simple example:
    
    
    > date +%Y-%m-%d
    2026-02-03
    

When working inside scripts, it is likely you will need to store the date in a variable:
    
    
    > TODAY=$(date +%Y-%m-%d)
    

It is also possible to include the time. In the following example I use a template that produces the [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format in the UTC timezone:
    
    
    > NOWUTC=$(date --utc +%Y-%m-%dT%H:%M:%SZ)
    > echo $NOWUTC
    2026-02-03T19:59:18Z
    

If you prefer to work in your local timezone, you can remove the `--utc` option and change the `Z` at the end to your timezone.

The `%Y`, `%m`, `%d`, `%H`, `%M` and `%S` are the most commonly used placeholders, but there are many more. Review the [man page for date](https://www.man7.org/linux/man-pages/man1/date.1.html) to learn about them.

### Choosing what date to print

So far all the examples printed the current date and time, which can be useful, although many times you'll want to work with other dates. You can give the `date` command a date to use instead of the current one with the `-d` option. In the next example I pass the `$NOWUTC` variable that I created above to see it printed in the default format:
    
    
    > date -d $NOWUTC
    Tue 03 Feb 2026 07:59:18 PM GMT
    

And of course, you can combine the `-d` option with the `+` custom formats to print a custom date using a custom format. The next example prints the day of the week of the date stored in the `$NOWUTC` variable:
    
    
    > date -d $NOWUTC +%A
    Tuesday
    

While the `%A` placeholder is useful to get the day of the week for printing it, when scripting it is more useful to get a numeric value, which you can get with `%w`:
    
    
    > date -d $NOWUTC +%w
    2
    

The value of `%w` goes from 0 to 6, with 0 meaning Sunday. I'll show you an example when this can be useful in a little bit.

### Moving through the calendar

In the previous section I only showed you the most basic possibilities with the `-d` option. But this option can also be used to navigate from one date to another in relative terms. The next examples show how to print some dates relative to today: 
    
    
    > date -d "-1 day" +%Y-%m-%d
    2026-02-02
    > date -d "-2 weeks" +%Y-%m-%d
    2026-01-20
    > date -d "-3 months" +%Y-%m-%d
    2025-11-03
    

You can also go forward using a positive distance with a `+` sign. And you can also use a custom starting date:
    
    
    > date -d "2025-01-01 +1 day" +%Y-%m-%d
    2025-01-02
    > date -d "2025-01-01 +2 weeks" +%Y-%m-%d
    2025-01-15
    > date -d "2025-01-01 +3 months" +%Y-%m-%d
    2025-04-01
    

You can combine several adjustments. Here is how you can calculate a week from tomorrow:
    
    
    > date -d "+1 day +1 week" +%Y-%m-%d
    2026-02-11
    

And this also works with time units. The next example prints the ISO8601 formatted time of 2 days, three hours and 27 minutes ago:
    
    
    > date --utc -d "-2 days -3 hours -27 minutes" +%Y-%m-%dT%H:%M:%SZ
    2026-02-01T19:05:46Z
    

Finally, you can store the results of these calculations instead of printing them:
    
    
    > YESTERDAY=$(date -d "-1 day" +%Y-%m-%d)
    > echo $YESTERDAY
    2026-02-02
    

### Advanced tricks

Hopefully you can now picture how you would go about calculating dates in bash, but so far we haven't connected the regular numerical features with the date manipulation options, and this is what brings the most interesting possibilities.

Let's say you need to repeat some task over the last 7 days. You can do this with a loop as follows:
    
    
    > for INDEX in $(seq -6 0); do
          DATE=$(date -d "-$INDEX days" +%Y-%m-%d);
          echo do something with $DATE
      done
    do something with 2026-01-28
    do something with 2026-01-29
    do something with 2026-01-30
    do something with 2026-01-31
    do something with 2026-02-01
    do something with 2026-02-02
    do something with 2026-02-03
    

In this example you can see that you can also substitute parts of the date manipulation options passed to the `-d` option with variables, for complete flexibility.

Another common need is to calculate a time difference. The next example is a bash function that calculates the number of days, hours, minutes and seconds between two timestamps:
    
    
    time_between() {
        START_SECS=$(date -d $1 +%s)
        END_SECS=$(date -d $2 +%s)
        DIFF_SECS=$(($END_SECS - $START_SECS))
        SECS=$(($DIFF_SECS % 60))
        MINS=$(($DIFF_SECS / 60 % 60))
        HOURS=$((DIFF_SECS / 3600 % 24))
        DAYS=$((DIFF_SECS / 86400))
        echo ${DAYS}d ${HOURS}h ${MINS}m ${SECS}s
    }
    

Here are two example calls to this function:
    
    
    # time between 20:30 and 23:00
    > time_between "2026-01-01T20:30:00Z" "2026-01-01T23:00:00Z"
    0d 2h 30m 0s
    
    # time between the Apolo 11 lunar landing and my current time
    > time_between "1969-07-20T20:17:00Z" $(date --utc +%Y-%m-%dT%H:%M:%SZ)
    20652d 2h 55m 49s
    

Pretty cool, don't you think? Note how for the second example I'm using `date` to generate the second argument to the `time_between` function, which in turn feeds it back into `date` in the `-d` option.

As I mentioned at the start of the article, this whole ordeal started when I needed to implement date arithmetic in a backup rotation script that I use. One of the features I wanted to add is the ability to preserve one backup per week for a given number of weeks starting from a given date. This ended up being very tricky, because I needed to know when a week started and ended, so that I could then search for the last backup made during that week to save.

To find the start of a week, I used the `%w` placeholder I mentioned earlier, but again in a sort of recursive way, where the output of the `date` command is fed into a second invocation of `date`. The following example shows how to get the date of the Sunday of the current week:
    
    
    > WEEKDAY=$(date +%w)
    > SUNDAY=$(date -d "-$WEEKDAY days" +%Y-%m-%d)
    > echo $SUNDAY
    2026-02-01
    

How does this work? I first get the day of the week number, which is an integer between 0 and 6. Then I subtract that number of days from the current date. If I'm on a Sunday, then I would be subtracting 0 days, so I'm still on Sunday. If I'm on a Tuesday, then `$WEEKDAY` would be 2, so subtracting 2 days from the current date also gives me the Sunday that started the week.

Because I like to live on the edge, I ended up implementing this algorithm all in a single line, avoiding the need to have a `$WEEKDAY` auxiliary variable:
    
    
    > SUNDAY=$(date -d "-$(date +%w) days" +%Y-%m-%d)
    > echo $SUNDAY
    2026-02-01
    

Knowing the date of the start of the current week, I can create a loop that goes backwards a specified number of weeks:
    
    
    > NUM_WEEKS=3
    > SUNDAY=$(date -d "-$(date +%w) days" +%Y-%m-%d)
    > for INDEX in $(seq 0 -1 -$(($NUM_WEEKS - 1))); do
        START=$(date -d "$SUNDAY -$INDEX weeks" +%Y-%m-%d)
        echo week from $START
      done
    week from 2026-02-01
    week from 2026-01-25
    week from 2026-01-18
    

This example incorporates pretty much all the techniques that I presented above, so I hope after reading it carefully you will understand it. I used this as a start to build my weekly backup scanning logic, but my actual solution ended up being much uglier than this because I had to add an inner loop to go from `$START +6 days` to `$START` searching for the backups I had for that week in descending order, so that I could save the most recent one (the first that I would find) and delete the rest.

I expect in a few months or years when I come up with another improvement idea for my backup rotation script I will find this article very useful as a reminder of what I did. If it also gives you some ideas for your own scripting projects, then great! If you make something cool with these concepts, please drop me a note below in the comments.

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through [Buy me a coffee](https://www.buymeacoffee.com/miguelgrinberg). Thanks!

[![Buy Me A Coffee](/static/buymeacoffee-yellow.png)](https://www.buymeacoffee.com/miguelgrinberg)

## Share this post

[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash&t=Date%20Arithmetic%20in%20Bash) [ Reddit ](https://reddit.com/submit/?url=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash&resubmit=true&title=Date Arithmetic in Bash) [ Twitter ](https://twitter.com/intent/tweet/?text=Date%20Arithmetic%20in%20Bash&url=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash&title=Date%20Arithmetic%20in%20Bash&summary=Date%20Arithmetic%20in%20Bash&source=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash) [ Facebook ](https://facebook.com/sharer/sharer.php?u=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash) [ E-Mail ](mailto:?subject=Date%20Arithmetic%20in%20Bash&body=https%3A//blog.miguelgrinberg.com/post/date-arithmetic-in-bash)

[No comments yet](/post/date-arithmetic-in-bash#comments)

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
