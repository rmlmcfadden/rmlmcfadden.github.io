---
layout: default
name: Building from Source
description: Intstructions on building ROOT from its source code.
parent: ROOT
---

# Building from Source
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

Building ROOT from source is no easy task - just ask anyone who has done it!

Fortunately, the quality of the documentation has improved dramatically over the
years, which has to some extent mitigated the difficulty of the task.

## Dependencies

ROOT provides list of dependence for different operating systems,
which can be found [here](https://root.cern/install/dependencies/).

In my experience, these are not reliably up-to-date, but still a good starting
point for wrangling all the build pieces.

## Build instructions

The official build instructions can be found
[here](https://root.cern/install/build_from_source/).

Really, the build instructions are better passed to a script that can be easily
edited and executed - there are simply too many options to type out for each
build! 

Assuming a directory structure similar to the following:
{% highlight bash %}
.
├── build
│   └── root
├── build-root.sh
└── root
{% endhighlight %}
where `root/` is the ROOT git repository,
`build/root/` is the ROOT build directory,
and `build-root.sh` is the build script,
I automate compiling the ROOT source code by running
{% highlight bash %}
bash build-root.sh
{% endhighlight %}
which you can download here: [`build-root.sh`]({% link root/build-root.sh %})

It's still a work in progress, but it gets the job done.

Unfortunately, having a build script isn't a bulletproof solution either, as the
build options tend to change (often silently) between versions. However, this
problem may be diminished in the near future (see e.g.,
<https://github.com/root-project/web/issues/272>).
