# How Michael Abrash doubled Quake framerate

**来源:** [fabiensanglard.net](https://fabiensanglard.net)
**发布时间:** 14 Feb 2026 00:00:00 +0000
**链接:** https://fabiensanglard.net/quake_asm_optimizations/index.html

---

FABIEN SANGLARD'S WEBSITE
CONTACT
RSS
DONATE
Feb 14, 2026
How Michael Abrash doubled Quake framerate
With the 1999 release of the Quake source code, came a
readme.txt
written by John Carmack. There is a particular sentence in that text that piqued my curiosity.
Masm is also required to build the assembly language files.  It is possible to
change a #define and build with only C code, but the software rendering versions
lose almost
half its speed
.
Quake would be twice as fast thanks to its hand-crafted assembly? Let's find out if that is true, how it works, and what are the most important optimizations.
Establishing stock fps on my machine
Before doing anything with the source I needed to establish what was the framerate of the released version of
winquake.exe
on my Pentium MMX 233MHz.
C:\winquake> winquake.exe -wavonly +d_subdiv16 0 +timedemo demo1
I disabled
d_subdiv16
because it has no C implementation (that will make C vs ASM comparison impossible). This makes the engine fallback to D_DrawSpans8 instead of D_DrawSpans16 (perspective sampling every 8 pixels instead of 16).
-wav
is the fastest audio backend (also known as
"fastvid" option in wq.bat)
.
Stock winquake completed
timedemo demo1
at 42.3fps.
Building with ASM
Following the steps in
Let's compile like it's 1997!
, I built
winquake.exe
in release mode
with
the ASM optimizations. I really hoped VC++6 compiler did not get significant improvement
[1]
over VC++4 (the version id software used to ship winquake in 1997).
C:\winquake> WinQuake_ASM.exe -wavonly +d_subdiv16 0 +timedemo demo1
I was relieved to see
WinQuake_ASM.exe
run at nearly the same framerate, 42.2 fps. I was on a good track.
Building without ASM
As John Carmack mentioned, building without ASM only requires setting
id386
to
0
in
quakedef.h
.
That broke the linker because a VC6 project meant running on an Intel CPU at the time.
All I had to do was to add
nointel.c
to the project and I had a working executable.
Quake without ASM optimizations
With a successful release build, it was time to run
WinQuake_No_ASM.exe
.
C:\winquake> WinQuake_No_ASM.exe -wavonly +d_subdiv16 0 +timedemo demo1
Son of a BLiT! The game indeed runs at
22.7fps
instead of
42.2fps
! As John Carmack warned, Quake framerate is halved without Michael Abrash's optimizations!.
Diving into the assembly
There is a lot of assembly in Quake. In total, grep found 63 functions spread across 21 files.
$ find . -name "*.s" | wc -l
21
$ find . -name "*.s" -exec grep -H ".globl C(" {} \;
./server/worlda.s:.globl C(SV_HullPointContents)
./server/math.s:.globl C(BoxOnPlaneSide)
./client/d_copy.s:.globl C(VGA_UpdatePlanarScreen)
./client/d_copy.s:.globl C(VGA_UpdateLinearScreen)
./client/d_draw.s:.globl C(D_DrawSpans8)
./client/d_draw.s:.globl C(D_DrawZSpans)
./client/surf16.s:.globl C(R_Surf16Start)
./client/surf16.s:.globl C(R_DrawSurfaceBlock16)
./client/surf16.s:.globl C(R_Surf16End)
./client/surf16.s:.globl C(R_Surf16Patch)
./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/r_drawa.s:.globl C(R_ClipEdge)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients)
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle)
./client/d_polysa.s:.globl C(D_PolysetAff8Start)
./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)
./client/d_polysa.s:.globl C(D_PolysetAff8End)
./client/d_polysa.s:.globl C(D_Aff8Patch)
./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLeftEdge)
./client/d_polysa.s:.globl C(D_PolysetDrawFinalVerts)
./client/d_polysa.s:.globl C(D_DrawNonSubdiv)
./client/sys_wina.s:.globl C(MaskExceptions)
./client/sys_wina.s:.globl C(unmaskexceptions)
./client/sys_wina.s:.globl C(Sys_LowFPPrecision)
./client/sys_wina.s:.globl C(Sys_HighFPPrecision)
./client/sys_wina.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_wina.s:.globl C(Sys_PopFPCW)
./client/sys_wina.s:.globl C(Sys_SetFPCW)
./client/math.s:.globl C(Invert24To16)
./client/math.s:.globl C(TransformVector)
./client/math.s:.globl C(BoxOnPlaneSide)
./client/d_draw16.s:.globl C(D_DrawSpans16)
./client/r_aclipa.s:.globl C(R_Alias_clip_bottom)
./client/r_aclipa.s:.globl C(R_Alias_clip_top)
./client/r_aclipa.s:.globl C(R_Alias_clip_right)
./client/r_aclipa.s:.globl C(R_Alias_clip_left)
./client/snd_mixa.s:.globl C(SND_PaintChannelFrom8)
./client/snd_mixa.s:.globl C(Snd_WriteLinearBlastStereo16)
./client/r_aliasa.s:.globl C(R_AliasTransformAndProjectFinalVerts)
./client/d_spr8.s:.globl C(D_SpriteDrawSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeStart)
./client/r_edgea.s:.globl C(R_InsertNewEdges)
./client/r_edgea.s:.globl C(R_RemoveEdges)
./client/r_edgea.s:.globl C(R_StepActiveU)
./client/r_edgea.s:.globl C(R_GenerateSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeEnd)
./client/r_edgea.s:.globl C(R_SurfacePatch)
./client/surf8.s:.globl C(R_Surf8Start)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip0)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip1)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip2)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip3)
./client/surf8.s:.globl C(R_Surf8End)
./client/surf8.s:.globl C(R_Surf8Patch)
./client/sys_dosa.s:.globl C(MaskExceptions)
./client/sys_dosa.s:.globl C(unmaskexceptions)
./client/sys_dosa.s:.globl C(Sys_LowFPPrecision)
./client/sys_dosa.s:.globl C(Sys_HighFPPrecision)
./client/sys_dosa.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_dosa.s:.globl C(Sys_PopFPCW)
./client/sys_dosa.s:.globl C(Sys_SetFPCW)
As a comparison, DOOM has only two
.asm
files and three functions to speed up the engine.
A lot of these functions can be discarded from this study. Some do things that cannot be done in C like setting the floating-point unit precision or setting up the High-precision counter (
). Some are not used (
). Some are duplicated (one for server, one for client). Some optimizations use self-modifying code requiring markers so the
.text
region can be updated from
r
to
rw
and patched (
).
$ find . -name "*.s" -exec grep -H ".globl C(" {} \;
./server/worlda.s:.globl C(SV_HullPointContents)
./server/math.s:.globl C(BoxOnPlaneSide)
// Duplicate from ./client/math.s
./client/d_copy.s:.globl C(VGA_UpdatePlanarScreen)
// DOS
./client/d_copy.s:.globl C(VGA_UpdateLinearScreen)
// DOS
./client/d_draw.s:.globl C(D_DrawSpans8)
./client/d_draw.s:.globl C(D_DrawZSpans)
./client/surf16.s:.globl C(R_Surf16Start)
./client/surf16.s:.globl C(R_DrawSurfaceBlock16)
// Experimental 16-bit rendering
./client/surf16.s:.globl C(R_Surf16End)
./client/surf16.s:.globl C(R_Surf16Patch)
./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/r_drawa.s:.globl C(R_ClipEdge)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients)
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle)
./client/d_polysa.s:.globl C(D_PolysetAff8Start)
./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)
./client/d_polysa.s:.globl C(D_PolysetAff8End)
../client/d_polysa.s:.globl C(D_Aff8Patch)
./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLeftEdge)
./client/d_polysa.s:.globl C(D_PolysetDrawFinalVerts)
./client/d_polysa.s:.globl C(D_DrawNonSubdiv)
./client/sys_wina.s:.globl C(MaskExceptions)
./client/sys_wina.s:.globl C(unmaskexceptions)
./client/sys_wina.s:.globl C(Sys_LowFPPrecision)
./client/sys_wina.s:.globl C(Sys_HighFPPrecision)
./client/sys_wina.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_wina.s:.globl C(Sys_PopFPCW)
./client/sys_wina.s:.globl C(Sys_SetFPCW)
./client/math.s:.globl C(Invert24To16)
./client/math.s:.globl C(TransformVector)
./client/math.s:.globl C(BoxOnPlaneSide)
./client/d_draw16.s:.globl C(D_DrawSpans16)
./client/r_aclipa.s:.globl C(R_Alias_clip_bottom)
./client/r_aclipa.s:.globl C(R_Alias_clip_top)
./client/r_aclipa.s:.globl C(R_Alias_clip_right)
./client/r_aclipa.s:.globl C(R_Alias_clip_left)
./client/snd_mixa.s:.globl C(SND_PaintChannelFrom8)
./client/snd_mixa.s:.globl C(Snd_WriteLinearBlastStereo16)
./client/r_aliasa.s:.globl C(R_AliasTransformAndProjectFinalVerts)
./client/d_spr8.s:.globl C(D_SpriteDrawSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeStart)
./client/r_edgea.s:.globl C(R_InsertNewEdges)
./client/r_edgea.s:.globl C(R_RemoveEdges)
./client/r_edgea.s:.globl C(R_StepActiveU)
./client/r_edgea.s:.globl C(R_GenerateSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeEnd)
./client/r_edgea.s:.globl C(R_SurfacePatch)
./client/surf8.s:.globl C(R_Surf8Start)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip0)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip1)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip2)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip3)
./client/surf8.s:.globl C(R_Surf8End)
./client/surf8.s:.globl C(R_Surf8Patch)
./client/sys_dosa.s:.globl C(MaskExceptions)
./client/sys_dosa.s:.globl C(unmaskexceptions)
./client/sys_dosa.s:.globl C(Sys_LowFPPrecision)
./client/sys_dosa.s:.globl C(Sys_HighFPPrecision)
./client/sys_dosa.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_dosa.s:.globl C(Sys_PopFPCW)
./client/sys_dosa.s:.globl C(Sys_SetFPCW)
This still leaves 32 methods pertaining to math, sound, render, and draw. The distinction between R_ and D_ is not obvious. The R_ code is in charge of *what* to draw. The D_ code is in charge of *how* to draw it.
//******* DRAW *******
./client/d_spr8.s:.globl C(D_SpriteDrawSpans)            // Draw sprite facing camera
./client/d_draw.s:.globl C(D_DrawSpans8)                 // World draw  8 pixels persp
./client/d_draw.s:.globl C(D_DrawZSpans)                 // World write to Z-Buffer
./client/d_draw16.s:.globl C(D_DrawSpans16)              // World draw 16 pixels persp
./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients)     // All the polysets are for
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle) // alias models rendering.
./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)
./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLef

... (内容已截断)

---

*抓取时间: 2026-02-18 18:04:23*
