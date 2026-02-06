# The day Return became Enter

**来源:** [aresluna.org](https://aresluna.org)
**发布时间:** 
**链接:** https://aresluna.org/the-day-return-became-enter

---

The day Return became Enter
In the popular imagination, the transition from the world of typewriters to the universe of computers was orderly and simple: at some point in the 20th century, someone attached a CPU and a screen to a typewriter, and that turned it into a computer.
But the reality is much more fascinating and convoluted. The transition was meandering and lengthy, and traces of its many battles and decisions remain scattered across keyboards today. And no key might better represent the complexity of that journey than the
Return
key.
Return
and
Enter
keys on a AT&T keyboard, and a carriage return on a typewriter
An assembly line of typewriters under construction at the Underwood plant in 1962, with the carriage return levers clearly visible
Typewriters, born in the 1870s, did not understand information, and didn’t care about the meaning of their output.
Early models lacked
0
and
1
keys for cost cutting reasons. You were supposed to type a capital O or a lowercase l instead – they looked just about good enough. Teachers and tutorials encouraged you to overprint to create missing characters: type I on top of S to get a dollar sign, for example, or even reach for a pencil to fill in a missing part if overtyping wasn’t good enough. In theory, you could go even further: nothing prevented you from grabbing a typewritten page, putting it back upside down, and typing on top of what you wrote before.
This technique added to the repertoire of an art form known as “concrete poetry.”
In that universe, a carriage return – that distinctive lever on the left-hand side of each typewriter – was a kind of mechanical shorthand. It advanced the paper by a line or two, and returned the carriage to the left margin, winding it for the next line. You could carry out those two functions separately, but even early typewriter manufacturers realized the operation needed a better, joint interface.
An evolution of the carriage return lever: from 1901 to the 1950s
The carriage return lever was similar to all the other mechanical functions of the typewriter, starting as simple as humanly (and inhumanly) possible.
Tab
added a few spaces or mechanically zipped the carriage to the next predetermined point.
The
Shift
key moved the carriage up or the key basket down, applying its simple operation to every key equally.
Shift Lock
was a literal tooth holding
Shift
in place, placed right next to it for manufacturing convenience first, and ergonomics a distant second. It affected letters, digits, and punctuation in equal measure, in contrast to the later
Caps Lock
.
Improperly set up tabs could damage the typewriter as the entire energy of the line was released immediately. In later typewriters, a tab brake that remedied the problem became a standard feature.
A demonstration station for a Burroughs typewriter with an electric carriage return, 1936
Some of these special keys started as levers or even, like
Tab
, first-party or third-party additions bolted onto your typewriter. In time, all these functions migrated to the keyboard, making them easier to reach and more consistent in their operation. But carriage return remained the one holdover, too mechanically complex to follow in the other functions’ footsteps.
It was only when typewriters embraced electricity in the 1940s and 1950s that the carriage return completed its transformation into a key, and the distinctive lever could be detached.
The key was most often called
Carriage Return
or
Return
, as expected.
But since introducing electricity made the carriage return so much easier to operate,
it was no surprise that the industry that once brought you
Floating Shift
and
Magic Margin
keys also saw some typewriter manufacturers calling their keys
Electric Return
or even
Power Return
, like doors in your shiny new Detroit-made car.
The most popular electric typewriter in history, the IBM Selectric, called it “carrier return” in the user manual – the carriage was stationary, and the font ball was
carried
across it – but the keyboard itself went with a simple
Return
.
In the 1960s, an experiment estimated that switching to an electric typewriter made regular typing 18 times easier on average. Pressing the spacebar required only about half the work on an electric, since it was already pretty easy on a mechanical typewriter.
Backspace
needed 12 times less effort on an electric typewriter, and
Shift
9 times. But the introduction of the
Carriage Return
key was measured to be an astonishing 425 times easier on people’s fingers.
In an interesting reversal of the early days of carriage returns, cheaper models of Smith-Corona typewriters from the 1970s came with most functions electrified except for the carriage return, negative space for the key appearing on the keyboard, and the lever still attached in a typical space. Note one typewriter using the early Dvorak layout, including reordered digits.
But there were other keyboards that embraced electricity even earlier without bragging about it. Those were the keyboards of teletypes, taught to send text across wires (“teletype” derived from “teletypewriter,” or “remote typewriter”) at a constant speed of a little over 6 characters per second.
Teletypes formed pre-internet information networks, used by news agencies, postal offices, railroads, and other big companies and institutions. They were a successor to Morse code, abandoning its iconic single key that was pressed repeatedly to create streams of dihs and dahs. What replaced a Morse code lever was, at first, the five-key Baudôt keyboard, and then a standard typewriter-like QWERTY keyboard, the general public’s familiarity with which ensured less training was required.
Using a QWERTY keyboard meant the machines had to be tasked with encoding. Every key was assigned a number from 0 to 31. Space was zero, A was 3, B was 25, C was 14, and so on
– teletypes knew how to encode all of the characters being typed in, and how to decode them on the other side.
This was an approach later built on by ASCII in the 1960s (encoding 128 numbers) and Unicode in the 1990s (encoding 150
thousand
at the time of writing).
But for proper operation, it wasn’t just letters and digits that needed to be transmitted. Everything else – spaces, backspaces, jumping to a new line – also had to travel across the wire, to make sure the reconstructed message matched the input like a carbon copy would.
Those extra pieces of information were eventually named “control characters,” and assigned their own codes. But there was a problem. Typing a letter, moving back, and advancing paper took relatively little time. However, zipping the carriage from the right side of the page to the left was slower. That created a challenge: since teletypes communicated at a constant rate, the first letter arriving after a longer line could be smeared across the page, as the carriage return was still in progress.
Just as with early typewriters, any “smart” solution would be prohibitively complicated or expensive to make. But what if the character following a carriage return was guaranteed to be non-printing? This would give the teletype a chance to catch up. And so teletypes undid the early convenience of typewriters, and
Carriage Return
became decoupled from
Line Feed
. The former key moved the carriage to the left, but stayed on the same line. The latter advanced the paper to the next line, with no horizontal movement. Sometimes, the
Line Feed
code would arrive after a carriage return was complete. Other times, it would come in the middle of the carriage returning, but the teletype could deal with those movements coexisting.
This is the origin of the CR/LF debacle that’s still an occasional problem for today’s programmers.
The responsibility now rested on a typist to press these two keys every time, and in that particular order. This was a solution to a weird challenge that was both smart and dumb – and it was the first, but far from the last, complication around
Return
.
In another corner of the typing universe, the word-processing revolution was brewing.
Early word processors – back when that phrase meant hardware, not software – were nothing more than automated typewriters, teletypes without wires. But they focused on solving a slightly different issue: not one of exchange of information, but one of copying and rewriting.
The first word processors allowed people to “save” a page’s worth of keystrokes that could later be replayed. The letters were initially stored on hole-filled cards – not dissimilar to player pianos – and later captured onto magnetic media. The automatic repetition had two huge benefits: You could create carbon copies that were of the same quality, and you could also create personalized advertising letters, ones that looked as if they were typed just for the recipient.
After mastering that, the inventors of word processors moved on to the next, even bigger challenge. With typewriters, making a single typo or having a belated desire to change anything usually meant throwing out what one had typed so far and retyping the page from the beginning. But what if new technology allowed you to freely modify the saved text? Would it be possible to replace one word with another? Or delete a word? Or insert a sentence?
There were many, many problems to solve here: storage, logic, user interface. One of them? The naïve carriage return struggled to find its place in the world of word processing. What was necessary was
text reflow
: automatically adjusting the text and inserting carriage returns (or even hyphenating) whenever a word was about to go past the right margin. And then revisiting those breaks the moment anything was changed, inserted, or deleted.
This eventually led to the
Insert
key, originally used to switch between old-school, typewriter-like overtyping, and the new shiny method of inserting text as you typed. The key was designed to help with a specific transition, and then did something few keys do: it disappeared from most keyboar

... (内容已截断)

---

*抓取时间: 2026-02-06 06:02:54*
