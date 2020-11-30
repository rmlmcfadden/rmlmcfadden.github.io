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

- allows for easy "batch" calculations where a few simulation parameters are
  systematically varied (e.g., the ion implantation energy).
- allows the use of `for` loops when creat multilayered heterostructures, which
  is arduous otherwise.
- makes the record of the calculation <i>much</i> more readable than `SRIM`'s
  own custom (and dated) input format.

It even works well when running on Linux
(i.e., it automatically calls `wine SRIM.exe`, `wine TRIM.exe`, etc.)!

As a bonus, it also has a short paper that can be cited:

---

<ul>
  <li>
    <p>
      C. Ostrouchov, Y. Zhang, and W. J. Weber.
    </p>
    <p>
      <i>pysrim: automation, analysis, and plotting of SRIM calculations.</i>
    </p>
    <p>
      J. Open Source Software <b>3</b>, 829 (2018).
    </p>
    <p>
      <i class="ai ai-doi"></i>
      <a href="https://doi.org/10.21105/joss.00829">10.21105/joss.00829</a>
    </p>
  </li>
</ul>

---

## Caveats

`pysrim`, unfortunately, isn't perfect and I ran into the following issues while
using it:

- Everytime it runs, it complains that the `.yaml` file its reading isn't done
  safely. This is due to a recent change in `pyYAML` requiring a `Loader` to be
  specified as a `kwarg`. There is currently a
  [merge request](https://gitlab.com/costrouc/pysrim/-/merge_requests/4) on the
  project's [GitLab page](https://gitlab.com/costrouc/pysrim) to fix this, but
  until this gets officially patched it can be mended by editing line 10 of
  `srim/core/elemementdb.py` so that it reads:

{% highlight python %}
return yaml.load(open(dbpath, "r"), Loader=yaml.SafeLoader)
{% endhighlight %}

- It fails to parse `IONIZ.txt` output when the ion energy is less than 1 keV.
  The problem is with the regex expression used to parse the output. As a simple
  workaround, rather than fixing the problem, it is sufficient to just comment
  out line 36 of `srim/output.py` so that it reads:

{% highlight python %}
# raise SRIMOutputParseError("unable to extract ion from file")
{% endhighlight %}

- The autosave input in `TRIM` setup does not appear to work; the calculation
  won't run if the `kwarg` is specified. This is relatively minor, so my
  workaround is to just avoid providing the parameter.

## Example: a multi-layered heterostructure

Here I give an example showcasing `pysrim`'s capabilities.
The script below creates a target with a complex layered structure
(one that would be particularly unpleasent to do "by hand")
and runs several `TRIM` calculations for a single ion at
a few different implantation energies.
Conveniently, the script takes care of moving all the results to
their own (new) folder after each calculations completes.

{% highlight python %}
{% include_relative heterostructure.py %}
{% endhighlight %}

Try it out yourself!

Download [`heterostructure.py`]({% link srim/heterostructure.py %}).
