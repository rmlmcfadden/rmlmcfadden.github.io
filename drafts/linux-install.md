---
layout: default
title: Linux Install
description: Installing SRIM on Linux using Wine.
parent: SRIM
---

# Linux Install

Though it has been years since I have done this,
I recall that installing `SRIM` on Linux is fairly trivial.
One needs to use `Wine` for this.
I was able to do this in the Fall of 2013 as a fresh Ph.D. student -
well before being gripped by an intrest
in computer science over the coming years.

Add some more explicit instruction here...

For simplicity, I'm just going to install everything in `$HOME`,
but you can put it whereever you like.

You can download `SRIM` using something like:

{% highlight bash %}
wget http://www.srim.org/SRIM/SRIM-2013-Pro.e -O $HOME/SRIM-2013.exe
{% endhighlight %}

which takes care of the archaic need to rename executable.

You need to use `Wine` for the installation:

{% highlight bash %}
wine $HOME/SRIM-2013.exe
{% endhighlight %}

which just involves following the instructions of the diaglog boxes that ensue.
Easy!

Now to actually get it running,
we need to manually install some missing Windows components.

Some vauge instructions for doing this are found here:
[https://appdb.winehq.org/objectManager.php?sClass=application&iId=5992](https://appdb.winehq.org/objectManager.php?sClass=application&iId=5992 "Wine HQ - SRIM").



Please install the following using winetricks
```
winetricks comdlg32ocx msflxgrd richtx32 vb5run comctl32ocx
```
then navigate to `llation-directory>/SRIM-Setup` and register `TabCtl32.ocx` using:
```
regsvr32 TabCtl32.ocx
```
in the near future will be possible to install `tabctl32` with winetricks too. 



Note that I think `winetricks` offers a more general,
elegent way of adding the missing Windows components;
however, I think you need to install the specific components shipped with `SRIM`
(i.e., those in the directory created during the installation).
