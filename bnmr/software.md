---
layout: default
title: Software
description: Software for analyzing β-NMR data taken at TRIUMF.
parent: β-NMR
mathjax: true
---

# Software
{: .no_toc }

Analyzing β-NMR data can be a rather onerous task and software plays a crucial
role in the processing, checking, fitting, and displaying of the results
obtained from a measurement. There are no "industrial" solutions for this; most
of the existing tools have been written on a as-needed basis and it is not
uncommon for "experimenters" to write their own code for a particular project.

Here I give a brief (and incomplete!) survey of the available tools.
Software considered outdated or defunct are marked as *OBSOLETE*.

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## mudpy, bdata, and bfit

Perhaps the most versatile set of tools for "wrangling" with any β-NMR data
collected at [TRIUMF] are the [Python] packages [mudpy], [bdata], and [bfit].
They are quite user-friendly, with [bfit] providing a feature-rich [GUI]
convenient "beginngers" or "exploratory" analyses. Alternatively, the packages'
[API] can be used directly in [Python] scripts, providing an even finer level
of control.

### Example

To demonstrate the power of the "scripted" approach,
let's consider the task of fitting some [SLR] data where the "amplitude" of each
measurement is shared as a common fit parameter (i.e., in a "global" fit).
As can be seen below, this is relatively painless to do!

{% highlight python %}
{% include_relative global_fit_slr.py %}
{% endhighlight %}

Try it out yourself!

Download [`global_fit_slr.py`]({% link bnmr/global_fit_slr.py %}).


## bnmr_20_*

Description to be added...

## bnmr-ROOT-suite

Description to be added...

## bnmroffice

*OBSOLETE*!

Description to be added...

## bnmrfit

*OBSOLETE*!

Description to be added...

## bnmrminfit

*OBSOLETE*!

Description to be added...

[API]: https://en.wikipedia.org/wiki/API
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[TRIUMF]: https://www.triumf.ca/
[Python]: https://www.python.org/
[mudpy]: https://github.com/dfujim/mudpy
[bdata]: https://github.com/dfujim/bdata
[bfit]: https://github.com/dfujim/bfit
