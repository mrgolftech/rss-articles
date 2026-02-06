# 1Password Dependency Breaks Syntax Highlighting

**来源:** [borretti.me](https://borretti.me/feed)
**发布时间:** Sat, 27 Dec 2025 01:00:00 +0000
**链接:** https://borretti.me/article/1password-dependency-breaks-syntax-highlighting

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
Earlier today I noticed the syntax highlighting on this website was broken. But\nnot fully: on reload I’d see a flash of highlighted text, that then turned\nmonochrome. The raw HTML from
curl
showed
rouge
tags, but the web inspector\nshowed raw text inside the
<code>
elements. This didn’t happen in Chromium.
\n\n
My first thought was: there’s malformed HTML, and Firefox is recovering in a way\nthat loses the DOM inside
<code>
tags. Then I noticed it doesn’t happen in\nincognito. Turning my extensions off one by one, I found that 1Password is\nresponsible. Others (
1
,
2
) have reported this also. If you\nextract the
latest XPI
, unzip it, and dig around, you’ll find they’re\nusing
Prism.js
, a JavaScript syntax highlighter.
\n\n
I don’t know why a password manager needs a syntax highlighter. I imagine it has\nto do with the app feature where, if you have an SSH key, you can open a
modal
\nthat tells you how to configure Git commit signing using. Maybe they want to\nhighlight the SSH configuration code block (which is unnecessary anyways, since\nyou could write that HTML by hand). But I can’t know for sure.
\n\n
Why write about this? Because 1Password is a security critical product, and they\nare apparently pulling random JavaScript dependencies and unwittingly running\nthem
in the tab context
, where the code has access to everything. This is\nno good. I don’t need to explain how bad a supply-chain attack on the 1Password\nbrowser extension would be.
\n\n
I like 1Password and I was sad when Apple
Sherlocked
them with the\n
Passwords
app, but this is a bad sign about their security practices.
'}

---

*抓取时间: 2026-02-05 12:56:53*
