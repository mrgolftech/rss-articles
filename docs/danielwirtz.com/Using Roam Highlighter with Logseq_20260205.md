# Using Roam Highlighter with Logseq

**来源:** https://danielwirtz.com
**链接:** https://danielwirtz.com/blog/logseq-web-highlighter
**日期:** Tue, 12 Oct 2021 20:33:00 GMT

---

DW

BlogAboutLists

Books

Bookmarks

Tools

# Using Roam Highlighter with Logseq

Daniel Wirtz

4 years ago • 

Copy link

Status

Slug

Desciption

Featured

Cover Video

Cover Image

Social Image

Publish date

Last edited time

Created time

URL

![notion image](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fc60cb9d6-ff5a-4eb2-823a-c07963f46657%2Fccf338fe-7a06-47da-8c34-733eb55a687c%2FFyDijxmJ57boxW52R35pDqTuY6pTaLrFxg73sv8rK3A.png%3FspaceId%3Dc60cb9d6-ff5a-4eb2-823a-c07963f46657?table=block&id=bcfc96c9-6fc7-471d-a4fd-36b9ac83214d&cache=v2)

I've recently started playing around with [Logseq](https://markdownlivepreview.com/logseq.com/) as my main note-taking app. And I was positively surprised to see how much progress they made in the last year. The app become way more stable and features are almost on par with [Roam Research](https://roamresearch.com/). On top of that, they also introduced things like [Youtube Timestamp](https://logseq.github.io/#/page/Youtube%20timestamp) , [PDF Highlights](https://logseq.github.io/#/page/pdf%20highlights) , [Plugins](https://logseq.github.io/#/page/plugins%20101). Just to name a few.

As I'm using Logseq now on daily basis, it made sense to see how well my [Roam Highlighter](https://chrome.google.com/webstore/detail/roam-highlighter/hponfflfgcjikmehlcdcnpapicnljkkc) for Chrome integrates with the app. And it turned out, that Logseq works great with the Roam Highlighter and that I didn't have to do any changes to the code. (yeahy!) So in this article, I want to give you a quick guide on how to best use the Roam Highlighter, while taking advantage of Logseqs features.

### 

Step 1: Install the Highlighter

Simply follow [this link](https://chrome.google.com/webstore/detail/roam-highlighter/hponfflfgcjikmehlcdcnpapicnljkkc) to install the Roam Highlighter from the Chrome Web Store. After the installation, you should be prompted with a short tutorial page where can make yourself familiar with the features of the highlighter.

### 

Step 2: Adjust the template

Open the widget by clicking on the icon in the toolbar. Once the widget is open, progress further to the settings by clicking the small settings icon in the bottom of the widget.

![notion image](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fc60cb9d6-ff5a-4eb2-823a-c07963f46657%2F7df401af-17a7-4489-b6d8-5482fc03a83e%2FbsQStoBlS-S-OaxdbtLYUnual3JhwXyxqefUfbx3j-c.png%3FspaceId%3Dc60cb9d6-ff5a-4eb2-823a-c07963f46657?table=block&id=b9be7025-85e6-4144-8c4d-8775a842637f&cache=v2)

Now you should be able to customize the format in which your bookmark and the highlights are copied to your clipboard. Here are some recommendations for a format that works great with Logseq:

  * Wrap the placeholder for the page title ( `$TITLE` ) in double brackets to backlink it automatically


  * Use the [properties feature](https://logseq.github.io/#/page/term/properties) to add metadata to your highlights


  * Use the "tag::" property in combination with the tag placeholder ( `$TAGS` )



Especially the last one is super cool, because everything that comes behind the tag property will automatically be linked by Logseq. This means that you can use the tag input field in the highlighter to quickly link related topics to your highlights. You can read more about that behavior [here](https://logseq.github.io/#/page/term/properties?anchor=ls-block-616448ab-7f24-4abf-bf54-e48fb82aad2b).

You can also find the format that I'm using below in the code box. Somehow I had to add an empty line above my properties to make them format correctly in Logseq.
    
    
    [[$TITLE]]
    
     - tags:: Article, $TAGS
    
       source:: [$TITLE]($URL)
    
     - Highlights
    
           $HIGHLIGHTS

### 

Step 3: Highlight and import to Logseq

Now everything is ready to go! Navigate to a page where you can try out the highlighter and click the icon to activate the widget. Once you made some highlights, copy them, open Logseq and paste the copied and formatted highlights into Logseq.

Something else that I found here is to use the [block to page](https://github.com/hyrijk/logseq-plugin-block-to-page) plugin to quickly turn the highlights into a page. Or you just park them in your daily notes.

_PS: I 'm working on a new version of the highlighter called _ _[Markway](https://markway.io/)_ _._

Subscribe to my blog

Helpful tools, thoughtful articles and other findings from the web. From my desk to yours.

Subscribe

Subscribe

Blog

Menu

Dark Mode

Contact

[](https://twitter.com/wirtzdan/)[](https://www.linkedin.com/in/wirtzdan/)[](https://github.com/wirtzdan)[](https://www.youtube.com/channel/UCje_bQMr6F45x0Auii7IOvA)

Privacy
