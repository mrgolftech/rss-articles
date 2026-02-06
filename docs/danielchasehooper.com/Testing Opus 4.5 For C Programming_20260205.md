# Testing Opus 4.5 For C Programming

**来源:** https://danielchasehooper.com
**链接:** https://danielchasehooper.com/posts/code-agents/
**日期:** Wed, 07 Jan 2026 00:00:00 +0000

---

[Daniel Hooper](https://danielchasehooper.com/)

[Home](https://danielchasehooper.com/) ・ [Articles](https://danielchasehooper.com/posts) ・ [Projects](https://danielchasehooper.com/#projects) ・ [About](https://danielchasehooper.com/about) ・ [X.com ](https://x.com/danielchooper)[Bluesky ](https://bsky.app/profile/danielchooper.bsky.social)[Mastodon](https://mastodon.gamedev.place/@danielchooper) [RSS](https://danielchasehooper.com/feed.xml)

# Testing Opus 4.5 For C Programming

January 7, 2026・6 minute read

I've been programming in C for 25 years and have net yet found AI useful for programming. I blew off the hype as "inexperienced glue coders". I'm not a luddite though, I use LLMs as a Google replacement; I even tried AI autocomplete in Cursor. Breaking my flow to read every autocomplete suggestion was annoying. However a new generation of "AI Code Agents" (Opus 4.5, and `gpt-5.2-codex high`) recently debuted that seemed worth a test.

In addition to the model improvements, code agents have 3 advantages over other AI-for-code approaches:

  1. They can read your entire codebase, unlike pasting code in chat
  2. They have shell access, meaning they can compile code, modify files, and use any command deemed necessary (Within the sandbox and limits you specify), unlike ai autocomplete
  3. They do their work independently while you work on something else, unlike chat or autocomplete



So I [installed Claude Code](https://code.claude.com/docs/en/quickstart), switched to Opus 4.5, and started an experiment…

## The Test

I used the Claude Code command line tool without any customization besides a Claude-generated `CLAUDE.md`. No secret prompt engineering voodoo. For each task I would:

  1. Write the prompt I would give an agent, _but not start it_
  2. Do the task by myself, measuring how long it took. I wrote the prompt before this step so that the understanding I gain from doing the work doesn't inadvertently improve the prompt and skew the experiment.
  3. Start the agent on the prompt in a separate copy of the project that doesn't contain my changes from the last step.
  4. Measure the time it takes me to review its work and edit up to satisfactory quality. I don't care how long the agent churns because that can happen in parallel while I do other work. I only care how much of my time this workflow consumes.
  5. Compare the times



What I found was that even after reviewing and editing the agent's code to my standards, AI assistance was usually a net time savings vs doing it by myself. One task involved writing a utf16 string type, writing utf16<->utf8 conversions, auditing all existing uses of strings, and reorganizing other affected types. That took me 4 hours. With AI assistance: 30 minutes. Straightforward but tedious, the ideal scenario for AI.

Outside the experiment, I felt like even when agent did a bad job, reading its changes acted as a shortcut to load the problem into my brain so I could do the work myself.

Regardless of how you feel about AI, I recommend trying this experiment for yourself.

## Lessons Learned

  1. Despite this generation of agents already being better than novice programmers, they're definitely still worse than great programmers. Mistakes range from organizing code poorly, to writing a brutally slow O(n²) algorithm when O(n) was not only possible, but simpler.

That said, it doesn't need to be perfect to be useful. It's best when treated like an intern or a lawyer's paralegal: you do big brain planning and give _specific_ instructions, it does tedium in background, you review, tweak, commit.

  2. Even though it doesn't write the best code when given free reign, it handles feedback well. I told it to rewrite the O(n²) algorithm to run in linear time, and it did. You need to already be a good programmer to know how the code could be improved. I will tolerate one round of feedback before cutting my losses and making the changes myself. Corrections were required less as I improved at giving direction and learned what tasks it could handle.

  3. It's useful for analysis. The time consuming part of many bugs is not writing the fix, but figuring out what went wrong. For example, I had one bug where adding 150,000+ items to a set was freezing the app for seconds at a time. The average number of probes per insert was enormous (set implemented with open addressing), so I thought it might be a cheap xor hash causing collisions. I tried other hash algorithms but they didn't help. On a whim I sent off Claude to look into it in parallel with me. It agreed with me: the xor hash function had a degenerate failure case with this data, but more importantly it noticed a recent change to the set allowed it to fill 100% before resizing, causing it to collapse into linear search of 150,000 items. I wrote the tiny fix myself and the freeze disappeared.

  4. Helped get over procrastination. Asking an agent to do a task I've been putting off made starting much easier. Best case: it completed the task. Worst case: it got me over the mental hump. I experienced this when I needed to create a linux sysroot for cross compilation. It found and downloaded the headers and static libraries.

  5. Running one or more agents in the background while I do other work feels like a superpower. This arrangement allows me to focus on doing what I do best while still achieving more per day. You can try this locally by making a copy of your project folder for each agent instance and having each one push to its own branch. Alternatively, you can use the web versions of these agents where they work in a Linux VM connected to your Github repo. One benefit of this approach is it never needs to ask for your permission to run a shell command.




## Dear Fellow Curmudgeons

I'd like to address sentiments that surfaced when I shared my experience with others:

> "If the AI writes the code then I won't understand my codebase."

First off, You should review everything it does.

Secondly, You dictate how you use it, so instead of prompts like "implement this whole feature, k thanks bye", do things like "replace the user array lookup with a hashmap and update all use sites". Don't use AI to replace your brain, use it to replace your keyboard.

I personally do not ask it to do any work that I don't know how to do myself. For unfamiliar territory, I use it like a research assistant: "what are my options?" "what are the trade-offs?" "link me to the research paper that introduced that approach"

> "But I _like_ programming, I don't want to be an AI manager"

Typing the code into the editor is the least interesting part of programming. AI assistance frees you to focus on the interesting parts: data and logic design, feature planning, optimization. You don't need to give up technical control like the vibecode kooks do. You probably like programming because you like making things, AI can help you make more.

> "If it's so productive where are all the AI-coded products?"

Not everyone wants to advertise "MADE BY AI", but there is already [stuff out there](https://mitchellh.com/writing/non-trivial-vibing) written with AI. "More products" is not the only way to realize productivity gains. It might be that a smaller team with AI is able to achieve the same amount as a large team without AI. Or more features can be developed within a fixed release cadence. Overall, this is a weak counter to claimed productivity gains.

## In summary

Current models are powerful but lack discernment, their greatest strength and greatest weakness is the same: they do what you tell them. They understand C, algorithms, and your existing code well enough that they can be useful if instructed clearly. While not perfect, I think code agents will be a part of my toolbox now.

### Read More

The examples in this article come from working on my [build visualizer](/posts/syscall-build-snooping)

I wrote about how to write [generic data structures in C](/posts/typechecked-generic-c-data-structures/)

My most popular article is "[Learn Shader Programming with Rick and Morty](/posts/code-animated-rick/)"

❖

Get notified about my next article:

Join Newsletter

[More articles by Daniel](https://danielchasehooper.com/)
