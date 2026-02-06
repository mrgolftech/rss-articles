# Solving the NYTimes Pips puzzle with a constraint solver

**来源:** [righto.com](https://www.righto.com)
**发布时间:** 2025-10-18T08:41:00.000-07:00
**链接:** http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html

---

{'type': 'text/html', 'language': None, 'base': 'https://www.righto.com/feeds/posts/default', 'value': '
The New York Times recently introduced a new daily puzzle called
Pips
.\nYou place a set of dominoes on a grid, satisfying various conditions.\nFor instance, in the puzzle below,\nthe pips (dots) in the purple squares must sum to 8,\nthere must be fewer than 5 pips in the red square, and the pips in the three green squares must be equal.\n(It doesn\'t take much thought to solve this "easy" puzzle, but the "medium" and "hard" puzzles\nare more challenging.)
\n
The New York Times Pips puzzle from Oct 5, 2025 (easy). Hint: What value must go in the three green squares?
\n
I was wondering about how to solve these puzzles with a computer.\nRecently, I saw an article on
Hacker News
—"
Many hard LeetCode problems are easy constraint problems
"—that described the benefits and flexibility of a system called\na constraint solver.\nA constraint solver takes a set of constraints and finds solutions that satisfy the constraints: exactly\nwhat Pips requires.
\n
I figured that solving Pips with a constraint solver would be a good way to learn more about these\nsolvers, but I had several questions.\nDid constraint solvers require incomprehensible mathematics?\nHow hard was it to express a problem? Would the solver quickly solve the problem, or\nwould it get caught in an exponential search?
\n
It turns out that using a constraint solver was straightforward; it took me under two hours from\nknowing nothing about constraint solvers to solving the problem.\nThe solver found solutions in milliseconds (for the most part).\nHowever, there were a few bumps along the way.\nIn this blog post, I\'ll discuss my experience with the
MiniZinc
1
constraint\nmodeling system and show how it can solve Pips.
\n
Approaching the problem
\n
Writing a program for a constraint solver is very different from writing a regular program.\nInstead of telling the computer
how
to solve the problem, you tell it
what
you want:\nthe conditions that must be satisfied.\nThe solver then "magically" finds solutions that satisfy the problem.
\n
To solve the problem, I created an array called
pips
that holds the number of domino pips at each position\nin the grid.\nThen, the three constraints for the above problem can be expressed as follows.\nYou can see how the constraints directly express the conditions in the puzzle.
\n
\nconstraint pips[1,1] + pips[2,1] == 8;\nconstraint pips[2,3] < 5;\nconstraint all_equal([pips[3,1], pips[3,2], pips[3,3]]);\n
\n\n
Next, I needed to specify where dominoes could be placed for the puzzle.\nTo do this, I defined an array called
grid
that indicated the allowable positions: 1 indicates a valid\nposition and 0 indicates an invalid position. (If you compare with the puzzle at the top of the article,\nyou can see that the grid below matches its shape.)
\n
\ngrid = [|\n1,1,0|\n1,1,1|\n1,1,1|];\n
\n\n
I also defined the set of dominoes for the problem above, specifying the number of spots in each half:
\n
\nspots = [|5,1| 1,4| 4,2| 1,3|];\n
\n\n
So far, the constraints directly match the problem.\nHowever, I needed to write some more code to specify how these pieces interact.\nBut\nbefore I describe that code, I\'ll show a solution.\nI wasn\'t sure what to expect: would the constraint solver give me a solution or would it spin\nforever?\nIt turned out to find the unique solution in 109 milliseconds, printing out the\nsolution arrays.\nThe
pips
array shows the number of pips in each position, while the
dominogrid
array shows which\ndomino (1 through 4) is in each position.
\n
\npips = \n[| 4, 2, 0\n | 4, 5, 3\n | 1, 1, 1\n |];\ndominogrid = \n[| 3, 3, 0\n | 2, 1, 4\n | 2, 1, 4\n |];\n
\n\n
The text-based solution above is a bit ugly.\nBut it is easy to create graphical output.\nMiniZinc provides a JavaScript API, so you can easily display\nsolutions on a web page.\nI wrote a few lines of JavaScript to draw the solution, as shown below.\n(I just display the numbers since I was too lazy to draw the dots.)\nSolving this puzzle is not too impressive—it\'s an "easy" puzzle after all—but I\'ll show below that\nthe solver can also handle considerably more difficult puzzles.
\n
Graphical display of the solution.
\n
Details of the code
\n
While the above code specifies a particular puzzle, a bit more code is required to define\nhow dominoes and the grid interact.\nThis code may appear strange because it is implemented as constraints, rather than the\nprocedural operations in a normal program.
\n
My main design decision was how to specify the locations of dominoes.\nI considered assigning a grid position and orientation\nto each domino, but it seemed inconvenient to deal with multiple orientations.\nInstead, I decided to position each half of the domino independently, with an
x
and
y
coordinate in\nthe grid.
2
I added a constraint that the two halves of each domino had to be in neighboring cells,\nthat is, either the X or Y coordinates had to differ by 1.
\n
\nconstraint forall(i in DOMINO) (abs(x[i, 1] - x[i, 2]) + abs(y[i, 1] - y[i, 2]) == 1);\n
\n\n
It took a bit of thought to fill in the
pips
array with the number of spots on each domino.\nIn a normal programming language, one would loop over the dominoes and store the values into
pips
.\nHowever, here it is done with a constraint so the solver makes sure the values are assigned.\nSpecifically, for each half-domino, the
pips
array entry at\nthe domino\'s x/y coordinate must equal the corresponding
spots
on the domino:
\n
\nconstraint forall(i in DOMINO, j in HALF) (pips[y[i,j], x[i, j]] == spots[i, j]);\n
\n\n
I decided to add another array to keep track of which domino is in which position.\nThis array is useful to see the domino locations in the output, but it also\nkeeps dominoes from overlapping.\nI used a constraint to put each domino\'s number (1, 2, 3, etc.) into the occupied position of
dominogrid
:
\n
\nconstraint forall(i in DOMINO, j in HALF) (dominogrid[y[i,j], x[i, j]] == i);\n
\n\n
Next, how do we make sure that dominoes only go into positions allowed by
grid
?\nI used a constraint that a square in
dominogrid
must be empty or the corresponding
grid
must allow a domino.
3
\nThis uses the "or" condition, which is expressed as
\\/
, an unusual stylistic\nchoice. (Likewise, "and" is expressed as
/\\
. These correspond to the logical symbols\n∨ and ∧.)
\n
\nconstraint forall(i in 1..H, j in 1..W) (dominogrid[i, j] == 0 \\/ grid[i, j] != 0);\n
\n\n
Honestly, I was worried that I had too many arrays and the solver would end up in a rathole ensuring that the arrays were consistent.\nBut I figured I\'d try this brute-force approach and see if it worked.\nIt turns out that it worked for the most part, so I didn\'t need to do anything more clever.
\n
Finally, the program requires a few lines to define some constants and variables.\nThe constants below define the number of dominoes and the size of the grid for a particular problem:
\n
\nint: NDOMINO = 4; % Number of dominoes in the puzzle\nint: W = 3; % Width of the grid in this puzzle\nint: H = 3; % Height of the grid in this puzzle\n
\n\n
Next, datatypes are defined to specify the allowable values.\nThis is very important for the solver; it is a "finite domain" solver, so limiting the size of\nthe domains reduces the size of the problem.\nFor this problem, the values are integers in a particular range, called a
set
:
\n
\nset of int: DOMINO = 1..NDOMINO; % Dominoes are numbered 1 to NDOMINO\nset of int: HALF = 1..2; % The domino half is 1 or 2\nset of int: xcoord = 1..W; % Coordinate into the grid\nset of int: ycoord = 1..H;\n
\n\n
At last, I define the sizes and types of the various arrays that I use.\nOne very important syntax is
var
, which indicates variables that the solver must determine.\nNote that the first two arrays,
grid
and
spots
do not have
var
since they are constant,\ninitialized to specify the problem.
\n
\narray[1..H,1..W] of 0..1: grid; % The grid defining where dominoes can go\narray[DOMINO, HALF] of int: spots; % The number of spots on each half of each domino\narray[DOMINO, HALF] of var xcoord: x; % X coordinate of each domino half\narray[DOMINO, HALF] of var ycoord: y; % Y coordinate of each domino half\narray[1..H,1..W] of var 0..6: pips; % The number of pips (0 to 6) at each location.\narray[1..H,1..W] of var 0..NDOMINO: dominogrid; % The domino sequence number at each location\n
\n\n
You can find all the code on
GitHub
.\nOne weird thing is that because the code is not procedural, the lines can be in any order.\nYou can use arrays or constants before you use them.\nYou can even move
include
statements to the end of the file if you want!
\n
Complications
\n
Overall, the solver was much easier to use than I expected. However, there were a few complications.
\n
By changing a setting, the solver can find multiple solutions instead of stopping after the first.\nHowever, when I tried this, the solver generated thousands of meaningless solutions.\nA closer look showed that the problem was that the solver was putting arbitrary numbers into the "empty"\ncells, creating valid but pointlessly different solutions.\nIt turns out that I didn\'t explicitly forbid this, so the sneaky constraint solver went ahead and\ngenerated tons of solutions that I didn\'t want.\nAdding another constraint fixed the problem.\nThe moral is that even if you think your constraints are clear, solvers are very good at finding unwanted\nsolutions that technically satisfy the constraints.\n
4
\n
A second problem is that if you do something wrong, the solver simply says that the problem is\nunsatisfiable. Maybe there\'s a clever way of debugging, but I ended up removing constraints until\nthe problem can be satisfied, and then see what I did wrong with that constraint.\n(For instance, I got the array indices backward at one point, making the problem insoluble.)
\n
The most concerning issue is the unpredictability of the solver:\nmaybe it will take milliseconds or maybe it will take hours.\nFor instance, the Oct 5 hard Pips puzzle (below) caused the solver to take minutes for no apparent reason.\nHowever, the MiniZinc IDE supports different solver backends. I switched from the default
Gecode
solver to\n
Chuffed
, and it immediately found numerous solutions, 384 to\nbe precise.\n(Sometimes the Pips puzzles sometimes have multiple solutions, which players find
controversial
.)\nI suspect that the multiple solutions messed up the Gecode solver somehow, perhaps because\nit couldn\'t narrow down a "good" branch in the search tree.\nFor a benchmark of the different solvers, see the footnote.
5
\n
Two of the 384 solutions to the NYT Pips puzzle from Oct 5, 2025 (hard difficulty).
\n
How does a constraint solver work?
\n
If you were writing a program to solve Pips from scratch, you\'d probably have a loop to try\nassigning dominoes to positions.\nThe problem is that the problem grows exponentially. If you have 16 dominoes, there are 16 choices\nfor the first domino, 15 choices for the second, and so forth, so about 16! combinations in total,\nand that\'s ignoring orientations.\nYou can think of this as a search tree: at the first step, you have 16 branches. For the next step,\neach branch has 15 sub-branches. Each sub-branch has 14 sub-sub-branches, and so forth.
\n
An easy optimization is to check the constraints after each domino is added. For instance, as soon\nas the \n"less than 5" constraint is violated, you can
backtrack
and skip that entire\nsection of the tree.\nIn this way, only a subset of the tree needs to be searched; the number of branches will be large, but\nhopefully manageable.
\n
A constraint solver works similarly, but in a more abstract way.\nThe constraint solver assigns values to the variables, backtracking when a conflict is detected.\nSince the underlying problem is typically NP-complete, the solver uses heuristics to attempt to\nimprove performance.\nFor instance, variables can be assigned in different orders. The solver attempts to generate\nconflicts as soon as possible so large pieces of the search tree can be pruned sooner rather than later.\n(In the domino case, this corresponds to placing dominoes in places with the tightest constraints, rather\nthan scattering them around the puzzle in "easy" spots.)
\n
Another technique is constraint propagation. The idea is that you can derive new constraints and\ncatch conflicts earlier. For instance, suppose you have a problem with the constraints "a equals c" and "b equals c".\nIf you assign "a=1" and "b=2", you won\'t find a conflict until later, when you try to find a value for "c".\nBut with constraint propagation, you can derive a new constraint "a equals b", and the problem will\nturn up immediately.\n(Solvers handle more complicated constraint propagation, such as inequalities.)\nThe tradeoff is that generating new constraints takes time and makes the problem larger, so constraint\npropagation can make the solver slower. Thus, heuristics are used to decide when to apply constraint propagation.
\n
Researchers are actively developing new\nalgorithms, heuristics, and optimizations
6
such as backtracking more aggressively\n(called "backjumping"),\nkeeping track of failing variable assignments (called "nogoods"), and\nleveraging Boolean SAT (satisfiability) solvers.\nSolvers compete in
annual challenges
to test\nthese techniques against each other.\nThe nice thing about a constraint solver is that you don\'t need to know anything about these techniques;\nthey are applied automatically.
\n
Conclusions
\n
I hope this has convinced you that constraint solvers are interesting, not too scary, and can solve\nreal problems with little effort.\nEven as a beginner, I was able to get started with MiniZinc quickly.\n(I read half the
tutorial
and then jumped into programming.)
\n
One reason to look at constraint solvers is that they are a completely different programming paradigm.\nUsing a constraint solver is like programming on a higher level, not worrying about how the problem\ngets solved or what algorithm gets used.\nMoreover, analyzing a problem in terms of constraints is a different way of thinking about algorithms.\nSome of the time it\'s frustrating when you can\'t use familiar constructs such as loops and assignments,\nbut it expands your horizons.
\n
Finally,\nwriting code to solve Pips is more fun than solving the problems by hand, at least in my opinion,\nso give it a try!
\n
For more, follow me on\n Bluesky (
@righto.com
),\nMastodon (
@kenshirriff@oldbytes.space
),\n
RSS
, or subscribe
here
.
\n
Solution to the Pips puzzle, September 21, 2005 (hard). This puzzle has regions that must all be equal (=) and regions that must all be different (≠). Conveniently, MiniZinc has
all_equal
and
alldifferent
constraint functions.
\n
Notes and references
\n
\n
\n
\n
\nI started by downloading the
MiniZinc IDE
and reading the\n
MiniZinc tutorial
. The MiniZinc IDE is straightforward, with an editor window at the top and an output window at\nthe bottom. Clicking the "Run" button causes it to generate a solution.
\n
Screenshot of the MiniZinc IDE. Click for a larger view.
\n
↩
\n
\n
\n
It might be cleaner to combine the X and Y coordinates into a single
Point
type, using a MiniZinc
record type
.
↩
\n
\n
\n
I later decided that it made more sense to enforce that
dominogrid
is empty if and only if\n
grid
is 0 at that point, although it doesn\'t affect the solution.\nThis constraint uses the "if and only if" operator
<->
.
\n
\nconstraint forall(i in 1..H, j in 1..W) (dominogrid[i, j] == 0 <-> grid[i, j] == 0);\n
↩
\n
\n
\n
To prevent the solver from putting arbitrary numbers in the unused positions of
pips
, I added a\nconstraint to force these values to be zero:
\n
\nconstraint forall(i in 1..H, j in 1..W) (grid[i, j] == 0 -> pips[i, j] == 0);\n
\n
Generating multiple solutions had a second issue, which I expected: A symmetric domino can be\nplaced in two redundant ways.\nFor instance, a double-six domino can be flipped to produce a solution that is technically\ndifferent but looks the same. I fixed this by adding constraints for each symmetric domino\nto allow only one of the two redundant positions. The constraint below forces a preferred\norientation for symmetric dominoes.
\n
\nconstraint forall(i in DOMINO) (spots[i,1] != spots[i,2] \\/ x[i,1] > x[i,2] \\/ (x[i,1] == x[i,2] /\\ y[i,1] > y[i,2]));\n
\n
To enable multiple solutions in MiniZinc, the setting is under Show Configuration Editor > User Defined Behavior >\nSatisfaction Problems or the
--all
flag from the command line.
↩
\n
\n
\n
MiniZinc has five solvers that can solve this sort of integer problem:
Chuffed
,\n
OR Tools CP-SAT
,\n
Gecode
,\n
HiGHS
,\nand
Coin-OR BC
.\nI measured the performance of the five solvers against 20 different Pips puzzles.\nMost of the solvers found solutions in under a second, most of the time, but there is a lot\nof variation.
\n
Timings for different solvers on 20 Pip puzzles.
\n
Overall, Chuffed had the best performance on the puzzles that I tested, taking well under a second.\nGoogle\'s OR-Tools won all\nthe categories in the
2025 MiniZinc challenge
,\nbut it was considerably slower than Chuffed for my Pips programs.\nThe default Gecode solver performed very well most of the time, but it did terribly on a few\nproblems, taking over 15 minutes.\nHiGHs was slower in general, taking a few minutes on the hardest problems, but it didn\'t fail\nas badly as Gecode.\n(Curiously, Gecode and HiGHS sometimes found different problems to be difficult.)\nFinally, Coin-OR BC was uniformly bad; at best it took a few seconds, but one puzzle took almost two\nhours and others weren\'t solved before I gave up after two hours.\n(I left Coin-OR BC off the graph because it messed up the scale.)
\n
Don\'t treat these results too seriously because different solvers are optimized for\ndifferent purposes. (In particular, Coin-OR BC is designed for linear problems.)\nBut the results demonstrate the unpredictability of solvers: maybe you get a solution in a second\nand maybe you get a solution in hours.
↩
\n
\n
\n
If you want to read more about solvers,
Constraint Satisfaction Problems
is an overview presentation.\nThe Gecode algorithms are described in a nice technical report:
Constraint Programming Algorithms used in Gecode
.\nChuffed is more complicated: "Chuffed is a state of the art lazy clause solver designed from the ground up with lazy clause generation in mind. Lazy clause generation is a hybrid approach to constraint solving that combines features of finite domain propagation and Boolean satisfiability."\nThe Chuffed paper
Lazy clause generation reengineered
\nand
slides
are more of a challenge.\n
↩
\n
\n
\n
'}

---

*抓取时间: 2026-02-05 12:51:49*
