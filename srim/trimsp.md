---
layout: default
title: TRIM.SP
description: TRIM.SP
parent: SRIM
---

# TRIM.SP

TRIM.SP is an offshoot of the original [TRIM] program that additionally includes
sputtering effects in the simulation of ion implantation.
The original citations for the work are:

<ul>
  <li>
    <p>J. P. Biersack and W. Eckstein</p>
    <p><i>Sputtering studies with the Monte Carlo Program TRIM.SP</i></p>
    <p>Appl. Phys. <b>34</b>, 73-94 (1984).</p>
    <p>
    <i class="ai ai-doi"></i>
    <a href="https://doi.org/10.1007/BF00614759">10.1007/BF00614759</a>
    </p>
  </li>
  <li>
    <p>W. Eckstein</p>
    <p><i>Backscattering and sputtering with the monte-carlo program TRIM.SP</i></p>
    <p>Radiat. Eff. Defects Solids <b>130-131</b>, 239-250 (1994).</p>
    <p>
    <i class="ai ai-doi"></i>
    <a href="https://doi.org/10.1080/10420159408219787">10.1080/10420159408219787</a>
    </p>
  </li>
</ul>

The code still sees routine use as a means of calculating μ<sup>+</sup>
stopping distances in μSR experiments using the [LEM facility] at [PSI].
A modified version of the TRIM.SP source code (maintained by the [LEM group])
can be found [here](https://gitlab.psi.ch/nemu/simulation).
Additionally, an online interface to TRIM.SP
(with limited simulation capabilities)
can be found [here](http://musruser.psi.ch/cgi-bin/TrimSP.cgi).

[LEM facility]: https://www.psi.ch/en/smus/lem
[LEM group]: https://www.psi.ch/en/low-energy-muons
[PSI]: https://www.psi.ch/en
[TRIM]: https://doi.org/10.1016/0029-554X(80)90440-1
