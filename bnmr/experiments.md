---
layout: default
title: Experiments
description: List of approved β-NMR experiments at TRIUMF.
parent: β-NMR
mathjax: true
---

# Experiments

Experiments at TRIUMF must be approved by an Experimental Evaluation Committee
(EEC) before being allocated beamtime. Since duplicate and overlapping
experiments (i.e., those which may be directly competative with one another) are
generally forbidden, it is useful to keep track of what experiments are
happening in parallel, as well as those that have already been performed.

An up-to-date list of β-NMR experiments at TRIUMF is given below.

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
