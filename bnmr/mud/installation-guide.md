---
layout: default
title: Installation Guide
description: MUD Library Installation Guide.
parent: MUD
grand_parent: β-NMR
---

# Installation Guide
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Instructions

On [Linux],
an easy way of installing the MUD library (and utility programs) is with:

{% highlight bash %}
wget http://cmms.triumf.ca/mud/mud.zip
unzip mud.zip
cd mud/
make all
sudo make install
sudo cp src/mud.h /usr/local/include
{% endhighlight %}

The last step above is mostly for convenience - you could equally include 
`mud.h` directly in the source code of each project that links to `libmud.a`.

Note that if you already have [Musrfit] installed, the above steps are
unecessary ([Musrfit] builds/installs the MUD library/headers when it's
compiled).

[Linux]: https://en.wikipedia.org/wiki/Linux
[Musrfit]: http://lmu.web.psi.ch/musrfit/user/html/
