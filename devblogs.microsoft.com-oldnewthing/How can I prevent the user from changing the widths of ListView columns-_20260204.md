# How can I prevent the user from changing the widths of ListView columns?

**来源:** [devblogs.microsoft.com/oldnewthing](https://devblogs.microsoft.com/oldnewthing)
**发布时间:** Wed, 04 Feb 2026 15:00:00 +0000
**链接:** https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037

---

{'type': 'text/html', 'language': None, 'base': 'https://devblogs.microsoft.com/oldnewthing/feed', 'value': '<p>Suppose you are using a Win32 ListView control in report mode, and you&#8217;ve got all your columns set up perfectly, and you don&#8217;t want the user to resize them. How do you do that?</p>\n<p>There is no ListView style for preventing column resize, but there <i>is</i> a header control style to prevent sizing: <code>HDS_NOSIZING</code>. This style requires Common Controls version 6, but I&#8217;m sure you&#8217;re all using that version already, right?</p>\n<pre>auto hdr = ListView_GetHeader(hwndLV);\nSetWindowLong(hdr, GWL_STYLE,\n              GetWindowLong(hdr, GWL_STYLE) | HDS_NOSIZING);\n</pre>\n<p>Whether the columns can be resized is independent of whether the columns can be rearranged, which you specify by setting the <code>LVS_EX_HEADER\xadDRAG\xadDROP</code> ListView extended style.</p>\n<pre>ListView_SetExtendedListViewStyleEx(hwndLV,\n                                    LVS_EX_HEADERDRAGDROP,\n                                    LVS_EX_HEADERDRAGDROP);\n</pre>\n<p>Okay, but what if you&#8217;re stuck in the dark ages with version 5 of the Common Controls? We&#8217;ll look at that next time.</p>\n<p>The post <a href="https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037">How can I prevent the user from changing the widths of ListView columns?</a> appeared first on <a href="https://devblogs.microsoft.com/oldnewthing">The Old New Thing</a>.</p>'}

---

*抓取时间: 2026-02-06 06:02:30*
