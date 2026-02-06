# Splitting Machines

**来源:** https://tedium.co
**链接:** https://feed.tedium.co/link/15204/17251925/vmware-virtualization-history
**日期:** 

---

[](https://tedium.co/cdn-cgi/content?id=7PyAS6b5g4T9zhtmFbJiCuwHxhiww1OBU9LihKDxe0k-1770286708.9916224-1.0.1.1-nU.VEt6g1SuusqqBSNkSbGl9_0DB.W3TEU0SO1SKCe0)

###  [ ![Tedium.](/content/logo_v3.svg) ](/)

[ __  About ](/what-is-tedium) / [ __  Archives ](/archive) / [ __  Sponsor Us ](/advertising)

Search Tedium __

![Splitting Machines](https://proxy.tedium.co/QdmEISLR-o5c4q_lidlSKimG03Q=/smart/filters:quality\(50\):format\(jpeg\)/uploads/tedium011226.gif) ![Splitting Machines](https://proxy.tedium.co/4ZDr9TjL7OB7tNBKAF6x6UhfEfg=/filters:quality\(80\)/uploads/tedium011226.gif) [ « Previously … ](/2026/01/02/tedium-trends-2026/) __ Subscribe [ __Shuffle ](/2025/04/29/new-color-discovery-history/ "Direct Color") [__ Support Us On Ko-Fi](https://ko-fi.com/tedium) [ Nextly … » ](/2026/01/19/billboard-bubbling-under-hot-100-chart-history/)

##### Share This Post:

[ ![](https://static.tedium.co/uploads/share-openly.svg)  ShareOpenly ](https://shareopenly.org/share/?url=https%3A%2F%2Ftedium.co%2F2026%2F01%2F12%2Fvmware-virtualization-history&text=https%3A%2F%2Ftedium.co%2F2026%2F01%2F12%2Fvmware-virtualization-history%3A%20How%20the%20virtual%20machine%2C%20a%20foundational%20element%20of%20cloud%20computing%2C%20found%20its%20modern%20footing%20after%20a%20couple%20of%20scientists%20proved%20a%20couple%20of%20theorems%20wrong.) [ __ Share Well ](https://toot.kytta.dev/?text=Splitting%20Machines%3A%20How%20the%20virtual%20machine%2C%20a%20foundational%20element%20of%20cloud%20computing%2C%20found%20its%20modern%20footing%20after%20a%20couple%20of%20scientists%20proved%20a%20couple%20of%20theorems%20wrong.%0A%0Ahttps%3A%2F%2Ftedium.co%2F2026%2F01%2F12%2Fvmware-virtualization-history%0A%0A%28via%20%40tedium%40social%2Etedium%2Eco%29) [ __ Share Amazingly ](https://bsky.app/intent/compose?text=Splitting%20Machines%3A%20How%20the%20virtual%20machine%2C%20a%20foundational%20element%20of%20cloud%20computing%2C%20found%20its%20modern%20footing%20after%20a%20couple%20of%20scientists%20proved%20a%20couple%20of%20theorems%20wrong.%20https%3A%2F%2Ftedium.co%2F2026%2F01%2F12%2Fvmware-virtualization-history) [ __ Waste Pixels ](https://twitter.com/intent/tweet?url=https%3A%2F%2Ftedium.co%2F2026%2F01%2F12%2Fvmware-virtualization-history&via=readtedium&text=Splitting%20Machines)

# Splitting Machines

## How the virtual machine, a foundational element of cloud computing, found its modern footing after a couple of scientists proved a couple of theorems wrong.

By Ernie Smith • January 12, 2026

https://static.tedium.co/uploads/tedium011226.gif

[ #vmware ](/tag/vmware/) [ #virtualization ](/tag/virtualization/) [ #vmware workstation ](/tag/vmware-workstation/) [ #broadcom ](/tag/broadcom/) [ #parallels ](/tag/parallels/) [ #kvm ](/tag/kvm/) [ #xen ](/tag/xen/) [ #dynamic recompilation ](/tag/dynamic-recompilation/) [ #just-in-time compilation ](/tag/just-in-time-compilation/)

**Today in Tedium:** Is there a technology that is more taken for granted in modern computing than virtualization? It’s an essential part of so many parts of modern computing, including cloud infrastructure. One could draw a straight line between virtual machines, which found their footing on x86 at the turn of the 21st century, and the myriad server farms that pepper the landscape today. But it’s worth keeping in mind that it wasn’t a guarantee that this would ever happen. Intel had all but written off this concept from the server world—and seemed primed to move to a new generation of hardware that might have gotten them there. But a startup not only proved that virtualization was possible, but likely opened up a cloud-forward economy that didn’t previously exist. (It might have been a rare time when hardware was playing catch-up to software.) Today’s Tedium talks about everyone’s favorite concept, virtualization. _— Ernie @ Tedium_

> ### “For any conventional third generation computer, a virtual machine monitor may be constructed if the set of sensitive instructions for that computer is a subset of the set of privileged instructions.”

**— The first of three theorems** developed by UCLA’s Gerald Popek and Honeywell’s Robert Goldberg to determine whether virtualization was possible on a particular system architecture. [Their _Communications of the ACM_ piece](https://dl.acm.org/doi/epdf/10.1145/361011.361073), dating to 1974, proved to be something of a Moore’s Law for virtualization in the decades afterward, a dividing line to prove what was possible. The x86 line of processors, with its CISC-y nature, violated many of the basic tenets of these theorems.

![vmware-workstation-haiku.jpg](https://proxy.tedium.co/hiDFTX6SVca4Ms28MS-c_r5fF70=/800x722/filters:quality\(80\)/uploads/vmware-workstation-haiku.jpg)VMware Workstation, running a version of the BeOS-inspired operating system Haiku. This is sort of the traditional nerd use case for a virtual machine. ([John Drinkwater/Flickr](https://www.flickr.com/photos/johndrinkwater/100943772/))

### Why nobody thought x86 could do something as technically impressive as virtualization

In the 1970s, during the era of the mainframe, a concept came to light that seemed to speak to a future where software and hardware lived hand in hand: The hypervisor. A term coined by IBM that also stands for “virtual machine monitor,” it represented the idea of splitting up a computer into multiple parts that were theoretically separated from one another.

(Why “hypervisor”? Easy. The concept is essentially a reference to the supervisor above the supervisor. What, did you think it was something more futuristic than that?)

What might that look like? [A 1971 article](https://dl.acm.org/doi/pdf/10.1145/1478786.1478810) by IBM employee Gary Allred lays it out:

> The Hypervisor concept was relatively simple. It consisted of an addendum to the emulator program and a hardware modification on a Model 65 having a compatibility feature. The hardware modification divided the Model 65 into two partitions, each addressable from 0-n. The program addendum, having overlaid the system Program Status Words (PSW) with its own, became the interrupt handler for the entire system. After determining which partition had initiated the event causing the interrupt, control was transferred accordingly. The Hypervisor required dedicated I/O devices for each partition and, because of this, the I/O configurations were usually quite large, and, therefore, prohibitive to the majority of users.

So, unlike a modern virtual machine, it was effectively running two machines completely separated from one another, as if they weren’t connected.

During the mainframe era, a use case like this made sense, especially given that a [System/360 Model 65](https://www.computerhistory.org/revolution/mainframe-computers/7/161/565) was about the size of a vending machine.

But as we all know, computers kept getting smaller and smaller from there. First, bigger than a bread box, then smaller than a bread box, then about the size of a loaf of bread, and now about the size of bread. (Basically the bread box metaphor has been utterly destroyed by the smartphone.)

For a time, smaller computers meant smaller computing capabilities, no matter how fast the processors got. But that wasn’t necessarily the only factor at play.

![intel-386.jpg](https://proxy.tedium.co/AN_wMFde0XUFK30HTHsOKm96jrA=/800x601/filters:quality\(80\)/uploads/intel-386.jpg)It may look like a square wafer, but it’s really a series or rings. ([e-coli/Flickr](https://www.flickr.com/photos/e-coli/508518299/))

Going back to [our knowledge of RISC and CISC processors](https://tedium.co/2023/04/26/transmeta-crusoe-processor-history/), we know that x86 processors made by Intel and AMD tended to have a lot of instructions, which made processors overly complex. This turned out to be a problem when it came to Gerald Popek and Robert Goldberg’s set of theorems. Intel had designed the x86 chipset to run software with different levels of privilege, [set up in a series of “rings,”](https://manybutfinite.com/post/cpu-rings-privilege-and-protection/) with the goal of limiting the attack surface of the kernel.

This is good for having a secure system, but less good if your goal is to run a copy of Linux inside a copy of Windows 2000. And because the structure of this system limited access to the number of commands software could have access to, it meant you couldn’t virtualize it in quite the same way as IBM virtualized the System/360.

Sure, it was technically possible to _emulate_ a Linux machine on a Windows 2000 machine, but that introduced a lot of overhead. You were recreating hardware in software—likely the very same hardware that the system already had. This didn’t make any dang sense.

Intel wasn’t alone on this front—it was really a problem with every major platform of the time, casting a broad net—but given how broadly used it was, Intel was the poster child. The x86 processor set [violated](https://read.seas.harvard.edu/cs161/2018/lectures/lecture25/) the Popek-Goldberg theorems in more than a dozen distinct ways, which seemed like it might just make VMs infeasible with the infrastructure the world currently worked on.

![dynamic-recompilation-patent.jpg](https://proxy.tedium.co/i0_LIfa-voKFJ1jjBubbySChFwY=/603x804/filters:quality\(80\)/uploads/dynamic-recompilation-patent.jpg)A drawing from the patent filing for dynamic recompilation filed by Apple employee Eric Traut in the mid-1990s. Traut figured out how to make old Mac apps not suck on PowerPC. ([Google Patents](https://patents.google.com/patent/US5790825A/en))

There were some emerging suggestions it didn’t have to be this way, though. On the Mac side of things, Apple had pulled off something of a magic trick with its transition from 68000 to PowerPC by making a translation layer that more or less ran old code natively. At first, Apple used emulation, but later switched over to something called dynamic recompilation. ([This technique](https://patents.google.com/patent/US5790825A/en) was developed by Apple employee Eric Traut, who later worked on the famed PlayStation emulator [Connectix Virtual Game Station](https://aarongiles.com/programming/war-connectix/).) Put another way, the system was reprogramming the vintage code for MacOS to run in real time. It was so good that even in later PowerPC versions of the classic MacOS, much of the software was emulated 68k code. They didn’t need to update it, because it just worked.

Meanwhile, the Java programming language helped to popularize the concept of just-in-time compilation, which made it possible for a program to execute on a machine in real time without necessarily being tethered to its architecture. (Much of the discussion around VMs in computing magazines in the mid-’90s was [focused](https://books.google.com/books?id=3zsEAAAAMBAJ&pg=PA29) on [Java](https://books.google.com/books?id=-lc5G5n5mUsC&pg=PT52), partly for this reason.)

JIT is arguably one of the most important techniques in modern programming—[your web browser uses it heavily](https://hacks.mozilla.org/2017/02/a-crash-course-in-just-in-time-jit-compilers/) to speed up its use of JavasScript—and a key element of what makes modern virtualization tick.

JIT proved that it was possible to translate applications in real time. But translating entire operating systems? The x86 was too broken to allow for anything like that.

The result was that the hypervisor, a somewhat forgotten remnant of the mainframe that had yet to overcome the Popek-Goldberg theorems that sidelined modern computers, had yet to make its big return to the mainstream. But a computer science experiment run on a top-of-the-line SGI Origin 2000 server was about to change all that.

[![… You?](https://static.tedium.co/uploads/kofi_logo.png)](https://ko-fi.com/tedium)

##### [ Sponsored By … You? ](https://ko-fi.com/tedium)

**If you find weird or unusual topics** like this super-fascinating, the best way to tell us is to **[give us a nod on Ko-Fi](https://ko-fi.com/tedium)**. It helps ensure that we can keep this machine moving, support outside writers, and bring on the tools to support our writing. (Also it’s heartening when someone chips in.)

We accept advertising, too! [Check out this page to learn more](https://tedium.co/advertising/).

![960px-Zork-photo.jpg](https://proxy.tedium.co/8p4o26ZQAhR57Co3RbBMBkY1PC0=/960x1440/filters:quality\(80\)/uploads/960px-Zork-photo.jpg)Thanks to the VM that Zork uses, you could play this on an iPhone just as you can on a Kaypro II. ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Zork_photo.jpg))

### Five facts about virtualization you probably didn’t know

  1. **The command-line success of Zork was enabled by virtualization.** Infocom, the makers of the Zork series, developed a lightweight VM called [Z-machine](https://www.ifwiki.org/Z-machine) that effectively made the popular game easier to port to different devices. (This was an important strategy during this era, when computers were highly incompatible.) Rather than reprogramming the whole game on a new computer, the company developed a new compiler for each distinct system.
  2. **One of the most popular game emulators is really a VM.** [ScummVM](https://www.scummvm.org), a popular tool for running games developed with the LucasArts-built game engine SCUMM, works very similarly to Z-machine, albeit with far more modernized components and an attempt to compile all those games in a reasonably modern language. It often gets mistaken for an emulator despite the fact that VM is right in the name.
  3. **Hardware virtualization existed on the 386.** While not quite the same thing as the hardware virtualization we use today, x86 processors starting with the 386 included a “[virtual 8086 mode](https://www.pcmag.com/encyclopedia/term/virtual-8086-mode),” which made it possible for 386 processors to run legacy 8086 software in a specialized mode. Applications like Desqview and Windows 3.1 took advantage of this to offer multitasking to users. This was removed for x64 processors, then brought back when Intel and AMD released their versions of hardware-level virtualization.
  4. **You can run a GPU through a virtual machine.** Linux’s [kernel-based virtual machine](https://linux-kvm.org/page/Main_Page), or KVM, technique is something of a very advanced derivative of the 1970s IBM System/360 approach, making it possible to run a VM that can directly access external hardware. That includes very high-end GPUs, which get passed through. (I used it [to make a Hackintosh](https://tedium.co/2024/04/08/hackintosh-proxmox-vm-experience/) one time.)
  5. **Virtualization is a key technique for modernizing legacy embedded systems.** It’s kind of hard to take something like an airplane and put it out of service just because the software it uses is old. But what _is_ more possible is replacing the old hardware, which can be hard to repair, with more modern or modular components, but virtualizing the software on those newer systems. It’s a technique [common in aircraft](https://militaryembedded.com/avionics/computers/migrating-legacy-software-from-obsolete-hardware-to-modern-system-environments) and similarly difficult-to-replace industrial and aerospace equipment.



### 2006

**The year that Amazon[first released](https://aws.amazon.com/about-aws/whats-new/2006/08/24/announcing-amazon-elastic-compute-cloud-amazon-ec2---beta/)** its Elastic Compute Cloud (EC2) platform, which is arguably one of the most fundamental building blocks of modern cloud computing. While it didn’t use VMware’s technology, it reflected the way that VMware ultimately reshaped the computing landscape, it initially used the Xen hypervisor, which gained its superpowers thanks to virtualization hardware support. (Intel and AMD likely added that support to their processors largely in response to VMware.)

![sgi-origin-2000.jpg](https://proxy.tedium.co/nAqNLQWrlTPEkO_T6EdMIXNFIGI=/1000x1500/filters:quality\(80\)/uploads/sgi-origin-2000.jpg)An example of an SGI Origin 2000, like the one the founders of VMware used at Stanford. ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:SGI_Origin_2000_-_Silicon_Graphics_%2817175637009%29.jpg))

### Disco ball: The SGI-driven experiments that gave us VMware

If Backrub—the foundation of Google—was the most important research experiment happening at Stanford University in the mid-1990s, Disco—the foundation of VMware—was very much the second-most-important.

Built by PhD students Edouard Bugnion, Scott Devine, and faculty advisor Mendel Rosenblum, Disco was an attempt to solve the challenges that prevented virtual machines from living up to their full potential. In [_Disco: Running Commodity Operating Systems on Scalable Multiprocessors_](https://dl.acm.org/doi/epdf/10.1145/268998.266672), their research paper on this work, the team spoke of sharing resources between with the host computer. From the 1997 paper:

> Disco contains many features that reduce or eliminate the problems associated with traditional virtual machine monitors. Specifically, it minimizes the overhead of virtual machines and enhances the resource sharing between virtual machines running on the same system. Disco allows the operating systems running on different virtual machines to be coupled using standard distributed systems protocols such as NFS and TCP/IP. It also allows for efficient sharing of memory and disk resources between virtual machines. The sharing support allows Disco to maintain a global buffer cache transparently shared by all the virtual machines, even when the virtual machines communicate through standard distributed protocols.

That’s a big shift from requiring dedicated hardware for each separate machine as used in the System/360 days. But computing had the benefit of experiences like [remote desktops](https://tedium.co/2021/02/12/remote-desktop-access-history/) and emulators like SoftWindows and VirtualPC to show that we could virtualize the context and reuse the components.

![disco-paper.jpg](https://proxy.tedium.co/9z4ZQ8-qnbWlqRl78IvpXIGjsgM=/1238x925/filters:quality\(80\)/uploads/disco-paper.jpg)The HTML version of the paper, as immortalized on the Internet Archive.

A little more about the Disco experiment: It’s rooted in Rosenblum’s work on something called SimOS, a prior initiative which Rosenblum and other researchers built on IRIX to experiment with completely simulating a computing environment through software alone. It was a project designed to help the university design a processor of its own, Flash, but it proved key to building a virtual machine and a thin OS layer, called SlimOS, to manage everything.

(Why [Silicon Graphics](https://tedium.co/2018/10/04/sgi-collector-history/)? At the time, multi-core computer processors were fairly rare, and the SGI Origin 2000 was one of the few options on the market that could handle such a task. It likely gave them enough additional headroom to do more extreme testing.)

![disco_chart.jpg](https://proxy.tedium.co/wMLwHNzixM7XT0SDzKCmkD2RGNU=/802x777/filters:quality\(80\)/uploads/disco_chart.jpg)The discovery that using a hypervisor in combination with just-in-time compilation caused only a very small performance decline was a huge deal. It was arguably the basis of VMware’s whole business.

And the testing proved the model. The overhead was fairly modest given the performance, which meant that it would theoretically be possible to use hypervisors to split up a machine into multiple pieces, each of which controlled a different process.

And, famous last words, the paper ends like this:

> This return to virtual machine monitors is driven by a current trend in computer systems. While operating systems and application programs continue to grow in size and complexity, the ma-chine-level interface has remained fairly simple. Software written to operate at this level remains simple, yet provides the necessary compatibility to leverage the large existing body of operating systems and application programs. We are interested in further exploring the use of virtual machine monitors as a way of dealing with the increasing complexity of modem computer systems.

The paper created waves. Within a year of its creation, Bugnion, Devine, and Rosenblum would become three cofounders of VMware. Rosenblum’s wife Diane Greene, an engineer who at one point worked at SGI, would become the fourth.

Just two years after the paper’s release, VMware hit the ground running: After a year in stealth mode, VMware Workstation, a Disco adaptation for Windows and Linux, made a huge splash at the start of 1999. (One [early _InfoWorld_ article](https://books.google.com/books?id=51QEAAAAMBAJ&pg=PA25) featured a quote from a skeptical IT advisor. Little did they know that it would come to dominate their lives.)

Decades later, the researchers [created a follow-up paper](https://dl.acm.org/doi/epdf/10.1145/2382553.2382554) explaining their process for developing the original version of VMware workstation. The paper, which came years after the founders had left the company, explained that the x86’s convoluted instruction set and the diverse peripheral ecosystem created significant added complexities. (Yes, they knew that the theorems would make what they were trying to do difficult.)

But so too, did the operating systems, which they had to implement one at a time. Linux was easy. Windows was hard. OS/2 was impossible.

As the authors wrote, IBM’s failed attempt to compete with Microsoft was just too proprietary to be feasible:

> Although our VMM did not depend on any internal semantics or interfaces of its guest operating systems, it depended heavily on understanding the ways they configured the hardware. Case-in-point: we considered supporting OS/2, a legacy operating system from IBM. However, OS/2 made extensive use of many features of the x86 architecture that we never encountered with other guest operating systems. Furthermore, the way in which these features were used made it particularly hard to virtualize. Ultimately, although we invested a significant amount of time in OS/2-specific optimizations, we ended up abandoning the effort.

All that work to develop hardware drivers and manage edge cases—and even create some fake virtual hardware that only existed in software—took time, but it paid off in a big way. The self-funded company quickly found itself making $5 million in a matter of months.

_A user dives into the first version of VMware Workstation._

The software, at first, went relatively mainstream, given what it was. [In a 1999 profile with _USA Today_](https://www.newspapers.com/article/usa-today-vmware-profile-1999/188755646/), Greene (the company’s CEO) noted that the company was getting email from Buddhist monks who were fighting with one another over whether to run Linux on their computer or Windows. VMware allowed them to split the difference.

“When we first put together the business plan for VMware in 1998, we never thought Buddhist monks in Thailand would be part of our customer base,” Greene told the newspaper. “But it’s certainly intriguing to be this global.”

Of course, monks were only the start of it—if you follow VMware today, you are likely aware that Workstation is only a very small part of what that company became. VMs were highly usable in thousands of ways, as a mechanism for security and upkeep. (Want to put your custom intranet app on thousands of employee phones while still keeping it separate from those phones? Put it in a VM!)

Within a decade, Greene and Rosenblum had taken the company public, [then sold it for more than $600 million](https://www.cnet.com/tech/tech-industry/emc-acquires-server-specialist-vmware/). Two decades later, after a series of mergers and spinouts, it sold for a hundred times that. (More on that merger in a second.)

And this was largely before we had any of the niceties of the modern VM experience—or before VMware had much in the way of competition. Intel and AMD had not included native virtualization hardware on their chipsets until the mid-2000s. Meanwhile, Microsoft had to settle for [acquiring Connectix](https://news.microsoft.com/source/2003/02/19/microsoft-acquires-connectix-virtual-machine-technology/), the only real competitor in the virtualization space, in 2003.

Parallels, the most popular virtualization app on the Mac, didn’t emerge until 2006, while open-source virtualization standbys like Xen, QEMU, VirtualBox, and Proxmox didn’t start making themselves known until the mid-2000s.

Put another way, VMware had a multi-year head start to dominate the world of virtualization. And in many ways, that reflects why the company has been such a key part of the enterprise for so long.

I imagine this is kind of a spicy take, but I think VMware’s success probably played a factor in x86 sticking around, despite Intel attempting to build a new generation of chip on a different architecture, called Itanium. [Intel spent billions of dollars](https://www.cnet.com/tech/tech-industry/itanium-a-cautionary-tale/) trying to make fetch happen, only for one company to awkwardly “fetch” it: Hewlett-Packard.

After all, VMware essentially proved that with an innovative use of hypervisors, you could work around the pain points that made x86 a weak option for virtualization—and it didn’t even have to break Intel’s security model to do so! If the existing x86 architecture was this capable, why switch?

VMware’s big innovation might have been born on an SGI computer, but it really proved a saving grace for Moore’s law.

### 2011

**The year that Diebold,** a major manufacturer of ATMs (and yes, voting machines), announced “the world’s first virtualized ATM.” It was a prototype that ultimately separated the software of an ATM, which can be quite difficult to update in the field, from the hardware. The concept, [developed with VMware](https://www.prnewswire.com/news-releases/diebold-to-unveil-prototype-for-worlds-first-virtualized-atm-128584333.html), points at the way that VMs made embedded systems, especially based on outdated software, easier to manage. These days, we don’t necessarily run our ATMs on VMs, but the technique is highly popular for _testing_ ATM software.

**It’s worth noting that VMware,** despite its fundamental role in modern tech as a pivotal enterprise firm that literally created an entire product category, has seen better days. Over the last couple of years, it [was acquired by Broadcom](https://www.broadcom.com/info/vmware), a company that has aggressively reset the model to maximize profitability and move away from one-time licenses.

[As _CIO Dive_ put it](https://www.ciodive.com/news/broadcom-vmware-acquistion-vcf-private-cloud/733800/) in 2024:

> The transition marked a seismic shift in enterprise IT. Sure, generative AI has caused its fair share of disruption, but the technology has yet to scale. The acquisition of VMware, however, and the ensuing licensing changes has threatened to upend core infrastructure, disrupt critical business processes and wreak havoc on spending.

And just this past week, a very high-profile zero-day security exploit involving its EXSi software package [was exploited in the wild](https://www.bleepingcomputer.com/news/security/vmware-esxi-zero-days-likely-exploited-a-year-before-disclosure/).

VMware’s founders left nearly two decades ago, and upon Dell’s 2016 acquisition of the company, the entire team that worked on the flagship Workstation product was fired. (Which, honestly, suggests that Workstation isn’t where the real money is.)

Options for virtualization and separation of concerns abound. Whole empires have been made around tools like QEMU, and software like Docker and Podman have helped to make virtualized tools a part of many workflows.

Recently, Broadcam [began to offer VMware Workstation](https://www.techradar.com/pro/vmware-is-suddenly-offering-a-free-hypervisor-once-again), the program that started it all, for free. Broadcom’s messaging has been all over the place—previously, the company _removed_ free versions of the software. But at a time when you can virtualize operating systems on modern hardware in a couple dozen ways, Workstation (and its Mac counterpart, Fusion) are no longer groundbreaking.

Yes, VMware broke the ground, but many companies built on that foundation, and our modern digital economy is built on nesting dolls of virtual machines. Broadcom might as well turn the iconic tool, the one allowed monks to share a computer and Fortune 500 companies to modernize their aging hardware stacks, into a loss-leader.

VMware got acquired for over $60 billion for a reason. It reflects the inherent value of its original idea: We are better off with a few computers that run many machines simultaneously than many computers that only run a handful of tools.

But perhaps what the computing industry didn't anticipate was that virtualization just raised demand for computers in general.

\--

Find this one an interesting read? [Share it with a pal](https://tedium.co/2026/01/12/vmware-virtualization-history/)!

By the way, you know a machine that doesn’t need virtualization? Yep, that’s right, [la machine](https://la-machine.fr/?utm_source=newsletter&utm_medium=email&utm_campaign=tedium)! Be sure to check them out.

![Ernie Smith](https://proxy.tedium.co/4DURKSI2domRaY9WpcAvjrbLaZM=/150x150/smart/filters:quality\(80\)/uploads/ernie_crop.jpg) Your time was wasted by … [Ernie Smith](/author/ernie/) Ernie Smith is the editor of Tedium, and an active internet snarker. Between his many internet side projects, he finds time to hang out with his wife Cat, who's funnier than he is. [ __](https://writing.exchange/@ernie) [ __](https://bsky.app/profile/ernie.tedium.co) [ __](https://www.threads.net/@shortformernie) [ __](https://erniesmith.net/) [ __](/cdn-cgi/l/email-protection#f194839f9894b185949598849cdf929e) [ « A Number Of Surprising Importance ](/2026/01/02/tedium-trends-2026/) __ Subscribe [ They Were Robbed » ](/2026/01/19/billboard-bubbling-under-hot-100-chart-history/)

#### Subscribe to Tedium

### Get more bizarre takes in your inbox.

**This is a newsletter that existed before Substack.** (We even turned Substack down!) Our goal is to outlive it. But we will be unable to do so unless you put your email in this box and let us invade your inbox with these messages that we send when we feel like it. It's an important obligation. Are you up to the task? 

Shoryuken!

Tedium can email me random bits of errata and rants about salsa jars. I am signing up for this. 

  ![Tedium T Logo](https://static.tedium.co/uploads/t-logo_nobg_v3.svg) **Once upon a time,** there was an internet that was weird and fascinating and didn’t make you mad. For the past ten years, Tedium has tried to bring that internet back through a commitment to weirdness and a love for the obscure and offbeat. We are nominally a newsletter, but if you share our content on the web, we won’t be upset. But if you email us asking for a backlink, we’ll publicly scold you on social media using the most sarcastic possible language. Them’s the breaks.

  * [What is Tedium?](https://tedium.co/what-is-tedium)
  * [Support us on Patreon](https://www.patreon.com/tedium)
  * [Share your ideas!](https://tedium.co/contribute)
  * [Privacy Policy](https://tedium.co/privacy-policy)
  * [Advertise With Us](https://tedium.co/advertising)
  * [RSS feed](https://feed.tedium.co/)
  * [Ernie on Mastodon](https://writing.exchange/@ernie)



_**Disclosure:** From time to time, we may use affiliate links in our content—but only when it makes sense. Promise._

_**P.S.:** If you email me asking about doing a guest post or posting a backlink, you forfeit ownership of your site to me._

Proudly built using a combination of [Craft CMS](https://craftcms.com/), Eleventy, Tailwind, and general magic.

Copyright (C) 2015-2025 Tedium LLC. All rights reserved. [Please, try the fish](https://www.youtube.com/watch?v=hqi2Jy0UMiA).
