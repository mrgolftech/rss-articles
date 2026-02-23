# Red/green TDD

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-23T07:12:28+00:00
**链接:** https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/#atom-everything

---

<p><em><a href="https://simonwillison.net/guides/agentic-engineering-patterns/">Agentic Engineering Patterns</a> &gt;</em></p>
    <p>"<strong>Use red/green TDD</strong>" is a pleasingly succinct way to get better results out of a coding agent.</p>
<p>TDD stands for Test Driven Development. It's a programming style where you ensure every piece of code you write is accompanied by automated tests that demonstrate the code works.</p>
<p>The most disciplined form of TDD is test-first development. You write the automated tests first, confirm that they fail, then iterate on the implementation until the tests pass.</p>
<p>This turns out to be a <em>fantastic</em> fit for coding agents. A significant risk with coding agents is that they might write code that doesn't work, or build code that is unnecessary and never gets used, or both.</p>
<p>Test-first development helps protect against both of these common mistakes, and also ensures a robust automated test suite that protects against future regressions. As projects grow the chance that a new change might break an existing feature grows with them. A comprehensive test suite is by far the most effective way to keep those features working.</p>
<p>It's important to confirm that the tests fail before implementing the code to make them pass. If you skip that step you risk building a test that passes already, hence failing to exercise and confirm your new implementation.</p>
<p>That's what "red/green" means: the red phase watches the tests fail, then the green phase confirms that they now pass.</p>
<p>Every good model understands "red/green TDD" as a shorthand for the much longer "use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass".</p>
<p>Example prompt:</p>
<blockquote>
<p>Build a Python function to extract headers from a markdown string. Use red/green TDD.</p>
</blockquote>
<p>Here's what I got <a href="https://claude.ai/share/2b9b952a-149b-4864-afb0-46f59b90b458">from Claude</a> and <a href="https://chatgpt.com/share/699beb6f-adc8-8006-a706-6bbfdcdca538">from ChatGPT</a>. Normally I would use a coding agent like Claude Code or OpenAI Codex, but this example is simple enough that both Claude and ChatGPT can implement it using their default code environments.</p>
<p>I did have to append "Use your code environment" to the ChatGPT prompt. When I tried without that it wrote the code and tests without actually executing them.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/testing">testing</a>, <a href="https://simonwillison.net/tags/tdd">tdd</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a></p>

---

*抓取时间: 2026-02-23 18:06:44*
