# Letting Claude Play Text Adventures

**来源:** [borretti.me](https://borretti.me/feed)
**发布时间:** Mon, 12 Jan 2026 00:00:00 +0000
**链接:** https://borretti.me/article/letting-claude-play-text-adventures

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
The other day I went to an
AI hackathon
organized by my friends\n
Lucia
and
Malin
. The theme was
mech interp
, but I hardly\nknow PyTorch so I planned to do something at the API layer rather than the model\nlayer.
\n\n
Something I think about a lot is
cognitive architectures
(like\n
Soar
and
ACT-R
). This is like a continuation of
GOFAI
\nresearch, inspired by cognitive science. And like GOFAI it’s never yielded\nanything useful. But I often think: can we scaffold LLMs with cog arch-inspired\nharnesses to overcome their limitations?
\n\n
LLM agents like
Claude Code
are basically “accidental” cognitive\narchitectures: they are designed and built my practitioners rather than\ntheorists, but they have commonalities, they all need a way to manage memory,\ntool use, a task agenda etc. Maybe building an agent on a more “principled”\nfoundation, one informed by cognitive science, yields a higher-performing\narchitecture.
\n\n
So I sat around a while thinking how to adapt Soar’s architecture to an LLM\nagent. And I sketched something out, but then I thought: how can I prove this\nperforms better than baseline? I need an eval, a task.
\n\n
Math problems? Too one-shottable. A chatbot? Too interactive, I want something\nhands-off and long-horizon. A coding agent? That’s too freeform and requires too\nmuch tool use. And then I thought:
text adventures
! You have a stylized,\nhierarchically-structured world accessible entirely tthrough text, long-term\ngoals, puzzles, physical exploration and discovery of the environment. Even the\ndata model of text adventures resembles
frame-based
knowledge\nrepresentation systems. And there’s a
vast collection
of games available\nonline.
\n\n
Anchorhead
, which I played years ago, is a Lovecraft-inspired text\nadventure by Michael S. Gentry. It takes on the order of hundrds of turns to win\nacross multiple in-game days. And the game world is huge and very open. In other\nwords: a perfect long-horizon task.
\n\n
So I started hacking. The
frotz
interpreter runs on the command line and has a\n“dumb” interface called
dfrotz
, which takes the ncurses fluff out, and gives\nyou a very stripped command-line experience. It looks like this:
\n\n
\n
\n
$ dfrotz games/anchor.z8\n...\n Outside the Real Estate Office                      day one\n\nANCHORHEAD\nAn interactive gothic by Michael S. Gentry\n\n(Type HELP or ABOUT for some useful information.)\n\nRelease 5 / Serial number 990206 / Inform v6.15 Library 6/7\n\nOutside the Real Estate Office\nA grim little cul-de-sac, tucked away in a corner of the claustrophobic tangle\nof narrow, twisting avenues that largely constitute the older portion of\nAnchorhead. Like most of the streets in this city, it is ancient, shadowy, and\nleads essentially nowhere. The lane ends here at the real estate agent\'s office,\nwhich lies to the east, and winds its way back toward the center of town to the\nwest. A narrow, garbage-choked alley opens to the southeast.\n\n>go southeast\n Alley                                               day one\n\nAlley\nThis narrow aperture between two buildings is nearly blocked with piles of\nrotting cardboard boxes and overstuffed garbage cans. Ugly, half-crumbling brick\nwalls to either side totter oppressively over you. The alley ends here at a\ntall, wooden fence.\n\nHigh up on the wall of the northern building there is a narrow, transom-style\nwindow.\n
\n
\n
\n\n
It is easy to write a little Python wrapper to drive the interpreter through\n
stdin
and
stdout
:
\n\n
\n
\n
class
Interpreter
:
\n
"""Manages the dfrotz Z-machine interpreter process."""
\n\n
p
:
Popen
\n\n
def
__init__
(
self
):
\n
log
(
"Starting dfrotz."
)
\n
p
:
Popen
=
Popen
(
\n
[
"dfrotz"
,
"-m"
,
GAME
],
\n
stdin
=
PIPE
,
\n
stdout
=
PIPE
,
\n
stderr
=
PIPE
,
\n
)
\n
log
(
f
"Started dfrotz with PID=
{
p
.
pid
}
."
)
\n
# Set stdout/stderr to non-blocking mode.\n
for
stream
in
[
p
.
stdout
,
p
.
stderr
]:
\n
assert
stream
is
not
None
\n
fd
=
stream
.
fileno
()
\n
flags
=
fcntl
.
fcntl
(
fd
,
fcntl
.
F_GETFL
)
\n
fcntl
.
fcntl
(
fd
,
fcntl
.
F_SETFL
,
flags
|
os
.
O_NONBLOCK
)
\n
self
.
p
=
p
\n\n
def
read
(
self
)
->
str
:
\n
assert
self
.
p
.
stdout
is
not
None
\n
b
:
bytes
|
None
=
self
.
p
.
stdout
.
read
()
\n
if
b
is
not
None
:
\n
t
:
str
=
b
.
decode
(
"utf-8"
)
\n
return
t
\n
else
:
\n
return
""
\n\n
def
write
(
self
,
t
:
str
)
->
None
:
\n
assert
self
.
p
.
stdin
is
not
None
\n
self
.
p
.
stdin
.
write
(
t
.
encode
(
"utf-8"
))
\n
self
.
p
.
stdin
.
flush
()
\n
# Give the interpreter time to respond. Not ideal!\n
time
.
sleep
(
0.1
)
\n
\n
\n
\n\n
Now we can play the game from Python: send commands, get game output. Now we\nneed the dual of this: a player.
\n\n
\n
\n
class
Player
(
ABC
):
\n
"""\n    Interface for game-playing agents.\n    """
\n\n
@
abstractmethod
\n
def
cycle
(
self
,
text
:
str
)
->
str
:
\n
"""\n        Send the game\'s output to the agent, and return the next command to execute.\n        """
\n
pass
\n
\n
\n
\n\n
The Trivial Harness
\n\n
The trivial harness is basically nothing at all: treat the LLM/game interaction\nlike a chat history. The LLM reads the game output from the interpreter, writes\nsome reasoning tokens, and writes a command that is sent via
stdin
to the\ninterpreter.
\n\n
\n
\n
SYSTEM_PROMPT
:
str
=
"""\nHello Claude. Your task is to play an adventure game. I\'ve hooked up\nyour output to the dfrotz (dumb frotz) interpreter.\n\nThe structure of your output is fairly freeform. The first line that\nstarts with `>` (and only the first line!) is interpreted as a game\ncommand, everything else is uninterpreted commentary, e.g. you may\nwrite:\n\n    We should go north to explore the church.\n\n    >go north\n\n    Maybe we can use the silver key there.\n\nIf you write multiple `>` lines in one response, all but the first\nwill be ignored.\n\nHave fun! 😊\n"""
\n\n\n
class
SimplePlayer
(
Player
):
\n
"""\n    The simplest game-playing agent: keep the entire game histoyr in-context.\n    """
\n\n
client
:
Anthropic
\n
history
:
list
[
tuple
[
EntryType
,
str
]]
\n\n
def
__init__
(
self
):
\n
self
.
client
=
Anthropic
()
\n
self
.
history
=
[]
\n\n
def
cycle
(
self
,
text
:
str
)
->
str
:
\n
self
.
history
.
append
((
EntryType
.
GAME
,
text
))
\n
system
=
trim
(
SYSTEM_PROMPT
)
\n
messages
:
list
[
MessageParam
]
=
[]
\n
for
entry_type
,
entry_text
in
self
.
history
:
\n
role
:
str
\n
match
entry_type
:
\n
case
EntryType
.
GAME
:
\n
role
=
"user"
\n
case
EntryType
.
COMMAND
:
\n
role
=
"assistant"
\n
messages
.
append
(
\n
{
\n
"role"
:
role
,
\n
"content"
:
entry_text
,
\n
}
\n
)
\n
message
:
Message
=
self
.
client
.
messages
.
create
(
\n
max_tokens
=
512
,
\n
model
=
MODEL
,
\n
system
=
system
,
\n
messages
=
messages
,
\n
)
\n
log
(
f
"Tokens:
{
message
.
usage
.
input_tokens
}
"
)
\n
response
:
str
=
message
.
content
[
0
].
text
\n
log_claude
(
response
)
\n
lines
:
list
[
str
]
=
[
line
for
line
in
response
.
split
(
"
\\n
"
)
if
line
]
\n
cmd
:
str
=
[
line
for
line
in
lines
if
line
.
startswith
(
">"
)][
0
][
1
:]
\n
self
.
history
.
append
((
EntryType
.
COMMAND
,
response
))
\n
return
cmd
\n
\n
\n
\n\n
And this works well enough. Haiku 4.5 would mostly wander around the game map,\nbut Sonnet 4.5 and Opus 4.5 manage to solve the game’s first puzzle—breaking\ninto the real estate office, and finding the keys to the mansion—readily\nenough. It takes about ~200 turns for Claude to get to the second in-game day.
\n\n
The way I thought this would fail is: attention gets smeared across the long\ncontext, the model gets confused about the geometry of the world, its goal and\ntask state, and starts confabulating, going in circles, etc.
\n\n
As usual, I was outsmarting myself. The reason this fails is you run out of\ncredits. By the time you get to day two, each turn costs tens of thousands of\ninput tokens. No good! We need a way to save money.
\n\n
Memory
\n\n
Ok, let’s try something that’s easier on my Claude credits. We’ll show Claude\nthe most recent five turns (this is the perceptual working memory), and give it\na simple semantic memory: a list of strings that it can append entries to, and\nremove entries from using tool use.
\n\n
This keeps the token usage down:
\n\n
\n\n
The problem is the narrow time horizon. With the trivial harness, Claude can\nbreak into the real estate office in ~10 turns, and does so right at the start\nof the game. With this new harness, Claude wanders about the town, taking\ncopious notes, before returning to the real estate office, and it spends ~40\nturns fumbling around with the garbage cans before managing to break into the\nreal estate office.
\n\n
The next step, after getting the keys to the house, is to meet your husband\nMichael at the University and head home. Claude with the trivial harness takes\nabout ~100 turns to find the house, with some tangential wandering about the\ntown, and reaches day two around turn 150.
\n\n
Claude, with the memory harness, took ~250 turns just to get the keys to the\nhouse. And then it spends hundreds of turns just wandering in circles around the\ntown, accumulating redundant memories, and hits the turn limit before even\nfinding the house.
\n\n
Aside: Small Worlds
\n\n
Anchorhead
is a long, broad game, and from the very beginning you can forget\nthe plot and wander about most of the town. It takes a long time to see if a run\nwith an agent goes anywhere. So I thought: I need something smaller.
\n\n
Unsurprisingly, Claude can make its own games. The
Inform 7
package for\nNixOS was broken (though
Mikael
has
fixed this
recently) so I had\nto use
Inform 6
. I started with a trivial escape-the-room type game, which\nwas less than 100 lines of
.inf
code and any Claude could beat it less than 10\nturns. Then I asked for a larger, multi-room heist game.
\n\n
This one was more fun. It’s short enough that Claude can win with just the\ntrivial harness. I tried a different harness, where Claude has access to only\nthe last five turns of the game’s history, and a read-write memory\nscratchpad. And this one was interesting.
\n\n
First, because Claude only ever adds to its own memory, it never deletes\nmemories. I thought it would do more to trim and edit its scratchpad.
\n\n
Second, because Claude become fixated on this red-herring room: a garden with a\nwell. It kept going in circles, trying to tie a rope to the well and climb\ndown. Because of the limited game history, it only realized it was stuck when it\nsaw that the most recent ~20 entries it wrote to its memories related to various\nattempts to go down the well. Then I watched Claude walk away from the garden\nand solve the final puzzle, and hit the turn limit just two turns short of\nwinning.
\n\n
Tangent: I wonder if models are better at playing games created by other\ninstances of the same model, by noticing tiny correlations in the text to infer\nwhat puzzles and obstacles they would have written.
\n\n
In the end I abandoned the “small worlds” approach because the games are too\nstylized, linear, and uninteresting.
Anchorhead
is more unwieldy, but more\nnatural.
\n\n
Future Work
\n\n
I have a bunch of ideas I want to test, to better learn how harness\nimplementations affect performance. But I’m short on time, so I’m cutting it\nhere and listing these as todos:
\n\n
\n
Domain-Specific Memories:
Claude’s notes are all jumbled with information\non tasks, locations, etc. It might be better to have separate memories: a todo\nlist, a memory of locations and their connections, etc. This is close to the\nSoar approach.
\n
Automatic Geography:
related to the above, the harness can inspect the\ngame output and build up a graph of rooms and their connections, and format it\nin the context. This saves Claude having to note those things manually using a\ntool.
\n
Manual Geography:
the automatic geography approach has a few\ndrawbacks. Without integration into the Z-machine interpreter, it requires\nsome work to implement (parsing the currente location from the
dfrotz
\noutput, keeping track of the command history to find standard travel commands\ne.g.
go south
) but isn’t 100% deterministic, so that mazes and dynamic rooms\n(e.g. elevators) will confuse the system. So, instead of doing it manually, we\ncould give Claude a tool like
link(room, direction, other_room)
.
\n
Episodic Memory:
this feels like cheating, but, at the end of a run, you\ncan show Claude the session transcript and ask it to summarize: what it\naccomplished and how, where it failed and why. Including a short walkthrough\nfor how to get to the “last successful state”. This allows future runs to save\ntime in getting up to speed.
\n
\n\n
Code
\n\n
The repository is
here
.
'}

---

*抓取时间: 2026-02-05 12:56:50*
