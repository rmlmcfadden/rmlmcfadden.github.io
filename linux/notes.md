---
layout: default
title: Notes
description: Notes on Linux administration.
parent: Linux
---

# Notes
{: .no_toc }

Here I give some short notes related to the administration of a [Linux] system.


## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Cleaning up space in `/`

<!--- from 2016-12-23 --->

Though it is much less prevalent nowadays, in the past it was occasionally
possible to run out of disk space in the root directory (i.e., `/`).
Usually, most of the space was "eaten up" by `/var/cache` and `/var/log`,
so the task then is to free them.

There are a few possibilities to try, such as:

{% highlight bash %}
journalctl --disk-usage
journalctl --verify
journalctl --vacuum-size=50M
{% endhighlight %}

or edit

{% highlight bash %}
/etc/systemd/journald.conf
{% endhighlight %}

Alternatively, one can try cleaning the `packagekit` cache
(which isn't done automatically!?).

{% highlight bash %}
pkcan refresh force -c -1
{% endhighlight %}


## Mounting LVM2 (LVMR?) filesystems

<!--- from 2017-04-21 --->

I came across this difficulty while trying to mount a hard drive which had an
old [Fedora] install while running a fresh (i.e., newer) version of [Fedora].
A key issue may be that all Fedora (default) installs give these volumes the
same name.

Here is what I did to solve the mounting problem
(and re-gain access to all the old files):

{% highlight bash %}
su -
lvmdiskscan
lvdisplay # get LV name and VG name
vgdisplay
lvscan # see which are inactive
vgrename <UUID> <VolumeGroupName>
{% endhighlight %}

where
`<UUID>` is the Volume Group UUID
and
`<VolumeGroupName>` is the New Volume Group Name.

{% highlight bash %}
modprobe dm-mod
vgchange -ay
{% endhighlight %}

Now you should be able to mount the old drive!

Some other commands that may be usefull are:

{% highlight bash %}
pvscan
vgscan
{% endhighlight %}


[Fedora]: https://getfedora.org/
[Linux]: https://en.wikipedia.org/wiki/Linux
