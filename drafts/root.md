---
layout: default
title: ROOT
description: ROOT Data Analysis Framework
has_children: true
has_toc: true
---

# ROOT

ROOT is an open-source data analysis framework born at [CERN] in the 1990s.
While it is targeted primarily for high energy physics experiments,
its utility extends beyond this relm, providing many features that are useful
across all branches of experimental science
(e.g., saving, processing, and fitting data).
As such, the following taglines can be found on the web,
succinctly advertising ROOT's capabilities:

- ROOT: a modular scientific software framework.
- ROOT: analyzing petabytes of data, scientifically.
- ROOT: analyzing, storing and visualizing big data, scientifically.

The canonical citation for ROOT is:

<ul>
  <li>
    <p>
      R. Brun and F. Rademakers.
    </p>
    <p>
      <i>ROOT - an object oriented data analysis framework.</i>
    </p>
    <p>
      Nucl. Instrum. Methods Phys. Res., Sect. A <b>389</b>, 81-86 (1997).
    </p>
    <p>
      <i class="ai ai-doi"></i>
      <a href="https://doi.org/10.1016/S0168-9002(97)00048-X">10.1016/S0168-9002(97)00048-X</a>
    </p>
  </li>
</ul>

The source code for ROOT and related projects can be found on [Github].

While I have used ROOT for many years (espcially during my PhD),
I wouldn't necessarily describe the experience as "smooth" or "pleasant".
The project suffers from what I assume all old codes of substantial size do:
legacy issues.
The ROOT codebase, written [C++]
(with bindings to other languages like [Python]),
is <i>gigantic</i> and somewhat difficult to navigate.
That is, the optimal solution for a problem ~20 years ago may no longer be the
optimal implementation today.
Part of this is due to the continued evolution of [C++],
with recent "versions" of language greatly improving its usability.
As such, some of facilities in ROOT are wrought with idiosyncrasies and
complexity.

That said, ROOT does allow one to do some rather complicated things
(e.g., <i>parallelized</i> and <i>vectorized</i> fitting of data)
throught a relatively straightforward interface.
Similarly, when a histogram is involved, ROOT is "king".
It is for these reasons that I often find myself using ROOT and
here I will try to document how I overcame some use-case hurdles or give
examples of nice features others might like to make use of.

[C++]: https://isocpp.org/
[CERN]: https://home.cern/
[homepage]: https://root.cern/
[Github]: https://github.com/root-project
[Python]: https://www.python.org/
