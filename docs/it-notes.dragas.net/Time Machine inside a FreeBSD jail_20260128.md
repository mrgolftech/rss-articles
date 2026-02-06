# Time Machine inside a FreeBSD jail

**来源:** https://it-notes.dragas.net
**链接:** https://it-notes.dragas.net/2026/01/28/time-machine-freebsd-jail/
**日期:** Wed, 28 Jan 2026 08:52:00 +0000

---

Skip to main content [Access Key: S]

**Notice:** This site works best with JavaScript enabled, but all content is accessible without it. Skip to main content

[IT Notes](https://it-notes.dragas.net)Open navigation menu

  * [Home](https://it-notes.dragas.net "Return to homepage")
  * [Archives](https://it-notes.dragas.net/archives/ "Browse post archives by date")
  * [Categories](https://it-notes.dragas.net/categories/ "Browse posts by category")
  * [Tags](https://it-notes.dragas.net/tags/ "Browse posts by tag")
  * [Series](https://it-notes.dragas.net/series/ "Series")
  * [Under The Hood](https://it-notes.dragas.net/under-the-hood/ "Under The Hood")
  * [Professional Services](https://it-notes.dragas.net/professional-services/ "Professional Services")
  * [About](https://it-notes.dragas.net/about-me/ "About")



Search articles and pages Enter keywords to search articles and pages Submit search

![Time Machine inside a FreeBSD jail - Featured image](https://unsplash.com/photos/W32yvc0JJjw/download?force=true&w=640)

# Time Machine inside a FreeBSD jail

FreeBSD

8 min read

28/01/2026 08:52:00 

by Stefano Marinelli

Categories: [ freebsd](https://it-notes.dragas.net/categories/freebsd/), [ timemachine](https://it-notes.dragas.net/categories/timemachine/), [ apple](https://it-notes.dragas.net/categories/apple/), [ backup](https://it-notes.dragas.net/categories/backup/), [ data](https://it-notes.dragas.net/categories/data/), [ zfs](https://it-notes.dragas.net/categories/zfs/), [ server](https://it-notes.dragas.net/categories/server/), [ tutorial](https://it-notes.dragas.net/categories/tutorial/), [ ownyourdata](https://it-notes.dragas.net/categories/ownyourdata/)

Tags: [freebsd](https://it-notes.dragas.net/tags/freebsd/), [timemachine](https://it-notes.dragas.net/tags/timemachine/), [apple](https://it-notes.dragas.net/tags/apple/), [backup](https://it-notes.dragas.net/tags/backup/), [data](https://it-notes.dragas.net/tags/data/), [zfs](https://it-notes.dragas.net/tags/zfs/), [server](https://it-notes.dragas.net/tags/server/), [tutorial](https://it-notes.dragas.net/tags/tutorial/), [ownyourdata](https://it-notes.dragas.net/tags/ownyourdata/)

Many of my clients do not use Microsoft systems on their desktops; they use Linux-based systems or, in some cases, FreeBSD. Many use Apple systems - macOS - and are generally satisfied with them. While I wash my hands of it when it comes to Microsoft systems (telling them they have to manage their desktops autonomously), I am often able to lend a hand with macOS. And one of the main requests they make is to manage the backups of their individual workstations.

macOS, thanks to its Unix base, offers good native tools. Time Machine is transparent and effective, allowing a certain freedom of management. APFS, Apple's current file system, supports snapshots, so the backup will be effectively made on a snapshot. It also supports multiple receiving devices, so you can even have a certain redundancy of the backup itself.

Having many FreeBSD servers, I am often asked to use their resources and storage. To build, in practice, a Time Machine inside one of the servers. And it is a simple and practical operation, quick and "painless". There are many guides, including the excellent one by [Benedict Reuschling](https://freebsdfoundation.org/our-work/journal/browser-based-edition/storage-and-filesystems/samba-based-time-machine-backups/) from which I took inspiration for this one, and I will describe the steps I usually follow to set it all up in just a few minutes.

I usually use [BastilleBSD](https://bastillebsd.org) to manage my jails, so the first step is to create a new jail dedicated to the purpose. Here you have to decide on the approach: I suggest using a VNET jail or an "inherit" jail - meaning one that attaches to the host's network stack. On one hand, the inherit approach is less secure but, as often happens, it depends on the complexity of the situation. If, for example, we are using a Raspberry PI dedicated to the purpose, there is no reason to complicate things with bridges, etc., but we can attach directly to the network card with a creation command like:
    
    
    bastille create tmjail 15.0-RELEASE inherit igb0
    

Where `igb0` is the network interface we want to attach to.

In case we want to attach to the interface but in the form of a bridge, we should use this syntax:
    
    
    bastille create -V tmjail 15.0-RELEASE 192.168.0.42/24 igb0
    

Or, if our server already has a bridge (in this case it's `bridge0`, but yours might be named differently):
    
    
    bastille create -B tmjail 15.0-RELEASE 192.168.0.42/24 bridge0
    

At this point, you can choose: do we want to keep the backups inside the jail or in a separate dataset - which can even be on another pool? In some cases, this can be extremely useful: often I have jails running on fast disks (SSD or NVMe) but abundant storage on slower devices. In this example, therefore, I will create an external dataset for the backups (directly from the host) and mount it in the jail. You could also delegate the entire management of the dataset to the jail, which is a different approach.

Let's create a space of 600 GB - already reserved - on the chosen pool. 600 GB is a small space, but it's ok for an example:
    
    
    zfs create -o quota=600G -o reservation=600G bigpool/tmdata
    

We can also create separate datasets inside for each user and assign a specific space:
    
    
    zfs create -o refquota=500g -o refreservation=500g bigpool/tmdata/stefano
    

We can enter the jail and install what we need, remembering also to create the "mountpoint" for the dataset we just created:
    
    
    bastille console tmjail 
    
    pkg install -y samba419
    mkdir /tmdata
    

Exit the jail and instruct Bastille to mount the dataset inside the jail every time it is launched:
    
    
    exit
    bastille mount tmjail /bigpool/tmdata /tmdata nullfs rw 0 0
    

Let's go back into the jail and start with the actual configuration. First, for each Time Machine user, we will create a system user. In my example, I will create the user "stefano", giving him `/var/empty` as the home directory - this will give an error since we created a Bastille thin jail, but it's not a problem. It happens because in a thin jail some system paths are read-only or not manageable as they are on a full base system, but the user is only needed for ownership and Samba login.
    
    
    root@tmjail:~ # adduser
    Username: stefano
    Full name: Stefano
    Uid (Leave empty for default):
    Login group [stefano]:
    Login group is stefano. Invite stefano into other groups? []:
    Login class [default]:
    Shell (sh csh tcsh nologin) [sh]: nologin
    Home directory [/home/stefano]: /var/empty
    Home directory permissions (Leave empty for default):
    Use password-based authentication? [yes]: no
    Lock out the account after creation? [no]:
    Username    : stefano
    Password    : <disabled>
    Full Name   : Stefano
    Uid         : 1001
    Class       :
    Groups      : stefano
    Home        : /var/empty
    Home Mode   :
    Shell       : /usr/sbin/nologin
    Locked      : no
    OK? (yes/no) [yes]: yes
    pw: chmod(var/empty): Operation not permitted
    pw: chown(var/empty): Operation not permitted
    adduser: INFO: Successfully added (stefano) to the user database.
    Add another user? (yes/no) [no]: no
    Goodbye!
    

Give the correct permissions to the user:
    
    
    # If you've not created specific datasets for the users, you'd better create their home directories now
    mkdir /tmdata/stefano
    chown -R stefano /tmdata/stefano/
    

Now we configure Samba for Time Machine. The file to create/modify is `/usr/local/etc/smb4.conf`:
    
    
    [global]
    workgroup = WORKGROUP
    security = user
    passdb backend = tdbsam
    fruit:aapl = yes
    fruit:model = MacSamba
    fruit:advertise_fullsync = true
    fruit:metadata = stream
    fruit:veto_appledouble = no
    fruit:nfs_aces = no
    fruit:wipe_intentionally_left_blank_rfork = yes
    fruit:delete_empty_adfiles = yes
    
    [TimeMachine]
    path = /tmdata/%U
    valid users = %U
    browseable = yes
    writeable = yes
    vfs objects = catia fruit streams_xattr zfsacl
    fruit:time machine = yes
    create mask = 0600
    directory mask = 0700
    

We have set up Time Machine to support all the necessary features of macOS and to show itself as "Time Machine". Having set `path = /tmdata/%U`, each user will only see their own path.

At this point, we create the Samba user (meaning the one we will have to type on macOS when we configure the Time Machine):
    
    
    smbpasswd -a stefano
    

The Time Machine is seen by macOS because it announces itself via mDNS on the network. This type of service is performed by Avahi, which we are now going to configure. Although not strictly necessary (we can always find the Time Machine by connecting directly to its IP and macOS will remember everything), seeing it announced will help other non-expert users and ourselves when we have to configure another Mac in the future.

Recent Samba releases won't need any specific avahi configuration, so we can skip this step.

We are now ready to enable everything.
    
    
    service dbus enable
    service dbus start
    service avahi-daemon enable
    service avahi-daemon start
    service samba_server enable
    service samba_server start
    

Et voilÃ . If everything went according to plan, the Time Machine will announce itself on your network (if you have different networks, remember to configure the mDNS proxy on your router) and you will be able to log in (with the smb user you created) and start your first backup.

I suggest encrypting the backups for maximum security and observing, from time to time, your Mac as it silently makes its backups to your trusted FreeBSD server.

### Tags:

[freebsd](https://it-notes.dragas.net/tags/freebsd/) [timemachine](https://it-notes.dragas.net/tags/timemachine/) [apple](https://it-notes.dragas.net/tags/apple/) [backup](https://it-notes.dragas.net/tags/backup/) [data](https://it-notes.dragas.net/tags/data/) [zfs](https://it-notes.dragas.net/tags/zfs/) [server](https://it-notes.dragas.net/tags/server/) [tutorial](https://it-notes.dragas.net/tags/tutorial/) [ownyourdata](https://it-notes.dragas.net/tags/ownyourdata/)

[Previous Post ->Installing Void Linux on ZFS with Hibernation Support](https://it-notes.dragas.net/2025/12/22/void-linux-zfs-hibernation-guide/)

### You may also like

## [How we are migrating (many of) our servers from Linux to FreeBSD - Part 2 - Backups and Disaster Recovery](https://it-notes.dragas.net/2022/05/30/how-we-are-migrating-many-of-our-servers-from-linux-to-freebsd-part-2/)

30/05/2022 03:03:52  by Stefano Marinelli

Some details on how we're performing backups and disaster recovery of the migrated servers.

[Read More](https://it-notes.dragas.net/2022/05/30/how-we-are-migrating-many-of-our-servers-from-linux-to-freebsd-part-2/)

## [How we are migrating (many of) our servers from Linux to FreeBSD - Part 3 - Proxmox to FreeBSD](https://it-notes.dragas.net/2023/03/14/how-we-are-migrating-many-of-our-servers-from-linux-to-freebsd-part-3/)

14/03/2023 13:00:00  by Stefano Marinelli

Part 3 of our migration series details the complex process of moving servers from Proxmox to FreeBSD, including overcoming challenges with old hardware, problematic LXC containers, and fine-tuning virtual machines for optimal performance on bhyve.

[Read More](https://it-notes.dragas.net/2023/03/14/how-we-are-migrating-many-of-our-servers-from-linux-to-freebsd-part-3/)

## [FreeBSD vs. SmartOS: Who's Faster for Jails, Zones, and bhyve VMs?](https://it-notes.dragas.net/2025/09/19/freebsd-vs-smartos-whos-faster-for-jails-zones-bhyve/)

19/09/2025 10:50:00  by Stefano Marinelli

Which virtualization host performs better? I put FreeBSD and SmartOS in a head-to-head showdown. The performance of Jails, Zones, and bhyve VMs surprised me, forcing a second round of tests on different hardware to find the real winner.

[Read More](https://it-notes.dragas.net/2025/09/19/freebsd-vs-smartos-whos-faster-for-jails-zones-bhyve/)

### About

Scattered IT Notes - by Stefano Marinelli

[![EuroBSDCon 2025](https://it-notes.dragas.net/banner_zagreb.png)](https://2025.eurobsdcon.org/)

EuroBSDCon 2025 - Zagreb, Croatia; September 25-28, 2025.

### Categories

  * [server](https://it-notes.dragas.net/categories/server/)
  * [freebsd](https://it-notes.dragas.net/categories/freebsd/)
  * [hosting](https://it-notes.dragas.net/categories/hosting/)
  * [ownyourdata](https://it-notes.dragas.net/categories/ownyourdata/)
  * [tutorial](https://it-notes.dragas.net/categories/tutorial/)
  * [linux](https://it-notes.dragas.net/categories/linux/)
  * [data](https://it-notes.dragas.net/categories/data/)
  * [networking](https://it-notes.dragas.net/categories/networking/)
  * [zfs](https://it-notes.dragas.net/categories/zfs/)
  * [jail](https://it-notes.dragas.net/categories/jail/)
  * [container](https://it-notes.dragas.net/categories/container/)
  * [filesystems](https://it-notes.dragas.net/categories/filesystems/)
  * [series](https://it-notes.dragas.net/categories/series/)
  * [web](https://it-notes.dragas.net/categories/web/)
  * [backup](https://it-notes.dragas.net/categories/backup/)
  * [View All Categories](https://it-notes.dragas.net/categories/)



### Links

  * [Home](https://it-notes.dragas.net)
  * [Archives](https://it-notes.dragas.net/archives/)
  * [Tags](https://it-notes.dragas.net/tags/)
  * [Categories](https://it-notes.dragas.net/categories/)
  * [Series](https://it-notes.dragas.net/series/)
  * [Under The Hood](https://it-notes.dragas.net/under-the-hood/)
  * [Professional Services](https://it-notes.dragas.net/professional-services/)
  * [About](https://it-notes.dragas.net/about-me/)
  * [RSS](https://it-notes.dragas.net/feed.xml)



(C) 2026 IT Notes. All rights reserved. 

Generated with [ITNBlog](https://itnblog.dragas.net) on 29/01/2026 09:12:41 UTC 
