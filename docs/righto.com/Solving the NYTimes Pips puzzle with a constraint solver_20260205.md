# Solving the NYTimes Pips puzzle with a constraint solver

**来源:** https://righto.com
**链接:** http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html
**日期:** 2025-10-18T08:41:00.000-07:00

---

#  [ Ken Shirriff's blog ](http://www.righto.com/)

Computer history, restoring vintage computers, IC reverse engineering, and whatever

###  Solving the NYTimes Pips puzzle with a constraint solver 

The New York Times recently introduced a new daily puzzle called [Pips](https://www.nytimes.com/games/pips). You place a set of dominoes on a grid, satisfying various conditions. For instance, in the puzzle below, the pips (dots) in the purple squares must sum to 8, there must be fewer than 5 pips in the red square, and the pips in the three green squares must be equal. (It doesn't take much thought to solve this "easy" puzzle, but the "medium" and "hard" puzzles are more challenging.)

[![The New York Times Pips puzzle from Oct 5, 2025 \(easy\). Hint: What value must go in the three green squares?](https://static.righto.com/images/pips/pips-10-5-easy-w300.jpg)](https://static.righto.com/images/pips/pips-10-5-easy.jpg)

The New York Times Pips puzzle from Oct 5, 2025 (easy). Hint: What value must go in the three green squares?

I was wondering about how to solve these puzzles with a computer. Recently, I saw an article on [Hacker News](https://news.ycombinator.com/item?id=45222695)--"[Many hard LeetCode problems are easy constraint problems](https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/)"--that described the benefits and flexibility of a system called a constraint solver. A constraint solver takes a set of constraints and finds solutions that satisfy the constraints: exactly what Pips requires.

I figured that solving Pips with a constraint solver would be a good way to learn more about these solvers, but I had several questions. Did constraint solvers require incomprehensible mathematics? How hard was it to express a problem? Would the solver quickly solve the problem, or would it get caught in an exponential search?

It turns out that using a constraint solver was straightforward; it took me under two hours from knowing nothing about constraint solvers to solving the problem. The solver found solutions in milliseconds (for the most part). However, there were a few bumps along the way. In this blog post, I'll discuss my experience with the [MiniZinc](https://www.minizinc.org/)1 constraint modeling system and show how it can solve Pips.

## Approaching the problem

Writing a program for a constraint solver is very different from writing a regular program. Instead of telling the computer _how_ to solve the problem, you tell it _what_ you want: the conditions that must be satisfied. The solver then "magically" finds solutions that satisfy the problem.

To solve the problem, I created an array called `pips` that holds the number of domino pips at each position in the grid. Then, the three constraints for the above problem can be expressed as follows. You can see how the constraints directly express the conditions in the puzzle.
    
    
    constraint pips[1,1] + pips[2,1] == 8;
    constraint pips[2,3] < 5;
    constraint all_equal([pips[3,1], pips[3,2], pips[3,3]]);
    

Next, I needed to specify where dominoes could be placed for the puzzle. To do this, I defined an array called `grid` that indicated the allowable positions: 1 indicates a valid position and 0 indicates an invalid position. (If you compare with the puzzle at the top of the article, you can see that the grid below matches its shape.)
    
    
    grid = [|
    1,1,0|
    1,1,1|
    1,1,1|];
    

I also defined the set of dominoes for the problem above, specifying the number of spots in each half:
    
    
    spots = [|5,1| 1,4| 4,2| 1,3|];
    

So far, the constraints directly match the problem. However, I needed to write some more code to specify how these pieces interact. But before I describe that code, I'll show a solution. I wasn't sure what to expect: would the constraint solver give me a solution or would it spin forever? It turned out to find the unique solution in 109 milliseconds, printing out the solution arrays. The `pips` array shows the number of pips in each position, while the `dominogrid` array shows which domino (1 through 4) is in each position.
    
    
    pips = 
    [| 4, 2, 0
     | 4, 5, 3
     | 1, 1, 1
     |];
    dominogrid = 
    [| 3, 3, 0
     | 2, 1, 4
     | 2, 1, 4
     |];
    

The text-based solution above is a bit ugly. But it is easy to create graphical output. MiniZinc provides a JavaScript API, so you can easily display solutions on a web page. I wrote a few lines of JavaScript to draw the solution, as shown below. (I just display the numbers since I was too lazy to draw the dots.) Solving this puzzle is not too impressive--it's an "easy" puzzle after all--but I'll show below that the solver can also handle considerably more difficult puzzles.

[![Graphical display of the solution.](https://static.righto.com/images/pips/solution-10-5-easy-w300.jpg)](https://static.righto.com/images/pips/solution-10-5-easy.jpg)

Graphical display of the solution.

### Details of the code

While the above code specifies a particular puzzle, a bit more code is required to define how dominoes and the grid interact. This code may appear strange because it is implemented as constraints, rather than the procedural operations in a normal program.

My main design decision was how to specify the locations of dominoes. I considered assigning a grid position and orientation to each domino, but it seemed inconvenient to deal with multiple orientations. Instead, I decided to position each half of the domino independently, with an `x` and `y` coordinate in the grid.2 I added a constraint that the two halves of each domino had to be in neighboring cells, that is, either the X or Y coordinates had to differ by 1.
    
    
    constraint forall(i in DOMINO) (abs(x[i, 1] - x[i, 2]) + abs(y[i, 1] - y[i, 2]) == 1);
    

It took a bit of thought to fill in the `pips` array with the number of spots on each domino. In a normal programming language, one would loop over the dominoes and store the values into `pips`. However, here it is done with a constraint so the solver makes sure the values are assigned. Specifically, for each half-domino, the `pips` array entry at the domino's x/y coordinate must equal the corresponding `spots` on the domino:
    
    
    constraint forall(i in DOMINO, j in HALF) (pips[y[i,j], x[i, j]] == spots[i, j]);
    

I decided to add another array to keep track of which domino is in which position. This array is useful to see the domino locations in the output, but it also keeps dominoes from overlapping. I used a constraint to put each domino's number (1, 2, 3, etc.) into the occupied position of `dominogrid`:
    
    
    constraint forall(i in DOMINO, j in HALF) (dominogrid[y[i,j], x[i, j]] == i);
    

Next, how do we make sure that dominoes only go into positions allowed by `grid`? I used a constraint that a square in `dominogrid` must be empty or the corresponding `grid` must allow a domino.3 This uses the "or" condition, which is expressed as `\/`, an unusual stylistic choice. (Likewise, "and" is expressed as `/\`. These correspond to the logical symbols ∨ and ∧.)
    
    
    constraint forall(i in 1..H, j in 1..W) (dominogrid[i, j] == 0 \/ grid[i, j] != 0);
    

Honestly, I was worried that I had too many arrays and the solver would end up in a rathole ensuring that the arrays were consistent. But I figured I'd try this brute-force approach and see if it worked. It turns out that it worked for the most part, so I didn't need to do anything more clever.

Finally, the program requires a few lines to define some constants and variables. The constants below define the number of dominoes and the size of the grid for a particular problem:
    
    
    int: NDOMINO = 4; % Number of dominoes in the puzzle
    int: W = 3; % Width of the grid in this puzzle
    int: H = 3; % Height of the grid in this puzzle
    

Next, datatypes are defined to specify the allowable values. This is very important for the solver; it is a "finite domain" solver, so limiting the size of the domains reduces the size of the problem. For this problem, the values are integers in a particular range, called a `set`:
    
    
    set of int: DOMINO = 1..NDOMINO; % Dominoes are numbered 1 to NDOMINO
    set of int: HALF = 1..2; % The domino half is 1 or 2
    set of int: xcoord = 1..W; % Coordinate into the grid
    set of int: ycoord = 1..H;
    

At last, I define the sizes and types of the various arrays that I use. One very important syntax is `var`, which indicates variables that the solver must determine. Note that the first two arrays, `grid` and `spots` do not have `var` since they are constant, initialized to specify the problem.
    
    
    array[1..H,1..W] of 0..1: grid; % The grid defining where dominoes can go
    array[DOMINO, HALF] of int: spots; % The number of spots on each half of each domino
    array[DOMINO, HALF] of var xcoord: x; % X coordinate of each domino half
    array[DOMINO, HALF] of var ycoord: y; % Y coordinate of each domino half
    array[1..H,1..W] of var 0..6: pips; % The number of pips (0 to 6) at each location.
    array[1..H,1..W] of var 0..NDOMINO: dominogrid; % The domino sequence number at each location
    

You can find all the code on [GitHub](https://github.com/shirriff/pips). One weird thing is that because the code is not procedural, the lines can be in any order. You can use arrays or constants before you use them. You can even move `include` statements to the end of the file if you want!

## Complications

Overall, the solver was much easier to use than I expected. However, there were a few complications.

By changing a setting, the solver can find multiple solutions instead of stopping after the first. However, when I tried this, the solver generated thousands of meaningless solutions. A closer look showed that the problem was that the solver was putting arbitrary numbers into the "empty" cells, creating valid but pointlessly different solutions. It turns out that I didn't explicitly forbid this, so the sneaky constraint solver went ahead and generated tons of solutions that I didn't want. Adding another constraint fixed the problem. The moral is that even if you think your constraints are clear, solvers are very good at finding unwanted solutions that technically satisfy the constraints. 4

A second problem is that if you do something wrong, the solver simply says that the problem is unsatisfiable. Maybe there's a clever way of debugging, but I ended up removing constraints until the problem can be satisfied, and then see what I did wrong with that constraint. (For instance, I got the array indices backward at one point, making the problem insoluble.)

The most concerning issue is the unpredictability of the solver: maybe it will take milliseconds or maybe it will take hours. For instance, the Oct 5 hard Pips puzzle (below) caused the solver to take minutes for no apparent reason. However, the MiniZinc IDE supports different solver backends. I switched from the default [Gecode](https://www.gecode.dev/publications.html) solver to [Chuffed](https://github.com/chuffed/chuffed), and it immediately found numerous solutions, 384 to be precise. (Sometimes the Pips puzzles sometimes have multiple solutions, which players find [controversial](https://www.reddit.com/r/nytpips/comments/1nyfk5u/sunday_oct_5_2025_pips_49_thread/).) I suspect that the multiple solutions messed up the Gecode solver somehow, perhaps because it couldn't narrow down a "good" branch in the search tree. For a benchmark of the different solvers, see the footnote.5

[![Two of the 384 solutions to the NYT Pips puzzle from Oct 5, 2025 \(hard difficulty\).](https://static.righto.com/images/pips/solutions-10-5-hard-w600.jpg)](https://static.righto.com/images/pips/solutions-10-5-hard.jpg)

Two of the 384 solutions to the NYT Pips puzzle from Oct 5, 2025 (hard difficulty).

## How does a constraint solver work?

If you were writing a program to solve Pips from scratch, you'd probably have a loop to try assigning dominoes to positions. The problem is that the problem grows exponentially. If you have 16 dominoes, there are 16 choices for the first domino, 15 choices for the second, and so forth, so about 16! combinations in total, and that's ignoring orientations. You can think of this as a search tree: at the first step, you have 16 branches. For the next step, each branch has 15 sub-branches. Each sub-branch has 14 sub-sub-branches, and so forth.

An easy optimization is to check the constraints after each domino is added. For instance, as soon as the "less than 5" constraint is violated, you can [backtrack](https://en.wikipedia.org/wiki/Backtracking) and skip that entire section of the tree. In this way, only a subset of the tree needs to be searched; the number of branches will be large, but hopefully manageable.

A constraint solver works similarly, but in a more abstract way. The constraint solver assigns values to the variables, backtracking when a conflict is detected. Since the underlying problem is typically NP-complete, the solver uses heuristics to attempt to improve performance. For instance, variables can be assigned in different orders. The solver attempts to generate conflicts as soon as possible so large pieces of the search tree can be pruned sooner rather than later. (In the domino case, this corresponds to placing dominoes in places with the tightest constraints, rather than scattering them around the puzzle in "easy" spots.)

Another technique is constraint propagation. The idea is that you can derive new constraints and catch conflicts earlier. For instance, suppose you have a problem with the constraints "a equals c" and "b equals c". If you assign "a=1" and "b=2", you won't find a conflict until later, when you try to find a value for "c". But with constraint propagation, you can derive a new constraint "a equals b", and the problem will turn up immediately. (Solvers handle more complicated constraint propagation, such as inequalities.) The tradeoff is that generating new constraints takes time and makes the problem larger, so constraint propagation can make the solver slower. Thus, heuristics are used to decide when to apply constraint propagation.

Researchers are actively developing new algorithms, heuristics, and optimizations6 such as backtracking more aggressively (called "backjumping"), keeping track of failing variable assignments (called "nogoods"), and leveraging Boolean SAT (satisfiability) solvers. Solvers compete in [annual challenges](https://www.minizinc.org/challenge/) to test these techniques against each other. The nice thing about a constraint solver is that you don't need to know anything about these techniques; they are applied automatically.

## Conclusions

I hope this has convinced you that constraint solvers are interesting, not too scary, and can solve real problems with little effort. Even as a beginner, I was able to get started with MiniZinc quickly. (I read half the [tutorial](https://docs.minizinc.dev/en/stable/modelling.html) and then jumped into programming.)

One reason to look at constraint solvers is that they are a completely different programming paradigm. Using a constraint solver is like programming on a higher level, not worrying about how the problem gets solved or what algorithm gets used. Moreover, analyzing a problem in terms of constraints is a different way of thinking about algorithms. Some of the time it's frustrating when you can't use familiar constructs such as loops and assignments, but it expands your horizons.

Finally, writing code to solve Pips is more fun than solving the problems by hand, at least in my opinion, so give it a try!

For more, follow me on Bluesky ([@righto.com](https://bsky.app/profile/righto.com)), Mastodon ([@[email protected]](https://oldbytes.space/@kenshirriff)), [RSS](http://www.righto.com/feeds/posts/default), or subscribe [here](https://righto.kit.com/20bf534dff).

[![Solution to the Pips puzzle, September 21, 2005 \(hard\). This puzzle has regions that must all be equal \(=\) and regions that must all be different \(≠\). Conveniently, MiniZinc has all_equal and alldifferent constraint functions.](https://static.righto.com/images/pips/solution-9-21-hard-w330.jpg)](https://static.righto.com/images/pips/solution-9-21-hard.jpg)

Solution to the Pips puzzle, September 21, 2005 (hard). This puzzle has regions that must all be equal (=) and regions that must all be different (≠). Conveniently, MiniZinc has `all_equal` and `alldifferent` constraint functions.

## Notes and references

  1. I started by downloading the [MiniZinc IDE](https://www.minizinc.org/) and reading the [MiniZinc tutorial](https://docs.minizinc.dev/en/stable/part_2_tutorial.html). The MiniZinc IDE is straightforward, with an editor window at the top and an output window at the bottom. Clicking the "Run" button causes it to generate a solution.

[![Screenshot of the MiniZinc IDE. Click for a larger view.](https://static.righto.com/images/pips/ide-w600.jpg)](https://static.righto.com/images/pips/ide.jpg)

Screenshot of the MiniZinc IDE. Click for a larger view.

↩

  2. It might be cleaner to combine the X and Y coordinates into a single `Point` type, using a MiniZinc [record type](https://docs.minizinc.dev/en/stable/tuple_and_record_types.html). ↩

  3. I later decided that it made more sense to enforce that `dominogrid` is empty if and only if `grid` is 0 at that point, although it doesn't affect the solution. This constraint uses the "if and only if" operator `<->`.
         
         constraint forall(i in 1..H, j in 1..W) (dominogrid[i, j] == 0 <-> grid[i, j] == 0);
         

↩

  4. To prevent the solver from putting arbitrary numbers in the unused positions of `pips`, I added a constraint to force these values to be zero:
         
         constraint forall(i in 1..H, j in 1..W) (grid[i, j] == 0 -> pips[i, j] == 0);
         

Generating multiple solutions had a second issue, which I expected: A symmetric domino can be placed in two redundant ways. For instance, a double-six domino can be flipped to produce a solution that is technically different but looks the same. I fixed this by adding constraints for each symmetric domino to allow only one of the two redundant positions. The constraint below forces a preferred orientation for symmetric dominoes.
         
         constraint forall(i in DOMINO) (spots[i,1] != spots[i,2] \/ x[i,1] > x[i,2] \/ (x[i,1] == x[i,2] /\ y[i,1] > y[i,2]));
         

To enable multiple solutions in MiniZinc, the setting is under Show Configuration Editor > User Defined Behavior > Satisfaction Problems or the `--all` flag from the command line. ↩

  5. MiniZinc has five solvers that can solve this sort of integer problem: [Chuffed](https://github.com/chuffed/chuffed), [OR Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver), [Gecode](https://github.com/Gecode/gecode), [HiGHS](https://highs.dev/), and [Coin-OR BC](https://github.com/coin-or/Cbc). I measured the performance of the five solvers against 20 different Pips puzzles. Most of the solvers found solutions in under a second, most of the time, but there is a lot of variation.

[![Timings for different solvers on 20 Pip puzzles.](https://static.righto.com/images/pips/benchmarks-w600.jpg)](https://static.righto.com/images/pips/benchmarks.jpg)

Timings for different solvers on 20 Pip puzzles.

Overall, Chuffed had the best performance on the puzzles that I tested, taking well under a second. Google's OR-Tools won all the categories in the [2025 MiniZinc challenge](https://www.minizinc.org/challenge/2025/results/), but it was considerably slower than Chuffed for my Pips programs. The default Gecode solver performed very well most of the time, but it did terribly on a few problems, taking over 15 minutes. HiGHs was slower in general, taking a few minutes on the hardest problems, but it didn't fail as badly as Gecode. (Curiously, Gecode and HiGHS sometimes found different problems to be difficult.) Finally, Coin-OR BC was uniformly bad; at best it took a few seconds, but one puzzle took almost two hours and others weren't solved before I gave up after two hours. (I left Coin-OR BC off the graph because it messed up the scale.)

Don't treat these results too seriously because different solvers are optimized for different purposes. (In particular, Coin-OR BC is designed for linear problems.) But the results demonstrate the unpredictability of solvers: maybe you get a solution in a second and maybe you get a solution in hours. ↩

  6. If you want to read more about solvers, [Constraint Satisfaction Problems](https://zoo.cs.yale.edu/classes/cs470/lectures/s2019/07-CSP.pdf) is an overview presentation. The Gecode algorithms are described in a nice technical report: [Constraint Programming Algorithms used in Gecode](https://www.researchgate.net/publication/311953428_Constraint_Programming_Algorithms_used_in_Gecode). Chuffed is more complicated: "Chuffed is a state of the art lazy clause solver designed from the ground up with lazy clause generation in mind. Lazy clause generation is a hybrid approach to constraint solving that combines features of finite domain propagation and Boolean satisfiability." The Chuffed paper [Lazy clause generation reengineered](https://people.eng.unimelb.edu.au/pstuckey/papers/cp09-lc.pdf) and [slides](https://school.a4cp.org/summer2011/slides/Gent/Peter%20Stuckey%20-%20Lazy%20Clause%20Generation.pdf) are more of a challenge.  ↩




[ ![](http://img1.blogblog.com/img/icon18_email.gif) ](https://www.blogger.com/email-post/6264947694886887540/983202427505631074 "Email Post") [ ![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=6264947694886887540&postID=983202427505631074&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=983202427505631074&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=983202427505631074&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=983202427505631074&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=983202427505631074&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=983202427505631074&target=pinterest "Share to Pinterest")

Labels: [math](http://www.righto.com/search/label/math), [random](http://www.righto.com/search/label/random)

#### 6 comments:

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

SWI-Prolog CLP(fd) 

     [ October 18, 2025 at 10:53 AM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1760810024635#c6926595031117924665 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/6926595031117924665 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

When writing VHDL code for FPGA's, I encounter such constraint solvers: I write "assert" statements that describe properties that the block must satisfy. Then the constraint solver will try to find a sequence of inputs that violate any one of these assert statements. The tricky part - as you say - is getting used to thinking in terms of properties. For instance, one way to describe the function of a FIFO is that if A is seen before B on the output, then A must also come before B on the input. But coming up with these assertions is a brain twister. 

     [ October 18, 2025 at 12:04 PM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1760814279107#c9055925801377381734 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/9055925801377381734 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

I have not used any of the declarative programming languages like Prolog II, but would those be similarly effective for problems like these? I thought that Ada was a constraint-based language, but apparently not. It looks like the first comment above is referring to CLP(R) ? which is a superset of Prolog. 

     [ October 18, 2025 at 2:40 PM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1760823638229#c7673337898659853395 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/7673337898659853395 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

FD said... 
    

> This uses the "or" condition, which is expressed as \/, an unusual  
> stylistic choice. (Likewise, "and" is expressed as /\\. These  
> correspond to the logical symbols ∨ and ∧.)  
  
MiniZinc input is unicode, so you can use ∧ and ∨ directly  
(https://docs.minizinc.dev/en/stable/spec.html#bin-ops-unicode).  
  
> A second problem is that if you do something wrong, the solver  
> simply says that the problem is unsatisfiable. Maybe there's a  
> clever way of debugging, but I ended up removing constraints until  
> the problem can be satisfied, and then see what I did wrong with  
> that constraint.  
  
This is a know problem with CP and the debuging technique you used is  
the common one.  
  
> I suspect that the multiple solutions messed up the Gecode solver  
> somehow, perhaps because it couldn't narrow down a "good" branch in  
> the search tree.  
  
Depending on the type of the solver, different constraints lead to  
differing levels of propagation, and are therefore more/less  
successful in avoiding search. Adding redundant constraints expressed  
differently, but implying the same thing, can sometimes give you a  
CP-program which is fast using multiple solvers.  
  
MiniZinc IDE has a CP-profiler  
(https://docs.minizinc.dev/en/stable/cpprofiler.html) which lets you  
look at the search tree as the search progresses. Some solvers, such  
as Gecode, allow you to influence the search strategy. Unfortunately  
Gecode is no longer actively developed, as Christian Schulte, the main  
developer, died in 2020 (https://www.a4cp.org/-24). If he were alive,  
he would not have allowed Chuffed to beat Gecode for very  
long. Although good friends, there was always a healthy competition  
between Schulte and Stuckey (one of the developers of Chuffed).  
  
BTW Christian Schulte is the father of the modern way of implementing  
CP by dividing up the implementation into three distinct areas:  
maintaining the state of the constraint variables, propagation and  
search. His Phd-thesis  
(https://link.springer.com/book/10.1007/3-540-45945-6) is well worth a  
read.  


     [ October 19, 2025 at 10:47 AM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1760896077312#c2681913168269467202 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/2681913168269467202 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

My first thought was they've re-invented Prolog, a language I hate with a passion (my brain and it do not agree). I'd be curious to see a Prolog implementation of the same problem. 

     [ October 20, 2025 at 11:19 PM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1761027559077#c6319629252239960056 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/6319629252239960056 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png) ](https://www.blogger.com/profile/17085707453187179626)

[Tigrou](https://www.blogger.com/profile/17085707453187179626) said... 
    

I really recommend taking a look at "SAT/SMT by Example by Dennis Yurichev" ebook. It contains lot of puzzles/problems and the SAT/SMT equivalent solution. You can find it easily on Google. The official link from smt.st domain is broken but it can be downloaded from wayback machine. 

     [ November 22, 2025 at 2:39 PM ](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html?showComment=1763851141741#c4793901570867130927 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/4793901570867130927 "Delete Comment")

[Post a Comment](https://www.blogger.com/comment/fullpage/post/6264947694886887540/983202427505631074)

[Newer Post](http://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html "Newer Post") [Older Post](http://www.righto.com/2025/09/marilou-schultz-navajo-555-weaving.html "Older Post") [Home](http://www.righto.com/)

[Subscribe](https://righto.kit.com/20bf534dff
)

[Contact info and site index](https://www.righto.com/p/index.html)

## Popular Posts

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_t5PKnrEF1fLjjQMJ1zf8UxFcfPawLITDCr0WNUtFW6MIIxrS6IudrPt1-W7zVHnA97AzVE41-UiFToXaEconRtOoduXW2eW9B_4T1sILyCoow=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

[A Multi-Protocol Infrared Remote Library for the Arduino](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_uo1KLY6cKndrrJWcDDoa8dUlh97njRoAGoW0SVgwep70n5OXUeDIaSS1Qzh-Qh6pQhQ0p_otQB65DdtrcUVegfBkJIDgreT5mMxPHIo6yOeFyQCYRK_NRt5rU2ZNH2NMxbWTERYGc1-Q=w72-h72-p-k-no-nu) ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

[Notes on the Intel 8086 processor's arithmetic-logic unit](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_swxZd70ysen4R8ivBelCJa1S8moZ5n7WMk_qBGA4jR1pupa6VI56DieiiUZGpPY4vTItTIhdMeSTt02mygnDrDfVR4QTqjqOj-t-ThDwbV8eL2hNbqPsGCEUWLGgY=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

[A dozen USB chargers in the lab: Apple is very good, but not quite the best](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sB0xWSaLLTAiCdpvmN7Z9HQDS7BusrQOVxWxE37kvzblCiG5IXfRJBj0EAjjwBwpk59HCY62x7mpxzSocjG67K0s30uTQlrYEdio05YGGw_2l04AOy6OH3DQd_k516DtlMBZTI7ifk-IUeSZBenxOz2sA=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

[Apple iPhone charger teardown: quality in a tiny expensive package](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_tLuRlv1pr3Y55WTXqO7O9Tnq-QNYV8Ko-fXIEdYB2qPZTLavUO7cg0KxVUs1Dj9hUcUN8aWa7QSYoU6rSHlJlwT-7IPQ2C7YBvpQh28u8-9t-P12mrRwKs3f-16k1DwZD7QRWBK2CS8BOkLjik=w72-h72-p-k-no-nu) ](http://www.righto.com/2025/12/8087-microcode-conditions.html)

[Conditions in the Intel 8087 floating-point chip's microcode](http://www.righto.com/2025/12/8087-microcode-conditions.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_s7w0iYcjt66-9B3Al0qouosfmjkXxf7nCfReUKuHNzeMQBK_KAQnQiBzuoiwxdRY6p4_4CaPoIq5kzIzGUBzpgWF0w0leatGGNausbFxR4E9yDJb1l7XzPPMbIwx_wb9amMDC1Zp30G_i9Z04=w72-h72-p-k-no-nu) ](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

[Teardown and exploration of Apple's Magsafe connector](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sE7Ptz5al8KfBlCHim3ytsezk6nSOTMcZbvGBt6R9ZKDCjGKvCikjxVMNmxBH64gC38x4PNrPnVZYZFcdMHepMEkOTfs02h3YUb-mEA-rUEL7q1iLSH7WWWC9A7Jj0nqis=w72-h72-p-k-no-nu) ](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

[Mining Bitcoin with pencil and paper: 0.67 hashes per day](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_v8XWCKRvmI7Jmjtj7XPniyJLaC55pZAQdwebJIZ4q2MTfWdPF_AmhhaVy8YjISGQL2ZmXhZIZzeETT7dlTJxyFRTs7G44zo1-6JG2HN10B=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)

[An Arduino universal remote: record and playback IR signals](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)




## Search This Blog

|   
---|---  
  
## Labels

[386](http://www.righto.com/search/label/386) [6502](http://www.righto.com/search/label/6502) [8008](http://www.righto.com/search/label/8008) [8085](http://www.righto.com/search/label/8085) [8086](http://www.righto.com/search/label/8086) [8087](http://www.righto.com/search/label/8087) [8088](http://www.righto.com/search/label/8088) [aerospace](http://www.righto.com/search/label/aerospace) [alto](http://www.righto.com/search/label/alto) [analog](http://www.righto.com/search/label/analog) [Apollo](http://www.righto.com/search/label/Apollo) [apple](http://www.righto.com/search/label/apple) [arc](http://www.righto.com/search/label/arc) [arduino](http://www.righto.com/search/label/arduino) [arm](http://www.righto.com/search/label/arm) [beaglebone](http://www.righto.com/search/label/beaglebone) [bitcoin](http://www.righto.com/search/label/bitcoin) [c#](http://www.righto.com/search/label/c%23) [cadc](http://www.righto.com/search/label/cadc) [calculator](http://www.righto.com/search/label/calculator) [chips](http://www.righto.com/search/label/chips) [css](http://www.righto.com/search/label/css) [datapoint](http://www.righto.com/search/label/datapoint) [dx7](http://www.righto.com/search/label/dx7) [electronics](http://www.righto.com/search/label/electronics) [f#](http://www.righto.com/search/label/f%23) [fairchild](http://www.righto.com/search/label/fairchild) [fpga](http://www.righto.com/search/label/fpga) [fractals](http://www.righto.com/search/label/fractals) [genome](http://www.righto.com/search/label/genome) [globus](http://www.righto.com/search/label/globus) [haskell](http://www.righto.com/search/label/haskell) [HP](http://www.righto.com/search/label/HP) [html5](http://www.righto.com/search/label/html5) [ibm](http://www.righto.com/search/label/ibm) [ibm1401](http://www.righto.com/search/label/ibm1401) [ibm360](http://www.righto.com/search/label/ibm360) [intel](http://www.righto.com/search/label/intel) [ipv6](http://www.righto.com/search/label/ipv6) [ir](http://www.righto.com/search/label/ir) [java](http://www.righto.com/search/label/java) [javascript](http://www.righto.com/search/label/javascript) [math](http://www.righto.com/search/label/math) [microcode](http://www.righto.com/search/label/microcode) [oscilloscope](http://www.righto.com/search/label/oscilloscope) [Pentium](http://www.righto.com/search/label/Pentium) [photo](http://www.righto.com/search/label/photo) [power supply](http://www.righto.com/search/label/power%20supply) [random](http://www.righto.com/search/label/random) [reverse-engineering](http://www.righto.com/search/label/reverse-engineering) [sheevaplug](http://www.righto.com/search/label/sheevaplug) [snark](http://www.righto.com/search/label/snark) [space](http://www.righto.com/search/label/space) [spanish](http://www.righto.com/search/label/spanish) [synth](http://www.righto.com/search/label/synth) [teardown](http://www.righto.com/search/label/teardown) [theory](http://www.righto.com/search/label/theory) [unicode](http://www.righto.com/search/label/unicode) [Z-80](http://www.righto.com/search/label/Z-80)

## Blog Archive

  * [ ► ](javascript:void\(0\)) [ 2026 ](http://www.righto.com/2026/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2026/01/) (1)


  * [ ▼ ](javascript:void\(0\)) [ 2025 ](http://www.righto.com/2025/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2025/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2025/11/) (1)
    * [ ▼ ](javascript:void\(0\)) [ October ](http://www.righto.com/2025/10/) (1)
      * [Solving the NYTimes Pips puzzle with a constraint ...](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2025/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2025/08/) (4)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2025/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2025/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2025/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2025/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2025/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2025/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2025/01/) (4)


  * [ ► ](javascript:void\(0\)) [ 2024 ](http://www.righto.com/2024/) (21)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2024/12/) (1)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2024/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2024/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2024/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2024/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2024/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2024/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2024/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2024/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2024/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2024/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2024/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2023 ](http://www.righto.com/2023/) (35)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2023/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2023/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2023/10/) (3)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2023/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2023/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2023/07/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2023/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2023/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2023/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2023/02/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2023/01/) (8)


  * [ ► ](javascript:void\(0\)) [ 2022 ](http://www.righto.com/2022/) (18)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2022/11/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2022/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2022/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2022/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2022/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2022/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2022/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2022/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2022/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2021 ](http://www.righto.com/2021/) (26)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2021/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2021/11/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2021/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2021/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2021/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2021/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2021/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2021/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2021/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2021/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2021/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2020 ](http://www.righto.com/2020/) (33)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2020/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2020/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2020/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2020/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2020/08/) (5)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2020/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2020/06/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2020/05/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2020/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2020/03/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2020/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2019 ](http://www.righto.com/2019/) (18)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2019/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2019/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2019/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2019/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2019/07/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2019/04/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2019/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2019/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2018 ](http://www.righto.com/2018/) (17)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2018/12/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2018/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2018/08/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2018/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2018/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2018/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2018/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2018/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2018/01/) (4)


  * [ ► ](javascript:void\(0\)) [ 2017 ](http://www.righto.com/2017/) (21)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2017/12/) (5)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2017/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2017/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2017/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2017/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2017/06/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2017/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2017/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2017/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2017/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2016 ](http://www.righto.com/2016/) (34)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2016/12/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2016/10/) (5)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2016/09/) (8)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2016/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2016/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2016/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2016/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2016/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2016/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2016/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2016/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2015 ](http://www.righto.com/2015/) (12)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2015/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2015/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2015/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2015/08/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2015/05/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2015/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2015/02/) (1)


  * [ ► ](javascript:void\(0\)) [ 2014 ](http://www.righto.com/2014/) (13)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2014/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2014/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2014/09/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2014/05/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2014/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2014/02/) (5)


  * [ ► ](javascript:void\(0\)) [ 2013 ](http://www.righto.com/2013/) (24)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2013/11/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2013/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2013/08/) (4)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2013/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2013/06/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2013/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2013/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2013/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2013/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2012 ](http://www.righto.com/2012/) (10)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2012/12/) (1)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2012/11/) (5)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2012/10/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2012/05/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2012/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2012/02/) (1)


  * [ ► ](javascript:void\(0\)) [ 2011 ](http://www.righto.com/2011/) (11)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2011/12/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2011/07/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2011/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2011/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2011/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2011/02/) (3)


  * [ ► ](javascript:void\(0\)) [ 2010 ](http://www.righto.com/2010/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2010/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2010/11/) (4)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2010/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2010/08/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2010/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2010/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2010/04/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2010/03/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2010/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2009 ](http://www.righto.com/2009/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2009/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2009/11/) (5)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2009/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2009/08/) (3)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2009/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2009/06/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2009/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2009/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2009/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2009/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2008 ](http://www.righto.com/2008/) (27)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2008/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2008/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2008/05/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2008/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2008/03/) (10)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2008/02/) (6)



## Don't miss a post!

Subscribe to get updates by email.




Subscribe

​

[Built with Kit](https://kit.com/features/forms?utm_campaign=poweredby&utm_content=form&utm_medium=referral&utm_source=dynamic)

|   
---|---  
  
Powered by [Blogger](https://www.blogger.com). 
