---
layout: default
title: SRIM
description: Stopping and range of ions in matter.
parent: Ion Implantation
---

# `SRIM`
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

The Stopping and Range of Ions in Matter (`SRIM`) is a collection of software
for calculations/simulations dealing with ion transport in matter.
This includes:

- ion stopping and range in targets,
- ion implantation,
- sputtering,
- ion transmisstion,
- and ion beam therapy.

Further details can be found at the `SRIM` homepage (<http://www.srim.org/>),
as well as the textbook sharing the same name:

---

<dl>
    <dt>Title</dt>
        <dd>SRIM - The Stopping and Range of Ions in Matter</dd>
    <dt>Author</dt>
        <dd>J. F. Ziegler, J. P. Biersack, M. D. Ziegler</dd>
    <dt>Edition</dt>
        <dd>7</dd>
    <dt>Publisher</dt>
        <dd>SRIM Co.</dd>
    <dt>Address</dt>
        <dd>Chester, MD</dd>
    <dt>Year</dt>
        <dd>2008</dd>
    <dt>Cover</dt>
        <dd><img src="/assets/images/srim_textbook_cover.jpg" alt="SRIM textbook" width="25%"></dd>
</dl>

---

Papers dealing with specific versions of `SRIM` also exist:

- [SRIM 2010](https://doi.org/10.1016/j.nimb.2010.02.091)
- [SRIM 2003](https://doi.org/10.1016/j.nimb.2004.01.208)

Though the software is free, it is [closed source] and written in
(the now defunct language) [Visual Basic].
Niether of these traits are particularly appealing
(or sensible) by modern standards.
Nevertheless,
it offers a user friendly interface for a number of
complicated tasks that are useful for many branches of science
(e.g., the stopping profile of an implanted ion).

For those who prefer to work with scripts over `SRIM`'s [GUI],
check out [pysrim]({% link ion-implantation/pysrim.md %}),
which provides a nice [Python] interface to the application.

## Running on Linux

Though `SRIM` is a (legacy) [Microsoft Windows] application,
it is possible to run the program on [Linux] thanks to the magic of [Wine].
Some install instructions are already available [online](https://appdb.winehq.org/objectManager.php?sClass=application&iId=5992) and these seemed to work well in the past;
however, for recent versions of [Wine]/[Linux], a modified installation procedure
was required.

First, I removed any previous instance of [Wine] by executing:

{% highlight bash %}
rm -rf ~/.wine
{% endhighlight %}

Next, I added the following to my `.bashrc` file:

{% highlight bash %}
export WINEARCH=win32
export WINEPREFIX=~/.wine
{% endhighlight %}

and in a fresh terminal run:

{% highlight bash %}
winecfg
{% endhighlight %}

This ensures a clean 32-bit [Wine] instance is set up.

Through inspection of the contents of `~/.wine/drive_c/windows/system32`,
I noticed that many of the `.dll` and `.ocx` files needed by `SRIM` are already
present. Instead following the exact instructions of registering each of the
`.ocx`s provided with the application
(i.e., in the folder `/path/to/srim/SRIM-Setup/`),
I elected to start `SRIM` via:

{% highlight bash %}
wine SRIM.exe
{% endhighlight %}

which then prompted me with error messages as to which files were
unregistered/missing. To rectify this, I both copied the missing files
(from the `SRIM Setup` directory) to `~/.wine/drive_c/windows/system32` and
registered them using:

{% highlight bash %}
regsvr32 *.ocx
{% endhighlight %}

where `*.ocx` is the missing (copied) file.

Afterwards, `SRIM` ran without issue!

[closed source]: https://en.wikipedia.org/wiki/Proprietary_software
[Visual Basic]: https://en.wikipedia.org/wiki/Visual_Basic
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[Python]: https://www.python.org/
[Microsoft Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[Linux]: https://en.wikipedia.org/wiki/Linux
[Wine]: https://www.winehq.org/
