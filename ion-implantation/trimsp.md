---
layout: default
title: TRIM.SP
description: TRIM.SP
parent: Ion Implantation
---

# `TRIM.SP`

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
    <dt>Volume</dd>
        <dd>34</dd>
    <dt>Issue</dt>
        <dd>2</dd>
    <dt>Pages</dt>
        <dd>73-94</dd>
    <dt>Year</dt>
        <dd>1984</dd>
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1007/BF00614759">10.1007/BF00614759</a></dd>
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
    <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/10.1080/10420159408219787">10.1080/10420159408219787</a></dd>
</dl>

---

The code still sees routine use as a means of calculating μ<sup>+</sup>
stopping distances in μSR experiments using the [LEM facility] at [PSI].
A modified version of the `TRIM.SP` source code (maintained by the [LEM group])
can be found [here](https://gitlab.psi.ch/nemu/simulation).
Additionally, an online interface to `TRIM.SP`
(with limited simulation capabilities)
can be found [here](http://musruser.psi.ch/cgi-bin/TrimSP.cgi).

[LEM facility]: https://www.psi.ch/en/smus/lem
[LEM group]: https://www.psi.ch/en/low-energy-muons
[PSI]: https://www.psi.ch/en
[`TRIM`]: https://doi.org/10.1016/0029-554X(80)90440-1
