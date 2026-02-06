# How to Add a Quick Interactive Map to your Website

**来源:** https://miguelgrinberg.com
**链接:** https://blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website
**日期:** Thu, 29 Jan 2026 12:25:14 GMT

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



# [How to Add a Quick Interactive Map to your Website](/post/how-to-add-a-quick-interactive-map-to-your-website)

##  Posted by  on 2026-01-29T12:25:14Z under 

In this article I want to share a technique that I recently learned to display an interactive map on a website. For this, you will need just a few lines of HTML and JavaScript. This solution does not require you to sign up for any accounts or services anywhere, it is completely free and open source, and can be integrated with any front or back end web framework.

Give the demo below a try and if you like it, then keep on reading to learn how you can add a map like this one to your website in just 3 quick steps!

## Add a map to your website in 3 steps

Okay, if you made it this far then I assume you want to get a map up and running on your site as quickly as possible. I will split the task into three steps.

### Step 1: Add the CSS and JavaScript dependencies

To display a map we are going to use [Leaflet](https://leafletjs.com/), an open source project that can render maps on desktop and mobile browsers.

First, add the CSS for this project In the `<head>` section of your page:
    
    
    <head>
      ...
      <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
        integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
        crossorigin=""/>
    </head>
    

Next add the JavaScript library. I like to add JavaScript dependencies at the bottom of the `<body>` section of the page. If you prefer to add it in the `<head>` section, that works too.
    
    
    <body>
      ...
      <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
        crossorigin=""></script>
    </body>
    

Note that I'm using version 1.9.4 of Leaflet, downloaded from the `unpkg` CDN. The 1.9.4 version is the latest at the time I'm writing this article. You may want to check Leaftlet's [download page](https://leafletjs.com/download.html) to see if there is a newer version that you can use instead.

### Step 2: Add a map element to your page

Now you need to add an element to your web page where the map should appear. This can be just a `<div>` element with an `id` that you can later use to reference it from JavaScript. Put this element in the place within the page where you want the map to appear, and give it the desired dimensions. Here is an example:
    
    
    <body>
      ...
      <div id="myMap" style="width: 100%; height: 450px;"></div>
      ...
    </body>
    

In this example I'm giving my map full width, and a height of 450 pixels. You can change these dimensions, and also if you prefer, you can move the style declarations with your other CSS definitions.

### Step 3: Add the JavaScript logic to your page

The last step is to add the JavaScript code that renders the map. This is going to be another `<script>` tag, which you should add right after the `<script>` tag that you added in step 1, usually as the very last element before the closing `</body>` tag.
    
    
    <body>
      ...
      <script>
      function showMap(id, lat, long, label) {
        const mapLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        });
        const satLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
          maxZoom: 19,
          attribution: '&copy; <a href="https://esri.com">ESRI</a>'
        });
        const map = L.map(id, {
          layers: [mapLayer],
          center: [lat, long],
          zoom: 14,
          scrollWheelZoom: false,
        });
        const markerLayer = L.marker([lat, long]).addTo(map).bindPopup(label);
        L.control.layers({Map: mapLayer, Satellite: satLayer}, {Markers: markerLayer}).addTo(map);
      }
      document.addEventListener("DOMContentLoaded", (event) => {
        showMap('myMap', 53.342686, -6.267118, 'Dublin Castle');
      });
      </script>
    </body>
    

This block of JavaScript defines the `showMap()` function, which takes four arguments: the `id` of the element on which the map is to be rendered, the latitude and longitude that will be at the center of the map, and a label to use for a marker that will mark this center position. You can see the call to `showMap()` near the bottom of the code block.

The `showMap()` function creates a simple map configuration with two map layers and one marker layer. The `mapLayer` variable holds the standard map layer, which is sourced from [OpenStreetMap](https://www.openstreetmap.org), an open and free provider of map imagery.

The `satLayer` variable holds the layer with satellite imagery, which is provided by [ESRI](https://www.esri.com) as part of their [ArcGIS Online](https://www.esri.com/en-us/arcgis/products/arcgis-online/overview) product. My understanding is that this [specific map](https://www.arcgis.com/home/item.html?id=974d45be315c4c87b2ac32be59af9a0b) is available for public use, but I suggest you reach out to ESRI if in doubt.

The `map` variable holds the map instance, which is created with the OpenStreetMap layer as the only active layer. The `center` and `zoom` options configure the initial view of the map. Feel free to play with different values for the zoom setting to find the value that looks the best for your map. There are a lot more [configuration options](https://leafletjs.com/reference.html#map-option) that can be passed here to control the behavior of the map. For this example I have chosen to disable zoom with the mouse scroll wheel, because that interferes with the scrolling of the article.

The `markerLayer` variable is initialized with a marker that points to the place at the center of the map. This marker is also given a popup bubble with a label, which appears when the marker is clicked.

Finally, a layer selection widget is added in the top right corner of the map. This is how you can switch between the street and satellite maps, and also how you can enable or disable the marker. The `L.control.layers()` method accepts two arguments. The first argument is an object with the mutually exclusive layers that can be chosen, which appear with radio buttons. The second argument is another object with the overlay layers, which can be turned on and off on top of the selected map layer.

And that's pretty much it! The call to `showMap()` is made inside an event handler for the `DOMContentLoaded` event, so that it happens after the page is ready to be displayed by the browser.

### Bonus step: How to find map coordinates for any place of interest

I'm sure you will want to reconfigure the map so that it points to a location you find interesting. If you know the map coordinates of the location in question, then great, just plug those numbers in the `showMap()` call and you are done.

But what if you don't know what the coordinates are for the place you want the map to be centered on? In that case, here is a simple trick you can use to find them:

  * Open [Google Maps](https://maps.google.com) and search the location you are interested in.
  * Right click on the exact place you want your map to be centered on.
  * A context menu will appear, with the latitude and longitude of the point you clicked as a first menu option. Select that menu option to copy the coordinates to the clipboard.



## Conclusion

I hope you have found this quick article useful. If you want to dig deeper into creating maps with Leaflet, I recommend that you check out their [documentation](https://leafletjs.com/reference.html) to learn about all the different kinds of layers you can add to your map and many other cool options the library offers.

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through [Buy me a coffee](https://www.buymeacoffee.com/miguelgrinberg). Thanks!

[![Buy Me A Coffee](/static/buymeacoffee-yellow.png)](https://www.buymeacoffee.com/miguelgrinberg)

## Share this post

[ Hacker News ](https://news.ycombinator.com/submitlink?u=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website&t=How%20to%20Add%20a%20Quick%20Interactive%20Map%20to%20your%20Website) [ Reddit ](https://reddit.com/submit/?url=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website&resubmit=true&title=How to Add a Quick Interactive Map to your Website) [ Twitter ](https://twitter.com/intent/tweet/?text=How%20to%20Add%20a%20Quick%20Interactive%20Map%20to%20your%20Website&url=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website&title=How%20to%20Add%20a%20Quick%20Interactive%20Map%20to%20your%20Website&summary=How%20to%20Add%20a%20Quick%20Interactive%20Map%20to%20your%20Website&source=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website) [ Facebook ](https://facebook.com/sharer/sharer.php?u=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website) [ E-Mail ](mailto:?subject=How%20to%20Add%20a%20Quick%20Interactive%20Map%20to%20your%20Website&body=https%3A//blog.miguelgrinberg.com/post/how-to-add-a-quick-interactive-map-to-your-website)

[1 comment](/post/how-to-add-a-quick-interactive-map-to-your-website#comments)

  * ![](https://gravatar.com/avatar/9048e60d86f2d1711cbb217986cec6bf?s=60&d=identicon)

#1 Guillermo said 2026-02-01T22:31:11Z

Leaflet is excellent, and not only when you don't want or can't go the Google Maps path. I used it in a Flask app where I needed to display a map of the city with dynamic markers, just to try it out. It worked out so well that I ended up using some plugins, for displaying a heat map and for area selection using a polygon. The possibilities seem endless. Thanks for the write-up on this great resource.




  * [««](/post/how-to-add-a-quick-interactive-map-to-your-website/page/1#comments)
  * [«](/post/how-to-add-a-quick-interactive-map-to-your-website/page/0#comments)
  * [»](/post/how-to-add-a-quick-interactive-map-to-your-website/page/0#comments)
  * [»»](/post/how-to-add-a-quick-interactive-map-to-your-website/page/0#comments)



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
