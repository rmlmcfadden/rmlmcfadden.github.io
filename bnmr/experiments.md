---
layout: default
title: Experiments
description: List of approved β-NMR experiments at TRIUMF.
parent: β-NMR
mathjax: true
---

# Experiments

An up-to-date list of ongoing and previous β-NMR experiments at [TRIUMF] is
given in the table below.

A list of <i>all</i> approved experiments at [TRIUMF] can be found
[here](https://mis.triumf.ca/science/experiment/list.jsf?schedule=View+all&discipline=View+all&status=View+all).

<table>
   <thead>
      <th>Number</th>
      <th>Title</th>
      <th>Spokespersons</th>
      <th>Status</th>
   </thead>
   <tbody>
   {% assign experiments = site.data.bnmr.experiments | reverse %}
   {% for exp in experiments %}
   <tr>
      <td><a href="{{ exp.url }}">{{ exp.experiment }}</a></td>
      <td>{{ exp.title }}</td>
      <td>{{ exp.spokespersons | join: ", " }}</td>
      <td>{{ exp.status }}</td>
   </tr>
   {% endfor %}
   </tbody>
</table>

Note that, as with all accelerator based experiments at [TRIUMF], β-NMR
experiments require the submission of a written proposal and approval from an
Experimental Evaluation Committee (EEC) prior to being allocated beamtime.
More details can be found at
[here](https://www.triumf.ca/research-program/planning-experiments).

[TRIUMF]: https://www.triumf.ca/
