# How can I prevent the user from changing the widths of ListView columns?

**来源:** [devblogs.microsoft.com/oldnewthing](https://devblogs.microsoft.com/oldnewthing/feed)
**发布时间:** Wed, 04 Feb 2026 15:00:00 +0000
**链接:** https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
Suppose you are using a Win32 ListView control in report mode, and you’ve got all your columns set up perfectly, and you don’t want the user to resize them. How do you do that?
\n
There is no ListView style for preventing column resize, but there
is
a header control style to prevent sizing:
HDS_NOSIZING
. This style requires Common Controls version 6, but I’m sure you’re all using that version already, right?
\n
auto hdr = ListView_GetHeader(hwndLV);\nSetWindowLong(hdr, GWL_STYLE,\n              GetWindowLong(hdr, GWL_STYLE) | HDS_NOSIZING);\n
\n
Whether the columns can be resized is independent of whether the columns can be rearranged, which you specify by setting the
LVS_EX_HEADER\xadDRAG\xadDROP
ListView extended style.
\n
ListView_SetExtendedListViewStyleEx(hwndLV,\n                                    LVS_EX_HEADERDRAGDROP,\n                                    LVS_EX_HEADERDRAGDROP);\n
\n
Okay, but what if you’re stuck in the dark ages with version 5 of the Common Controls? We’ll look at that next time.
\n
The post
How can I prevent the user from changing the widths of ListView columns?
appeared first on
The Old New Thing
.
'}

---

*抓取时间: 2026-02-05 13:04:33*
