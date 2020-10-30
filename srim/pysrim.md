---
layout: default
title: pysrim
description: Automation, analysis, and plotting of SRIM calculations
parent: SRIM
---

# pysrim
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

The Python package `pysrim` provides a slick and convenient way of scripting
some of the tedious aspects involed with running many similar `SRIM`
calculations. Its key strength is it provides a convenient interface to 
programatically define the calculation input. This is particularly
advantageous as it:

- allows for easy batch calculations where a few sim params are systematically varied (e.g., the ion implantation energy).
- enables the use of `for` loops to create multilayered heterostructures, which is painful to do otherwise.
- makes the record of the calculation <i>much</i> more readable than `SRIM`'s own custom input format.

It even works well when running on Linux
(i.e., it automatically calls `wine SRIM.exe`, `wine TRIM.exe`, etc.)!


## Caveats

`pysrim`, unfortunately, isn't perfect and I ran into the following issues while
using it.

<ul>
<li>
Everytime it runs, it complains that the `.yaml` file its reading isn't done
safely. This is due to a recent change in `pyYAML` requiring a `Loader` to be
specified as a `kwarg`. This is really only a minor annoyance, but can easily be
fixed by editing line 10 of `srim/core/elemementdb.py` so that it reads:

{% highlight python %}
return yaml.load(open(dbpath, "r"), Loader=yaml.SafeLoader)
{% endhighlight %}

There is currently a merge request on the project's GitLab page to fix this:
[https://gitlab.com/costrouc/pysrim/-/merge_requests/4](https://gitlab.com/costrouc/pysrim/-/merge_requests/4).
</li>
<li>
It fails to parse `IONIZ.txt` output when the ion energy is less than 1 keV.
The problem is with the regex expression used to parse the output.
As a simple workaround, rather than fixing the problem, it is sufficient to just
comment out line 36 of `srim/output.py` so that it reads:

{% highlight python %}
# raise SRIMOutputParseError("unable to extract ion from file")
{% endhighlight %}

With this change, `pysrim` will no longer automatically read all of the output
files; however, at least for my own purposes, this is fine.
</li>
<li>
The autosave input in `TRIM` setup does not appear to work; the calculation
won't run if `kwarg` is specified. This is relatively minor, so my workaround is
to just avoid providing the parameter.
</ul>

## Example

### Heterostructure

{% highlight python %}
{% include_relative heterostructure.py %}
{% endhighlight %}


