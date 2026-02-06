# Adding Mastodon Comments to your Blog

**来源:** https://beej.us
**链接:** http://beej.us/blog/data/mastodon-comments/
**日期:** Fri, 21 Feb 2025 00:00:00 +0000

---

# [Beej's Bit Bucket  â¡ Tech and Programming Fun ](../..)

2025-02-21

# Mastodon Comments

![Mastodon Logo](images/mastodon_logo_purple.svg) Comments powered by Mastodon!

I hate ads. I also hate tracking and bloat. But I didn't actually hate the latter quite enough to get rid of [Disqus](https://disqus.com/) for comments. It was a free, good service, and you could turn off ads for the users (which I did).

But recently they sent out a mail saying they were not longer offering a free ad-free option, and it's not worth paying for at my usage levels, so they got the boot.

What to replace them with? The ultimate would be some kind of home-grown thing, which I _could_ do with the hosting I have. But it's more than I want to take on right now.

So that leaves "Comments in Mastodon" as the winner. There's significant overlap between Mastodon users and my meager collection of blog readers, so that's not too bad.

The only thing that remains is either grabbing someone else's code to do the work, or doing it myself. Doing it myself is more fun. Let's figure it out!

I assumed correctly there was probably an API that would return JSON data for public comments, and it seems like it should do so without any login credentials.

First, get the JSON, then parse it down and convert it to HTML, then embed that in the page. And style it all with CSS.

Oh, and make it work with my custom static site generator.

> ![Hint Goat](../../common/images/goat50.png) Yes, this is going to be JavaScript-powered. I respect that some people don't support JS, but since Mastodon requires it, we're going to go with it. Also, it saves me from having a server-side component.
> 
> The only assurance I can give is that I don't use JS for tracking or ads. So you should go ahead and whitelist my site. ð

The basic idea is that we're going to:

  1. Write a blog entry.
  2. Post a link to that blog from our Mastodon account.
  3. Link the blog entry back to our Mastodon post.
  4. In the blog entry, show all the replies that have been made to that Mastodon post.



## Audience

This assumes you know some basic JavaScript/HTML/CSS, e.g. finding DOM elements, setting `innerHTML`, styling with CSS, using `<script>` tags, etc.

I'm going "high-level overview" here, not "complete source code".

## Getting the Post ID

When you make the announcement post to Mastodon, you need the ID of that post so you can refer to it from your blog page.

The easiest way to get this is to go to your post on Mastodon, and look at the URL.
    
    
    https://mastodon.sdf.org/@beejjorgensen/114011021587416866
    

That number at the end is your post ID. We'll need it for later.

## My Site Generator

I could go off on a tangent here talking about how I think everyone should write their own static site builder. Preferably in some POSIX-compliant shell like Bash or Zsh. Because it's super portable, fast as hell, already installed, and maximally removes dependencies.

But instead, I'll just cover the basics. This site is written in Markdown (I'm writing Markdown right now in this very sentence). And the site builder converts that to HTML, sticks some common headers and footers on there, and then, importantly, substitutes some text in the result with other values.

But that last bit is how we're going to make a static page aware of the Mastodon post ID we're going to be peeling comments off of.

For example, the post with the comments might have ID `114011021587416866`. Somehow I need to embed that inside the HTML for the page to be able to `fetch()` the data.

I do this by having a placeholder in the pre-built HTML that looks like this:
    
    
    MASTODON_POST_ID
    

Any place that string appears in the HTML, I replace it with `114011021587416866`. (Using [sed](https://en.wikipedia.org/wiki/Sed).)

And where do I get `114011021587416866`? It's in a file called `env.sh` in the directory for this particular blog entry.

It has content in it like this, setting shell environment variables:
    
    
    MASTODON_POST_ID=114011021587416866
    

I source this into the site builder shell script before the build starts so I can do the substitution.

If that environment variable isn't found, no comments section is emitted.

I use that ID a couple places in the code, so the site builder emits some HTML for "view" and "reply" buttons that look like this (wrapped for ease):
    
    
    <a id="comments-view"
        href="https://mastodon.sdf.org/@beejjorgensen/114011021587416866"
        data-comments-id="114011021587416866">View Comments</a>
    

Note the post ID in the `href`, but I've also added it to `data-comments-id`, which means I can get it in JavaScript like this, thanks to the whole [dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset) field:
    
    
    const a_elem = document.querySelector("#comments-view");
    const post_id = a_elem.dataset.commentsId;
    

However you do it, though, you somehow have to get the Mastodon post ID into the page.

## What's the API?

Now, on to business.

It's actually pretty simple to get a post and all its attached comments. You're going to want to do this for the server you have an account on, which in my case is `mastodon.sdf.org`. ([SDF](https://sdf.org/) is a venerable, classic public access Unix system.)

You just have to hit the API endpoint. Let's use the same post ID from the previous section in this example. Here is the URL to get the comments (with my example post ID):
    
    
    https://mastodon.sdf.org/api/v1/statuses/114011021587416866/context
    

That's it. You can [go hit it right now](https://mastodon.sdf.org/api/v1/statuses/114011021587416866/context) in your browser and see the JSON output.

And there's a _lot_ of it.

But for my bit, I only wanted a few pieces from the commenter so that I could use them to build the comment HTML.

  1. Their display name
  2. Their account name
  3. Their avatar URL
  4. Their profile URL
  5. Their content (what they posted)
  6. Their attachments (more on that later)
  7. Their comment Mastodon ID (for blacklist reasons)



If we look at the response we got, it has two keys: `ancestors` and `descendants`. The descendants are what we're interested in, i.e. all the comments made in reply to our post. And `descendants` is an array of all those comments.

Let's look at those elements and find what's interesting. Say `d = descendants[i]`. Then, searching through the JSON, we have:

Field | Description  
---|---  
`d.account.display_name` | Their display name  
`d.account.acct` | Their account name  
`d.account.avatar_static` | Their avatar URL  
`d.account.display_name` | Their profile URL  
`d.content` | Their content (what they posted)  
`d.media_attachments` | Their attachments (an array)  
`d.id` | Their comment Mastodon ID  
  
> ![Hint Goat](../../common/images/goat50.png) There's both `avatar` and `avatar_static` in the response. The former might be animated, and the latter is not. You could do something interesting here like switch to the animated one on mouse-over, but I didn't bother. I just always used the `_static` option for the various images.

So we have what we need, right there in each record.

## JavaScript at Last

All we need to do is `fetch()` that information with our Mastodon post ID that we baked into our static HTML. There are no credentials needed to access public posts (so be sure to make your Mastodon post public).

But when should we fetch? Should we do it on page load? When the element becomes visible? On a click?

If you have a high-traffic site, you might start raising the ire of your Mastodon server admins if you repeatedly hit that URL. My site is nowhere near those limits, so I _could_ just load the comments after my blog loads.

But I don't like extra overhead unless the user wants it, so instead I hooked it up to a link. The comments will only appear on the page if the user clicks the "View Comments" link.

A compromise might be to lazily load the comments when the user scrolls down enough for them to be visible. But I just went for manual. (I drive a [stick](https://en.wikipedia.org/wiki/Manual_transmission), too, BTW.)

In any case, we'll need a function to load the comments, and it'll look like this:
    
    
    async load_comments(ev) {
        const post_id = MASTODON_POST_ID;
    
        // Change the URL to your server
        const url = `https://mastodon.sdf.org/api/v1/statuses/${post_id}/context`
    
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
    
            const json = await response.json();
    
            populate_comments(json);
    
        } catch (error) {
            alert(`Error loading comments: ${error.message}`);
            console.error(error.message);
        }
    
    }
    

It's an async function that uses the `fetch()` API to get the data for my Mastodon post that corresponds to this blog entry.

Once it has loaded, we call `populate_comments()` with the JSON data to actually build out the HTML. Let's talk about that next.

## Building the HTML

This all depends on how you want your stuff to look at the end of the day.

I wanted something that looked like what we have at the bottom of this page, so I have some code that generates these. Here's what it looks like (obviously with values substituted in where appropriate):
    
    
    <div class="mast-comment">
        <div class="mast-comment-header">
            <div class="mast-comment-avatar">
                <a href="ACCOUNT_URL">
                    <img src="ACCOUNT_AVATAR_URL">
                </a>
            </div>
            <div class="mast-comment-ident">
                <div class="mast-comment-acct">
                    <a href="ACCOUNT_URL">
                        ACCOUNT_NAME
                    </a>
                </div>
                <div class="mast-comment-display-name">
                    <a href="ACCOUNT_URL">
                        ACCOUNT_DISPLAY_NAME
                    </a>
                </div>
            </div>
        </div>
        <div class="mast-comment-content">
            COMMENT_CONTENT
        </div>
        <!-- attachment HTML goes here -->
    </div>
    

Having it in that form allowed me to add some [flexbox CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) to lay out the whole thing.

I basically just appended a bunch of those to a string and then dumped it into the `innerHTML` of the comments block.

Note that the record `content` field is already HTML-encoded so there's no need to do that again. (And if you do, you'll lose the comment formatting and just display a bunch of HTML tags.)

## Media Attachments

This was interesting. Users can attach things to their posts. And then the question becomes what to do with them. The real Mastodon client will display previews of the attachments that you can click on to get the whole thing.

I'm going simpler with my stuff. Basically I'm just going to put a link with a text description. I don't want the comments to be too polluted with media.

We can find the media attachments in the `media_attachments` field, which, if present, is an array.

I just needed a few pieces of information from each `media_attachments` entry. Let's assume that `a = rec.media_attachments[i]`, and then we have:

Field | Description  
---|---  
`a.type` | The attachment type  
`a.url` | The attachment location  
`a.description` | The attachment text description  
  
The [spec says](https://docs.joinmastodon.org/entities/MediaAttachment/#type) the `type` can be a few things:

Type | Description  
---|---  
`unknown` | Unsupported or unrecognized file type  
`image` | Static image  
`gifv` | Looping, soundless animation  
`video` | Video clip  
`audio` | Audio track  
  
I used the `type` to choose an emoji icon that was appropriate (ð¼ï¸ ð¦ ð¶ ð), then used the `description` for the text underlying a link to the `url`. One per line. No preview. Kept it simple.

So I had `<div>` elements that I tucked into main comment `<div>` where the "attachment HTML goes here" comment was, above.
    
    
    <div class="mast-comment-attachment">
        ICON_EMOJI&nbsp;<a href="URL">DESCRIPTION</a>
    </div>
    

## Replying

100% punted on this. You click the "reply" button on my page and it takes you straight to my blog post announcement on Mastodon. If you want to reply, you need a Mastodon account and reply from there.

As such, the comments on my page are "read only". They are just a view onto the live comments that are on Mastodon.

## Blacklisting

I wanted to be able to blacklist entire accounts (`@user@example.com`) or individual comment IDs (the big number referencing that comment).

This wouldn't change what was actually on Mastodon, but it would filter out comments I didn't want to see on my blog site.

Remember how I jammed the Mastodon announcement post ID into my static HTML by putting it in the JavaScript variable `MASTODON_POST_ID`? Well, I do a similar thing for the blacklist.

In my environment shell script, I include a blacklist like this:
    
    
    MASTODON_BLACKLIST=@user@example.com,123456789,345678912
    

The numbers can be either a post ID or an account ID.

And my processing scripts turn that into JavaScript that looks like this:
    
    
    <script>MASTODON_BLACKLIST = new Set([
        "@user@example.com",
        "123456789",
        "345678912"
    ]);</script>
    

And then I can pass an entire `descendants` record into this function which will return `true` if it is blacklisted. It tests the comment record ID, the poster account ID, and the poster account login to see if any of them are in the blacklist. If so, no comment block is emitted for that record.
    
    
    function blacklisted(rec)
    {
        const bl = MASTODON_BLACKLIST;
    
        return bl.has(rec.id) ||
            bl.has(rec.account.id) ||
            bl.has(rec.account.acct);
    }
    

### Getting the Comment ID

If I see some offensive content, I can see who posted it because my comments viewer shows their name. But my comments viewer does not show their comment post ID.

And what if I want to block just that one post?

What I did was wire it up so that if I held `ALT` and clicked on the comment, it would display the comment ID underneath the comment. (And remove it if I clicked again.)

### Adding to the Blacklist

If I want to block someone, I do the following.

  1. If I want to block their account, I add their account login to my `MASTODON_BLACKLIST` environment variable. If I want to block just that comment, I `ALT`-click on it to get the ID, and then add that ID to the blacklist variable.
  2. I rebuild the site. It's static, so I need to get the new blacklist baked into the HTML. (I could also just rebuild this one page, but since it takes 0.5 seconds to rebuild the entire site currently, I just go for it.)
  3. I deploy the site.



### Global Blacklist

Right now I'm blacklisting people and comments on a per-blog-entry basis. But I'll probably modify my site builder to also support a global blacklist for people I want to ban on **all** my blog posts.

Hopefully I never have to do that.

## Chicken and Egg

I have to put the blog post online so I can link to it from the Mastodon announcement post.

I have to put the Mastodon announcement post online so I can refer to it from the blog post.

So there's just a moment where the comments don't show. Reviewing the launch process:

  1. Make the blog entry live with no comments.
  2. Link to it from Mastodon in the announcement post.
  3. Take the announcement post ID and use it to rebuild the blog entry.
  4. Re-deploy the blog entry.



Of course this could all be automated through the appropriate APIs to minimize that window, but I'm not going to bother for my low traffic.

## Maiden Voyage

This is the first post where I'm trying this out. So feel free to reply and I'll find out where all the breakages are. ð 

## Comments

[View Comments](https://mastodon.sdf.org/@beejjorgensen/114055638347066398) [Reply](https://mastodon.sdf.org/@beejjorgensen/114055638347066398)

Click on "View Comments" to see the comments.

[**Blog**](http://beej.us/blog/)  â¡  [**beej@beej.us**](mailto:beej@beej.us)  â¡  [**Home page**](http://beej.us/)
