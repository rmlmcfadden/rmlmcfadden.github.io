---
layout: default
title: TRIM.SP
description: TRIM.SP
parent: Ion Implantation
---

# `TRIM.SP`
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

`TRIM.SP` is an offshoot of the original [`TRIM`] program that additionally
includes sputtering effects in the simulation of ion implantation.
The original citations for the work are:

---

<dl>
    <dt>Title</dt>
        <dd>Sputtering studies with the Monte Carlo program TRIM.SP</dd>
    <dt>Author</dt>
        <dd>J. P. Biersack, W. Eckstein</dd>
    <dt>Journal</dt>
        <dd>Appl. Phys. A</dd>
    <dt>Volume</dt>
        <dd>34</dd>
    <dt>Issue</dt>
        <dd>2</dd>
    <dt>Pages</dt>
        <dd>73-94</dd>
    <dt>Year</dt>
        <dd>1984</dd>
    <dt>Abstract</dt>
        <dd>
        <details>
        <summary></summary>
        The Monte Carlo Program TRIM.SP (sputtering version of TRIM) was used to
        determine sputtering yields and energy and angular distributions of
        sputtered particles in physical (collisional) sputtering processes. The
        output is set up to distinguish between the contributions of primary and
        secondary knock-on atoms as caused by in- and outgoing incident ions, in
        order to get a better understanding of the sputtering mechanisms and to
        check on previous theoretical models. The influence of the interatomic
        potential and the inelastic energy loss model as well as the surface
        binding energy on the sputtering yield is investigated. Further results
        are sputtering yields versus incident energy and angle as well as total
        angular distributions of sputtered particles and energy distributions in
        specific solid angles for non-normal incidence. The calculated data are
        compared with experimental results as far as possible. From this
        comparison it turns out that the TRIM.SP is able to reproduce
        experimental results even in very special details of angular and energy
        distributions.
        </details>
        </dd>
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1007/BF00614759">10.1007/BF00614759</a></dd>
</dl>

---

<dl>
    <dt>Title</dt>
        <dd>Computer Simulation of Ion-Solid Interactions</dd>
    <dt>Author</dt>
        <dd>W. Eckstein</dd>
    <dt>Series</dt>
        <dd>Springer Series in Materials Science</dd>
    <dt>Volume</dt>
        <dd>10</dd>
    <dt>Publisher</dt>
        <dd>Springer-Verlag</dd>
    <dt>Address</dt>
        <dd>Berlin, Heidelberg</dd>
    <dt>Year</dt>
        <dd>1991</dd>
    <dt>Introduction</dt>
        <dd>
        <details>
        <summary></summary>
        In this book the author discusses the investigation of ion bombardment
        of solids by computer simulation, with the aim of demonstrating the
        usefulness of this approach to the problem of interactions of ions with
        solids. The various chapters present the basic physics behind the
        simulation programs, their structure and many applications to different
        topics. The two main streams, the binary collision model and the
        classical dynamics model, are discussed, as are interaction potentials
        and electronic energy losses. The main topics investigated are
        backscattering, sputtering and implantation for incident atomic
        particles with energies from the eV to the MeV range. An extensive
        overview of the literature is given, making this book of interest to the
        active reseacher as well to students entering the field.
        </details>
        </dd>
    <dt>Cover</dt>
        <dd><img src="https://media.springernature.com/w306/springer-static/cover-hires/book/978-3-642-73513-4" width="25%"></dd>
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1007/978-3-642-73513-4">10.1007/978-3-642-73513-4</a></dd>
</dl>

---

<dl>
    <dt>Title</dt>
        <dd>Backscattering and sputtering with the Monte-Carlo program TRIM.SP</dd>
    <dt>Author</dt>
        <dd>W. Eckstein</dd>
    <dt>Journal</dt>
        <dd>Radiat. Eff. Defects Solids</dd>
    <dt>Volume</dt>
        <dd>130-131</dd>
    <dt>Issue</dt>
        <dd>1</dd>
    <dt>Pages</dt>
        <dd>239-250</dd>
    <dt>Year</dt>
        <dd>1994</dd>
    <dt>Abstract</dt>
        <dd>
        <details>
        <summary></summary>
        The changes of the program TRIM.SP namely the vectorization and other
        minor changes since its first publication in 1984 are shortly described.
        Examples especially about backscattering and sputtering illustrate the
        possibilities which can be handled by the program.
        </details>
        </dd>
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1080/10420159408219787">10.1080/10420159408219787</a></dd>
</dl>

---

The code still sees routine use as a means of calculating μ<sup>+</sup>
stopping distances in μSR experiments using the [LEM facility] at [PSI].
A modified version of the `TRIM.SP` source code (maintained by the [LEM group])
can be found at:

---

<dl>
    <dt>GitLab <i class="fab fa-gitlab"></i></dt>
        <dd><a href="https://gitlab.psi.ch/nemu/simulation">nemu/simulation</a></dd>
    <dt>Bitbucket <i class="fab fa-bitbucket"></i></dt>
        <dd><a href="https://bitbucket.org/zaher-salman/trimsp/">zaher-salman/trimsp</a></dd>
    <dt>PSI Gitea <i class="fab fa-git-alt"></i></dt>
        <dd><a href="https://gitea.psi.ch/LMU/TRIMSP">LMU/TRIMSP</a></dd>
</dl>

---

Additionally, an online interface to `TRIM.SP`
(with limited simulation capabilities)
can be found [here](http://musruser.psi.ch/cgi-bin/TrimSP.cgi).

## Caveats

- Bin widths less than 2 Å (e.g., 1 Å) do not behave as intended. I suspect
  there is a floating-point rounding problem when writing the histogram data to
  disk...
- The maximum number of bins in the `.rge` output is hardcoded in the [Fortran]
  source code...
- Only up to 5 elements per layer can be simulated!?
- The `TRIM.SP` [GUI] has trouble parsing chemical formulas with non-integer
  stochiometries. A [regex] is used to parse the formulas, but devising a
  pattern that works for <i>all</i> formulae is non-trivial - see e.g.:
  - [RegEx for parsing chemical formulas](https://stackoverflow.com/questions/23602175/regex-for-parsing-chemical-formulas)
  - [A strict regular expression for matching chemical formulae](https://stackoverflow.com/questions/46200305/a-strict-regular-expression-for-matching-chemical-formulae)
- The [GUI] automatically loads coefficients that define the electronic stopping
  power of the target material (which is an awesome feature) using the tabulated
  values for protons from [ICRU Report 49]; however, this compilation is rather
  dated and even omits a low-energy value for carbon
  (which has been filled in <i>ad hoc</i>, as discussed [here](https://lmu.web.psi.ch/docu/LEM_Memo/LEM_EnergyLoss_CarbonFoil/MemoEnergyLossInC-TRIMSP.pdf)).

[LEM facility]: https://www.psi.ch/en/smus/lem
[LEM group]: https://www.psi.ch/en/low-energy-muons
[PSI]: https://www.psi.ch/en
[`TRIM`]: https://doi.org/10.1016/0029-554X(80)90440-1
[Fortran]: https://fortran-lang.org/
[regex]: https://en.wikipedia.org/wiki/Regular_expression
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[ICRU Report 49]: https://www.icru.org/report/stopping-power-and-ranges-for-protons-and-alpha-particles-report-49/
