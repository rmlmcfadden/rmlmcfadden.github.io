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

The source code for ROOT and related projects are hosted on [GitHub] and further
details, including documentation and tutorials, can be found on the ROOT
[homepage].

The canonical citation for the ROOT framework is:

---

<dl>
    <dt>Title</dt>
        <dd>ROOT - an object oriented data analysis framework</dd>
    <dt>Author</dt>
        <dd>R. Brun, F. Rademakers</dd>
    <dt>Journal</dt>
        <dd>Nucl. Instrum. Methods Phys. Res., Sect. A</dd>
    <dt>Volume</dt>
        <dd>389</dd>
    <dt>Issue</dt>
        <dd>1-2</dd>
    <dt>Pages</dt>
        <dd>81-86</dd>
    <dt>Year</dt>
        <dd>1997</dd>
    <dt>Abstract</dt>
        <dd>
        <details>
        <summary></summary>
        The ROOT system in an Object Oriented framework for large scale data
        analysis. ROOT written in C++, contains, among others, an efficient
        hierarchical OO database, a C++ interpreter, advanced statistical
        analysis (multi-dimensional histogramming, fitting, minimization,
        cluster finding algorithms) and visualization tools. The user interacts
        with ROOT via a graphical user interface, the command line or batch
        scripts. The command and scripting language is C++ (using the
        interpreter) and large scripts can be compiled and dynamically linked
        in. The OO database design has been optimized for parallel access
        (reading as well as writing) by multiple processes.
        </details>
        </dd>
    <dt>Logo</dt>
        <dd><img src="https://root.cern.ch/img/logos/ROOT_Logo/misc/generic-logo-color-plustext-512.png" width="50%"></dd>
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1016/S0168-9002(97)00048-X">10.1016/S0168-9002(97)00048-X</a></dd>
    <dt><i class="fab fa-github"></i></dt>
        <dd><a href="https://github.com/root-project/root">root-project/root</a></dd>
</dl>

---

While I have used ROOT for many years (espcially during my PhD),
I wouldn't describe the entire experience as "smooth" or "pleasant".
While it's likely some of the discomfort was to due to my own ignorance,
others have made stronger claims (e.g., calling it "[the ROOT of all evil]").

In my opinion,
ROOT suffers from what I assume all old codes of substantial size do:
legacy issues.
The ROOT codebase, written [C++]
(with bindings to other languages like [Python]),
is <i>gigantic</i> and somewhat difficult to navigate.
It implements a staggering number of individual components,
which all interact together - many through multiple inheritance -
with some rather curious designs/interfaces.
Some of this is certainly related to the age of the code.
That is, the optimal solution for a problem ~20 years ago may no longer be the
optimal implementation today.
Part of this is due to the continued evolution of [C++],
with recent "versions" of language greatly improving its usability.
As such, some of facilities in ROOT are wrought with unecessary idiosyncrasies
and complexity.

That said, ROOT <i>does</i> allow one to do some rather complicated things
(e.g., <i>parallelized</i> and <i>vectorized</i> fitting of data)
without having to implement all the low-level details yourself.
Similarly, when a histogram is involved, ROOT is pretty much "king".
It is for these reasons that I still often find myself turning to ROOT when
tackling certain problems.

Here I will try to document how I overcame some use-case hurdles or give
examples of nice features others might like to make use of.

[C++]: https://isocpp.org/
[CERN]: https://home.cern/
[homepage]: https://root.cern/
[GitHub]: https://github.com/root-project
[Python]: https://www.python.org/
[the ROOT of all evil]: http://insectnation.org/articles/problems-with-root.html
