# Studying compiler error messages closely: Input file paths

**来源:** [devblogs.microsoft.com/oldnewthing](https://devblogs.microsoft.com/oldnewthing/feed)
**发布时间:** Mon, 02 Feb 2026 15:00:00 +0000
**链接:** https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
A colleague was working in a project that used a number of data files to configure how the program worked. They wanted one portion of the configuration file to be included only if a particular build flag was set. Let’s say that the configuration file is
C:\\repos\\contoso\\config\\Contoso.config
.
\n
<providers>\n    <!-- Widget version should be 1.0, or 2.0 if the useV2Widgets build flag is set -->\n    <provider name="Widget" version="1.0"/>\n\n    <!-- Gadget is needed only if the useV2Widgets build flag is set -->\n    <provider name="Gadget" version="1.0"/>\n\n    <!-- other providers that are used regardless of the build flags -->\n</providers>\n
\n
They were adding a build flag to convert the code base to use 2.0 widgets, but they wanted the default to be 1.0; only people who build with the special build flag should get 2.0 widgets. It so happens that 2.0 widgets depend on gadgets, so they also wanted to add a gadget provider, but again only conditionally based on the build flag.
\n
The configuration file itself doesn’t support conditionals. How can they get a configuration file to support conditionals when the file format does not support conditionals?
\n
I suggested that they
use a preprocessor
to take the marked-up configuration file and produce a filtered output file, which becomes the
actual
configuration file. Upon closer investigation, it appeared that they were not the first project to need conditionals in their configuration file, and another team had already written a generic XML preprocessor that supports conditional elements based on build flags, and that other team even included instructions on their project wiki on how to include a preprocessor pass to their build configuration. The updated configuration file looks something like this:
\n
<providers>\n    <provider name="Widget" version="1.0" condition="!useV2Widgets"/>\n    <provider name="Widget" version="2.0" condition="useV2Widgets"/>\n    <provider name="Gadget" version="1.0" condition="useV2Widgets"/>\n</providers>\n
\n
However, after following the instructions on the wiki to update the configuration file to use the
condition
attribute, and update the build process to send the file through the “conditional build flags” preprocessor, the was still a build error:
\n
Validation failure: C:\\repos\\contoso\\config\\Contoso.config(2): Invalid attribute \'condition\'\n
\n
The configuration validator was upset at the
condition
attribute, but when they compared their project to other projects that used the configuration preprocessor, those other projects used the
condition
attribute just fine.
\n
Look carefully at the error message. In particular, look at the path to the file that the validator is complaining about.
\n
The validator is complaining about the original
unprocessed
file.
\n
They went to the effort of sending the unprocessed file through the conditional build flags preprocessor to produce a processed file that has the correct provider list based on the build flags. But they forgot to use the results of that hard work: They were still using the old unprocessed file. It’s like taking a photograph, doing digital touch-ups, but then uploading the original version instead of the touched-up version.
\n
The fix was to update the project so that it consumed the processed file instead of the raw file.¹
\n
Bonus chatter
: To avoid this type of confusion, it is common to change the extension of the unprocessed file to emphasize that it needs to be preprocessed. That way, when you see an error in
Contoso.config
, you don’t have to spend the effort to figure out
which
Contoso.config
the error is about.
\n
In this case, they could rename the unprocessed file to
Contoso.preconfig
and have the processed output be
Contoso.config
. I choose this pattern because the validator may require that the file extension be
.config
.
\n
Another pattern would be to call the unprocessed version
Contoso-raw.config
and the processed version
Contoso.config
.
\n
If you don’t want to rename an existing file (say because you are worried about merge errors if your change collides with others who are also modifying that file), you could leave the unprocessed file as
Contoso.config
and call the processed file
Contoso-final.config
.²
\n
¹ The instructions on the wiki says “In your project file, change references from
yourfile.ext
to
$(OutputDirectory)\\yourfile.ext
‘ But in this case, the file was being used not by the project file but by a separate configuration tool. The team was too focused on reading the literal instructions without trying to understand why the instructions were saying the things that they did. In this case, the instructions were focused on consumption from the project file, since that was the use case of the team that wrote the tool originally. But if you understand what the steps are trying to accomplish, you should realize that the intention is to update the references to the old
yourfile.ext
in
every location
you want to consume the postprocessed version.³
\n
² I chose the suffix
-final
as a joking reference to the pattern of seeing files named
Document-Final-Final-Final 2-USETHISONE.docx
.
\n
³ I took the liberty of updating the wiki to clarify that you need to update
all
references to
yourfile.ext
. The references usually come from the project file, but they could be in other places, too, such as a call to
makepri.exe
.
\n
The post
Studying compiler error messages closely: Input file paths
appeared first on
The Old New Thing
.
'}

---

*抓取时间: 2026-02-05 13:04:36*
