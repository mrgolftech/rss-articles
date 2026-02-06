# You gotta think outside the hypercube

**来源:** https://lcamtuf.substack.com
**链接:** https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube
**日期:** Mon, 26 Jan 2026 23:05:38 GMT

---

[![lcamtuf’s thing](https://substackcdn.com/image/fetch/$s_!WvGP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F57b73d90-d717-4de9-bfb7-30a0f2913607_400x400.png)](/)

# [lcamtuf’s thing](/)

SubscribeSign in

# You gotta think outside the hypercube

### A closer look at the tesseract and the ways we can render it on the screen.

Jan 26, 2026

21

4

1

Share

If you’re a nerd, you probably have encountered visualizations of a _tesseract:_ a four-dimensional equivalent of a cube. Heck, various representations of the shape have made it into blockbuster sci-fi films, music videos, and more.

What might be harder to grasp is what these images mean or how they’re generated. You can find a handful of tesseract rendering demos on GitHub, but they all take different approaches, produce different results, and don’t really explain what’s going on.

In this article, we’ll take a look at the hypercube from first principles — and then, figure out how to map this beast to a computer screen.

### It’s hip to be square

To build a mathematical model of the hypercube, let’s start with a square. If we get it right, our approach will generalize to three dimensions and produce a cube; if it does, it ought to extend to the hyperspace too.

More specifically, we’ll try to model the _edges_ of a square — i.e., the line segments that connect the vertices in the four corners. For our purposes, a see-through wireframe model will work better than a solid.

For a 2D square with dimensions _a×a_ , the horizontal edges can be described as a collection of points that satisfy two criteria:

\\(\begin{array}{c} |x| \leq a \\\ |y| = a \end{array}\\)

In essence, we’re saying that we want to include points for which the _y_ coordinate is equal to either _-a_(the lower edge) or _+a_ (the upper edge); and where the _x_ coordinate spans anywhere between _-a_ and _+a_ :

[![](https://substackcdn.com/image/fetch/$s_!alK2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb299481-ef67-4d13-baca-b0344fd8ce57_2000x1111.jpeg)](https://substackcdn.com/image/fetch/$s_!alK2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb299481-ef67-4d13-baca-b0344fd8ce57_2000x1111.jpeg)_One half of a square._

To construct the remaining vertical edges, we can just flip the criteria around, constraining _x_ to one of two values and allowing _y_ to span a range. This nets us the following combined formula:

\\(\begin{array}{r l} \textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a \\\ \textrm{Vertical lines: } & |x| = a, \quad |y| \leq a \\\ \end{array}\\)

The method is easy to generalize to a cube. We start by constructing a rectangle in the _x-y_ plane using the earlier approach, except we add a third modulo constraint so that we end up with two images at the _-a_ and _+a_ offsets in the _z_ axis:

\\(\begin{array}{r l} \textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \\\ \textrm{Vertical lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \\\ \end{array}\\)

What’s still missing are four edges oriented in the _z_ direction that connect the corresponding corners of the two squares. We can add this with a third rule:

\\(\begin{array}{r l} \textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \\\ \textrm{Vertical lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \\\ z \textrm{ lines: } & |x| = a, \quad |y| = a, \quad |z| \leq a \\\ \end{array}\\)

Note that each of these rules produces four line segments because there 22 possible combinations for the coordinates constrained by the equality relationship. For example, for horizontal lines, we can have the following pairs of _y_ and _z_ values: (_-a, -a)_ , (_-a, +a)_ , (_+a, -a)_ , and (_+a, +a)_.

From here, the extension to the fourth dimension should be clear. I’m going to sensibly label the dimension 🌀; with this done, we just add a fourth constraint to each of the existing 3D rules and then add connecting segments in the fourth dimension:

\\(\begin{array}{r l} x \textrm{ lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \quad |🌀| = a \\\ y \textrm{ lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \quad |🌀| = a \\\ z \textrm{ lines: } & |x| = a, \quad |y| = a, \quad |z| \leq a \quad |🌀| = a \\\ \textrm{🌀 lines: } & |x| = a, \quad |y| = a, \quad |z| = a \quad |🌀| \leq a \end{array}\\)

This time around, each rule nets us 23 = 8 line segments, so the tesseract has 4·8 = 32 edges. These edges connect 16 vertices.

### Defining rotations

Most visualization of the tesseract spin the figure around. This allows the shape to be examined from different angles and makes for some mind-bending visuals. But what does it mean to rotate an object in 4D?

In a two-dimensional space, there’s only one type of rotation; it transposes coordinates in the XY plane. The following demonstrates the effect of rotating a point originally placed on the _x_ axis around the center of the coordinate system:

[![](https://substackcdn.com/image/fetch/$s_!TRvf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5086b2ef-7009-4fdd-a620-da86a71bfac1_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!TRvf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5086b2ef-7009-4fdd-a620-da86a71bfac1_2000x1300.jpeg)_The trigonometric solution to the simplest case of XY rotation._

From basic trigonometry, the new _x_ coordinate of the rotated point is the adjacent of a right triangle with an angle _α_ and a hypotenuse of _x orig_. The new _y_ is the opposite of that same triangle. If we want to start with a non-zero _y_ coordinate for the point, we need add a small tweak:

\\(\begin{array}{c} x_{new} = x_{orig} \cdot cos(\alpha) - y_{orig} \cdot sin(\alpha) \\\ y_{new} = y_{orig} \cdot cos(\alpha) + x_{orig} \cdot sin(\alpha) \end{array}\\)

In three dimensions, we have a lot more freedom. We can obviously spin things around in the XY plane (around the _z_ axis), XZ (around _y_), or in YZ (around _x_). It is also possible to dream up more complex rotations that touch all three coordinates at once, but they don’t add much value. They can be deconstructed into a sequence of planar rotations in XY, XZ, and YZ.

Given this observation, in four dimensions, we should probably still stick to the primitive of planar rotations that modify just two axes at a time. The only difference is that we get additional X🌀, Y🌀, and Z🌀 planes to use.

For ease of viewing and for consistency with 3D models, we’ll focus on spinning things in the XZ plane — a “turntable” animation:

\\(\begin{array}{c} x_{new} = x_{orig} \cdot cos(\alpha) + z_{orig} \cdot sin(\alpha) \\\ z_{new} = z_{orig} \cdot cos(\alpha) - x_{orig} \cdot sin(\alpha) \end{array}\\)

That said, we’ll also pay a brief visit the Z🌀 rotation plane. It plays by similar rules:

\\(\begin{array}{c} z_{new} = z_{orig} \cdot cos(\alpha) - 🌀_{orig} \cdot sin(\alpha) \\\ 🌀_{new} = 🌀_{orig} \cdot cos(\alpha) + z_{orig} \cdot sin(\alpha) \end{array}\\)

### Projecting 4D to 2D

Our next challenge is figuring out how to project four-dimensional coordinates onto a two-dimensional drawing surface, such as a computer screen.

In standard geometries, Cartesian axes are orthogonal to each other — that is, there is a 90° rotation that can take you between any two dimensions. On a two-dimensional surface, we can only pull this off with two axes; that said, there are several imperfect ways to make do.

#### Cavalier projection

If we were to ask a random person to come up with a 3D-to-2D projection on the spot, they would probably suggest drawing the _z_ axis as a diagonal line on a 2D plane, as shown below:

[![](https://substackcdn.com/image/fetch/$s_!9iRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde4d7fcc-2d16-4081-83d4-bd779a54a9f1_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!9iRJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde4d7fcc-2d16-4081-83d4-bd779a54a9f1_2000x1300.jpeg)_The cavalier projection._

To convert the model-space _z_ value to screen coordinates, we can use trigonometry to project the component onto the real _x_ and _y_ axes:

\\(\begin{array}{c} x_{screen} = x_{model} + z_{model} \cdot cos(45^\circ) \\\ y_{screen} = y_{model} + z_{model} \cdot sin(45^\circ) \end{array}\\)

Alas, if you attempt this projection with a regular three-dimensional cube, you will immediately notice that it looks off:

[![](https://substackcdn.com/image/fetch/$s_!rzAm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F876874d9-f4be-43e2-b5f4-7b92f47c83be_1080x1080.png)](https://substackcdn.com/image/fetch/$s_!rzAm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F876874d9-f4be-43e2-b5f4-7b92f47c83be_1080x1080.png)_The problem with cavalier._

The viewer-facing edges in the XY plane are exactly the same length as the _z_ edge; nevertheless, it’s hard to shake the impression that the dimensions are off and the cube is stretched.

#### Cabinet projection

To address this issue, we need to shorten the projected _z_ -axis edges, crudely approximating the length contraction that we expect in real life. To do this, we divide the _z_ component by an ad hoc scaling factor, typically 2:

\\(\begin{array}{c} x_{screen} = x_{model} + z_{model} \cdot \frac{cos(45^\circ)}{2} \\\ y_{screen} = y_{model} + z_{model} \cdot \frac{sin(45^\circ)}{2} \end{array}\\)

The cabinet projection is ubiquitous in informal sketches and technical drawings, and it does look good at first blush. That said, consider the following video of a cube that is rotated in the XZ plane:

Note that the shape looks OK at first, but then gets weirdly squished near the rotation angle of 70°; this is because the projection gives us incorrect visual cues that the shape is facing us — the back edges are tucked squarely behind while in reality, the shape is still at an angle in relation to the viewer.

The root of the problem is that the axes are not oriented in a way that would be possible in real life. If we constructed a model of 3D axes out of sticks, the only way for the _z_ axis to appear at a 45° angle — or indeed, to be visible at all — is if at least one of the other axes is not parallel to the camera plane _:_

[![](https://substackcdn.com/image/fetch/$s_!uwHh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F026f5fbe-cbcd-424c-a6e6-4cc9a1e50239_2000x1281.jpeg)](https://substackcdn.com/image/fetch/$s_!uwHh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F026f5fbe-cbcd-424c-a6e6-4cc9a1e50239_2000x1281.jpeg)_An issue with the cabinet projection._

#### Isometric projection

This brings us to the isometric projection — a physically-plausible arrangement that places the model axes 60° apart:

[![](https://substackcdn.com/image/fetch/$s_!tEXA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19fdb5e5-3e55-438f-8ba8-e56998cad6ba_2000x1264.jpeg)](https://substackcdn.com/image/fetch/$s_!tEXA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19fdb5e5-3e55-438f-8ba8-e56998cad6ba_2000x1264.jpeg)_One of the possible isometric views._

The math for this projection is still simple. The screen _x_ coordinate is dictated by model _x_ multiplied by _cos(_ 30° _)_ — that’s the angle between the model _x_ axis and the real one. The value is also influenced in the same way but with an opposite sign by the model _z_ axis, so we get:

\\(x_{screen} = (x_{model} - z_{model}) \cdot cos(30^\circ) \\)

Meanwhile, on the _y_ side, we need to account for the projected sine component of _x_ and _z:_

\\(y_{screen} = y_{model} + (x_{model} + z_{model}) \cdot sin(30^\circ) \\)

Both cosine expressions can be further divided by √2 if the goal is to match the model- and screen-lengths of a horizontal line drawn in the model XY plane and then rotated by 45° around the _y_ axis. That said, it’s seldom a necessity.

The following video shows a cube rotated in the XZ plane in an isometric projection:

This looks great and it seems natural to extend the scheme to four dimensions simply by cramming another axis, giving us a progression of _x, y, z,_ and 🌀 axes spaced 45° apart:

[![](https://substackcdn.com/image/fetch/$s_!xkVm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F823c4b22-c1d4-4a11-9625-bf4ea63cc9ec_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!xkVm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F823c4b22-c1d4-4a11-9625-bf4ea63cc9ec_2000x1300.jpeg)_An extension of isometric projection to 4D?_

Yet, some readers might notice that with this modification, we’re back to the earlier “cavalier” scenario: our _x, y,_ and _z_ axes are now separated by an impossible angle of 45°. In other words, the projection should give us _something_ , but it will distort some 3D shapes in undesirable ways.

Still, let’s keep going. In the new model, we calculate screen _x_ as:

\\(x_{screen} = -🌀_{model} + (x_{model} - z_{model}) \cdot cos(45^\circ)\\)

The projected model _y_ axis is orthogonal to to screen _x_ , so it doesn’t appear in this formula. As for the _y_ coordinate, we need:

\\(y_{screen} = y_{model} + (x_{model} + z_{model}) \cdot sin(45^\circ)\\)

As before, since the projected model 🌀 axis is orthogonal to screen _y_ , it doesn’t appear in the second equation.

Let’s put this projection to real use. Here’s the video of a tesseract rotating in the XZ plane:

It looks pretty, but it isn’t particularly informative: the projection makes the object change shape in ways that seem difficult to parse. The shape appears to be intersecting itself, but it’s hard to pinpoint what’s what.

#### Rectilinear one-point perspective

A simpler but surprisingly powerful projection method is to keep model _x_ and _y_ in the same plane as the screen, but divide the values of these coordinates in proportion to the distance in _z_. This produces a familiar vanishing-point perspective:

A fairly natural extension of this technique to the fourth dimension is to divide the _x_ and _y_ coordinates twice: first by a _z-_ dependent factor and then by a 🌀-dependent one. This nets probably the most recognizable visualization of a tesseract:

If you want food for thought, consider the real-world appearance of a wireframe 3D cube when its shadow from a nearby overhead light is cast onto a 2D surface:

[![](https://substackcdn.com/image/fetch/$s_!Punz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d9c28a-f287-4b29-abc2-40d701fcdf60_1409x1012.jpeg)](https://substackcdn.com/image/fetch/$s_!Punz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d9c28a-f287-4b29-abc2-40d701fcdf60_1409x1012.jpeg)_It’s deja vu all over again._

This both helps make some sense of the nested-cube visualization of the tesseract, and signals that our algorithm is directionally correct. That said, the approach we’ve taken is also a bit of a cop-out: by commingling model _z_ and 🌀, we make these dimensions indistinguishable.

#### Fisheye perspective

At first blush, the tesseract visualization might look just like two nested 3D cubes connected in the corners. To reduce edge overlaps and better hint at the underlying shenanigans, we can switch to a curvilinear “fisheye” perspective, reminiscent of what you can see through a peephole or other low-quality, wide-angle lens. In this approach, point coordinates are reduced based on their Euclidean distance from a single reference point representing the camera. For a regular cube, we get:

But of course, we’re here to look at the tesseract:

The shading and the drawing order of the points is decided by the Euclidean distance to the viewing plane; this allows us to spot that the edges of the smaller, “inner” cube appear to pass behind the edges of the larger one:

[![](https://substackcdn.com/image/fetch/$s_!ngOa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925bb8c4-fbbc-4661-9bfb-ce76d7bce0ce_1080x1080.png)](https://substackcdn.com/image/fetch/$s_!ngOa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925bb8c4-fbbc-4661-9bfb-ce76d7bce0ce_1080x1080.png)_Could it be…?_

Still, as noted earlier, the disappointing part of the mapping is that it commingles two dimensions; can we distinguish them better without ending up with a visual disaster?

#### Mixed isometric + vanishing point

Sort of?… Instead of trying to come up with a single projection for all four axes, we could always use a conventional isometric view for _x, y,_ and _z,_ and then use the vanishing-point approach to represent 🌀.

The result is a remarkably stable and easy-to-parse view of the tesseract when rotated in the YZ plane:

This also brings us to a somewhat less-correct rendering of the hypercube spinning in the _Z_ 🌀 plane that can be found on Wikipedia and in some YouTube videos. If we change screen depth calculations to only account for the _z_ coordinate (i.e., completely ignore model 🌀), we obtain the following:

If you squint your eyes, this appears to show the tesseract passing through itself back-to-front as it rotates in the fourth dimension. I altered the proportions of the projection to make the effect easier to see.

Subscribe

 _👉 For more weird math,[click here](https://lcamtuf.substack.com/p/algorithms-and-math-trivia)._

21

4

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![lcamtuf's avatar](https://substackcdn.com/image/fetch/$s_!koIn!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F160026b1-f333-4244-b8dc-5ca8c437a0b4_400x400.jpeg)](https://substack.com/profile/92541588-lcamtuf?utm_source=comment)

[lcamtuf](https://substack.com/profile/92541588-lcamtuf?utm_source=substack-feed-item)

[Jan 28](https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube/comment/206204915 "Jan 28, 2026, 12:25 AM")

Pinned

PS. MATLAB code used to generate animation frames is here: <https://lcamtuf.coredump.cx/blog/hypercube.m>

ReplyShare

[![Rainbow Roxy's avatar](https://substackcdn.com/image/fetch/$s_!HMi_!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb98fdd41-e8f8-4b6a-900e-ac00feba0477_600x600.jpeg)](https://substack.com/profile/405122571-rainbow-roxy?utm_source=comment)

[Rainbow Roxy](https://substack.com/profile/405122571-rainbow-roxy?utm_source=substack-feed-item)

[6d](https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube/comment/207347019 "Jan 30, 2026, 9:25 AM")

Hey, great read as always. I've realy been fascinated by how tesseracts are rendered. Sometimes I feel like I'm trying to fold myself into a hypercube in Pilates, so this breakdown just resonated. Thanks for making such a complex topic so clear!

ReplyShare

[2 more comments...](https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube/comments)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 lcamtuf · [Publisher Privacy](https://lcamtuf.substack.com/privacy)

Substack · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
