# Using the Brother DS-640 Scanner on NixOS

**来源:** [borretti.me](https://borretti.me/feed)
**发布时间:** Sat, 27 Dec 2025 00:00:00 +0000
**链接:** https://borretti.me/article/using-the-brother-ds-640-scanner-on-nixos

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
The
DS-640
is a compact USB scanner from
Brother
. It was surprisingly hard to get it working on NixOS, so I wrote up my solution so others don’t have this problem. The bad news is you need Brother’s proprietary drivers to make this work.
\n\n
You need this configuration:
\n\n
\n
\n
# Enable SANE scanners.
\n
hardware
.
sane
.
enable
=
true
;
\n\n
# Add yourself to the scanner and printer groups.
\n
users
.
users
.
USERNAME
.
extraGroups
=
[
"scanner"
"lp"
];
\n\n
# Add support for Brother scanners.
\n
hardware
.
sane
.
brscan5
.
enable
=
true
;
\n
\n
\n
\n\n
After applying this you have to log out and in, or reboot, for the usergroup changes to apply.
\n\n
Note also
brscan5
: if you use
brscan4
(as I did initially), the scanner will kind of work, but it only scans the first third or so of every page.
\n\n
And if you want a GUI:
\n\n
\n
\n
# Install GNOME Document Scanner.
\n
home-manager
.
users
.
USERNAME
.
home
.
packages
=
with
pkgs
;
[
\n
simple-scan
\n
];
\n
\n
\n
\n\n
Now, make sure the scanner is there:
\n\n
\n
\n
$ scanimage --list-devices\ndevice `brother5:bus4;dev2\' is a Brother DS-640 USB scanner\n
\n
\n
\n\n
If you get
Brother *Unknown USB scanner
, you either have the wrong driver or (as I did, surprisingly) a faulty USB port. In which case move the scanner to another port.
scanimage --list-devices
should recognize the model number.
\n\n
The most basic test that should work: put a page in the scanner until it locks and run:
\n\n
\n
\n
$ scanimage --device="brother5:bus4;dev2" \\\n  --format=jpeg \\\n  --output-file=scan.jpg\n
\n
\n
\n\n
This will produce a (probably not very good) scan in
scan.jpg
. Now, we can improve things using the device-specific options, which you can check with this command:
\n\n
\n
\n
$ scanimage --all-options --device="brother5:bus4;dev2"\nAll options specific to device `brother5:bus4;dev2\':\n    --mode 24bit Color[Fast]|Black & White|True Gray|Gray[Error Diffusion] [24bit Color[Fast]]\n        Select the scan mode\n    --resolution 100|150|200|300|400|600|1200dpi [100]\n        Sets the resolution of the scanned image.\n    --source Automatic Document Feeder(left aligned) [Automatic Document Feeder(left aligned)]\n        Selects the scan source (such as a document-feeder).\n    --brightness -50..50% (in steps of 1) [inactive]\n        Controls the brightness of the acquired image.\n    --contrast -50..50% (in steps of 1) [inactive]\n        Controls the contrast of the acquired image.\n    --MultifeedDetection[=(yes|no)] [inactive]\n\n    --AutoDocumentSize[=(yes|no)] [no] [advanced]\n\n    --AutoDeskew[=(yes|no)] [no] [advanced]\n\n    --SkipBlankPage[=(yes|no)] [inactive]\n\n    --SkipBlankPageSensitivity 0..100% (in steps of 1) [inactive]\n\n    -l 0..215.9mm (in steps of 0.0999908) [0]\n        Top-left x position of scan area.\n    -t 0..355.6mm (in steps of 0.0999908) [0]\n        Top-left y position of scan area.\n    -x 0..215.9mm (in steps of 0.0999908) [215.88]\n        Width of scan-area.\n    -y 0..355.6mm (in steps of 0.0999908) [355.567]\n        Height of scan-area.\n
\n
\n
\n\n
Try this for a better scan:
\n\n
\n
\n
$ scanimage --device="brother5:bus4;dev2" \\\n  --AutoDeskew=yes \\\n  --AutoDocumentSize=yes \\\n  --resolution 300 \\\n  --format=jpeg \\\n  --output-file=scan.jpg\n
\n
\n
\n\n
Note that some of the flags are in
--key value
format and others
--key=value
, and if you mess it up you get a cryptic error message.
'}

---

*抓取时间: 2026-02-05 12:56:55*
