# Flake Checks in Shell

**来源:** [entropicthoughts.com](https://entropicthoughts.com)
**发布时间:** Tue, 24 Feb 2026 00:00:00 +0100
**链接:** https://entropicthoughts.com/flake-checks-in-shell

---

tl;dr
: To use a shell script as a Nix flake check, turn it into a derivation
with
runCommand
. It must
Create a file named as suggested in the environment variable
$out
.
Print the desired “how to fix” information to
stdout
.
Exit with status code 1 if the check failed, otherwise 0.
These three steps are not strictly documented anywhere, but are all needed for a
shell script to work as a good flake check.
An English linter
We might work on a project where the build server runs linters, unit tests, etc.
through the
nix flake check
command. Let’s say we want to add a linting step
that ensures we have chosen the
us
English spelling of some common words. On
this web site, the build failure would look like:
error: builder for '/nix/store/4k4...mal-reject-uk-spelling.drv' failed with exit code 1;
last 5 log lines:
> Found suspected words with UK spelling.
> the-most-mario-colour-revisited: colour
> update-on-antarctic-sea-ice: grey
> using-withptr-from-inline-c-in-haskell: realise
> war-what-is-it-good-for: centre,neighbour
> when-is-counter-strike-player-good: colour,favourite
For full logs, run 'nix log /nix/store/4k4..mal-reject-uk-spelling.drv'.
We have a shell script that performs this linting. We can start out with
In[1]:
words
=
'analyse|apologise|catalogue|centre|cheque|colour|defence|favourite|flavour|grey|honour|licence|mum|neighbour|organise|pyjamas|realise|theatre|travelling|tyre'
grep -roP
'(?<=\W)('"$words"')(?=\W)'
.
\
| sort
\
| uniq
\
| perl -F: -lanE
'
if ($F[0] ne $fn) {
say ("$fn: " . join(",", @words)) if defined($fn);
$fn = $F[0] =~ s/\..*//r;
@words = ();
}
push @words, $F[1];'
and this is what we want to get into the
nix flake check
.
Converting to a derivation
There are some things we need to think about when we try to jam this into our
flake.nix
. First off, we need to convert it into a Nix derivation, since flake
checks are supposed to be derivations. As a reminder, a derivation is a recipe
for building something. We aren’t really interested in building anything, so we
are looking to create a derivation that has meaningless output, but whose build
process runs the linting script.
We could do it manually with
mkDerivation
as always, but easier in this case
is the
runCommand
helper function. When given a script, that will evaluate to
a derivation that runs the script during the build stage. The
runCommand
helper also takes a
buildInputs
argument, which lets us specify the
dependencies we need for the script. In our case, that’s just Perl, but it could
be anything.
When made into a derivation, the script can no longer rely on the literal
relative path
.
as input to
grep
, so we’ll interpolate the Nix path for the
source tree.
In[2]:
{
inputs.nixpkgs.url
=
"github:NixOS/nixpkgs/nixos-25.05"
;
outputs
= { self, nixpkgs }:
let
pkgs
= nixpkgs.legacyPackages.x86_64-linux;
in
{
checks.x86_64-linux
= {
avoidUkSpellings
=
pkgs.runCommand
"avoid-uk-spellings"
{
buildInputs
= [ pkgs.perl ];
}
''
words='analyse|apologise|catalogue|centre|cheque|colour|defence|favourite|flavour|grey|honour|licence|mum|neighbour|organise|pyjamas|realise|theatre|travelling|tyre'
grep -roP '(?<=\W)('"$words"')(?=\W)'
${
srcPath
}
\
| sort \
| uniq \
| perl -F: -lanE '
if ($F[0] ne $fn) {
say ("$fn: " . join(",", @words)) if defined($fn);
$fn = $F[0] =~ s/\..*//r;
@words = ();
}
push @words, $F[1];'
''
;
};
};
}
With this, however, the check will always fail, saying the “builder failed to
produce path for output”.
Producing output from the derivation
If we recall that
runCommand
is masquerading as a build step, we get a better
understanding of the problem. It needs to produce
some
sort of output. The
easiest thing we can do is redirect the output of the pipeline to the
Nix-provided variable
$out
.
In[3]:
pkgs.runCommand
"avoid-uk-spellings"
{
buildInputs
= [ pkgs.perl ];
}
''
# --------------->8-----
| perl -F: -lanE '
if ($F[0] ne $fn) {
say ("$fn: " . join(",", @words)) if defined($fn);
$fn = $F[0] =~ s/\..*//r;
@words = ();
}
push @words, $F[1];' > $out
''
;
But now we have a new problem: the check
passes
even when it should not.
Returning the proper error code
The way build steps signal failure to Nix is by exiting with a non-zero status
code. Since the
$out
file only contains something if there were words with a
uk
spelling, we can use the state of that file to determine whether to fail
the build or not.
To the end of the script, we add a line
In[4]:
[ -z
"$(cat $out)"
] || exit 1
which ensures that either the file
$out
is empty, or we fail the build. And
now, finally, this works.
Getting better build errors
However, it could be more helpful. When the build fails, all we get from Nix is
error:
builder for '/nix/store/dql...k4g-avoid-uk-spellings.drv'
failed with exit code 1
rather than what we hoped to get: neat suggestions for what we need to fix. This
is because now that we redirect the output of the script to
$out
we are no
longer logging it to
stdout
. We can fix that by replacing the output
redirection with a pipe to
tee
.
In[5]:
pkgs.runCommand
"avoid-uk-spellings"
{
buildInputs
= [ pkgs.perl ];
}
''
# --------------->8-----
| perl -F: -lanE '
if ($F[0] ne $fn) {
say ("$fn: " . join(",", @words)) if defined($fn);
$fn = $F[0] =~ s/\..*//r;
@words = ();
}
push @words, $F[1];' \
| tee $out
[ -z "$(cat $out)" ] || exit 1
''
;
The
tee
command takes input and both prints it out
and
writes it to a file.
After this, the check both works and produces helpful output. We took care of
the things that were needed:
Turn the script into a derivation that creates an unused output.
Exit the script with an error code on linting failure.
Make sure to print diagnostic messages to standard out.
We used the
runCommand
helper because it was convenient, but we could turn
literally anything into a check with the low-level
mkDerivation
.
Bonus: fixing up the grep output
At this point, we might be annoyed by a
grep
peculiarity: if its given an
absolute path, it will print the absolute path for the matches too. Our check
errors might look like
error: builder for '/nix/store/4k4...mal-reject-uk-spelling.drv' failed with exit code 1;
last 5 log lines:
> Found suspected words with UK spelling.
> /nix/store/p81biq2dvbmhg3har759y18di9ybgpmj-ivc2w2wwrrrksd69nqccm7fz1b5xv171-source/the-most-mario-colour-revisited: colour
> /nix/store/p81biq2dvbmhg3har759y18di9ybgpmj-ivc2w2wwrrrksd69nqccm7fz1b5xv171-source/update-on-antarctic-sea-ice: grey
> /nix/store/p81biq2dvbmhg3har759y18di9ybgpmj-ivc2w2wwrrrksd69nqccm7fz1b5xv171-source/using-withptr-from-inline-c-in-haskell: realise
> /nix/store/p81biq2dvbmhg3har759y18di9ybgpmj-ivc2w2wwrrrksd69nqccm7fz1b5xv171-source/war-what-is-it-good-for: centre,neighbour
> /nix/store/p81biq2dvbmhg3har759y18di9ybgpmj-ivc2w2wwrrrksd69nqccm7fz1b5xv171-source/when-is-counter-strike-player-good: colour,favourite
For full logs, run 'nix log /nix/store/4k4...mal-reject-uk-spelling.drv'.
and that’s rather difficult to get an overview of. This has nothing to do with
creating checks for Nix, but it might be fun to know how to deal with it anyway.
We’ll use
sed
to strip out the first bits of the path, but we cannot use the
typical
/
separators to the substitution command, because the path contains
those characters. Fortunately,
sed
lets us use any separator characters, so
we’ll pick one we’re fairly sure won’t be in the Nix store path for the source.
In[6]:
pkgs.runCommand
"avoid-uk-spellings"
{
buildInputs
= [ pkgs.perl ];
}
''
# --------------->8-----
| perl -F: -lanE '
if ($F[0] ne $fn) {
say ("$fn: " . join(",", @words)) if defined($fn);
$fn = $F[0] =~ s/\..*//r;
@words = ();
}
push @words, $F[1];' \
| sed 's!
${
./.
}
!!' \
| tee $out
[ -z "$(cat $out)" ] || exit 1
''
;

---

*抓取时间: 2026-02-25 00:06:49*
