# Why not store the SAFEARRAY reference count as a hidden allocation next to the SAFEARRAY?

**来源:** [devblogs.microsoft.com/oldnewthing](https://devblogs.microsoft.com/oldnewthing/feed)
**发布时间:** Fri, 30 Jan 2026 15:00:00 +0000
**链接:** https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
When I described
how
Safe\xadArray\xadAdd\xadRef
keeps its reference count in a side table
, commenter Koro Unhallowed wondered
why we couldn’t store the reference count either before or after the formal
SAFEARRAY
structure
. Commenter Peter Cooper Jr. suspected that
there might be cases where applications assumed how much memory a
SAFEARRAY
occupied
.
\n
And indeed that is the case.
\n
Not all
SAFEARRAY
s are created by the
Safe\xadArray\xadCreate
function. I’ve seen code that declared and filled out their own
SAFEARRAY
structure. In those cases, the code allocates exactly
sizeof(SAFEARRAY)
bytes and doesn’t allocate any bonus data for the reference count.
\n
Indeed, there three flags
in the
fFeatures
member
for these “bring your own
SAFEARRAY
” structures.
\n
\n
\n
\n
FADF_AUTO
\n
An array that is allocated on the stack.
\n
\n
\n
FADF_STATIC
\n
An array that is statically allocated.
\n
\n
\n
FADF_EMBEDDED
\n
An array that is embedded in a structure.
\n
\n
\n
\n
These flag indicate that the array was not created by
Safe\xadArray\xadCreate
but rather was constructed manually by the caller in various ways.¹
\n
Note that if you pass a
SAFEARRAY
with one these flags to
Safe\xadArray\xadAdd\xadRef
, it will still increment the reference count, but you don’t get a data pointer back because the caller does not control the lifetime of the
SAFEARRAY
. The lifetime of the
SAFEARRAY
is controlled by the lifetime of the
SAFEARRAY
variable on the stack (
FADF_AUTO
), in the DLL’s global data segment (
FADF_STATIC
), or in the enclosing object (
FADF_EMBEDDED
).
\n
This means that our earlier suggestion to wrap the
SAFEARRAY
inside an in/out
VARIANT
runs into trouble if the
SAFEARRAY
is one of these types of arrays with externally-controlled lifetime. For those, you have no choice but to copy the data.
\n
¹ The documentation is, however, ambiguous about what “the array” refers to. Is it referring to the
SAFEARRAY
structure itself? Or is it referring to the data pointed to by the
pvData
member?
\n
The post
Why not store the <CODE>SAFEARRAY</CODE> reference count as a hidden allocation next to the <CODE>SAFEARRAY</CODE>?
appeared first on
The Old New Thing
.
'}

---

*抓取时间: 2026-02-05 13:04:37*
