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

[Linux]: https://en.wikipedia.org/wiki/Linux
