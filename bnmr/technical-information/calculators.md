---
layout: default
title: Calculators
description: Some useful calculators for β-NMR/β-NQR experiments at TRIUMF.
parent: Technical Information
grand_parent: β-NMR
---

# Calculators
{: .no_toc }

This is a small collection of calculators useful for running β-NMR/β-NQR
experiments at [TRIUMF] (see also <https://bnmr.triumf.ca/>).

Some of the calculators are web forms, where you simply enter a new value in one
of the boxes on the page and press ENTER or click outside the box to update the
values. Others are [Python] scripts, which can be downloaded and run on your own
machine.

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Bandwidth-to-pulse-duration converter for modulated RF fields

<center>
<form>
<table>
   <tbody>
      <tr>
      <td>
      
      </td>
      <td>
      <b>ln-sech</b>
      </td>
      <td>
      <b>Hermite</b>
      </td>
      </tr>
      <tr>
      <td>
       
      </td>
      <td>
      <i>t</i><sub>pulse</sub> (ms) × <i>B</i><sub>w</sub> (Hz) = 5 × 10<sup>4</sup>/π
      </td>
      <td>
      <i>t</i><sub>pulse</sub> (ms) × <i>B</i><sub>w</sub> (Hz) = 1764.8
      </td>
      </tr>
      <tr>
      <td>
      Pulse duration [<i>t</i><sub>pulse</sub>] (ms):
      </td>
      <td>
      <input name="Tls" value="79.5816" onchange="Bls.value = 15916.4/( this.value ) " type="text">
      </td>
      <td>
      <input name="Th" value="8.82" onchange="Bh.value = 1764.8/( this.value ) " type="text">
      </td>
      </tr>
      <tr>
      <td>
      Bandwidth [<i>B</i><sub>w</sub>] (Hz):
      </td>
      <td>
      <input name="Bls" value="200"  onchange="Tls.value = 15916.4/( this.value ) " type="text">
      </td>
      <td>
      <input name="Bh" value="200" onchange="Th.value = 1764.8/( this.value ) " type="text">
      </td>
      </tr>
   </tbody>
</table>
</form>
</center>


## β-NMR antenna-pickup-to-RF-field converter

<center>
<form>
   <table>
   <tbody>
   <tr>
   <td>
   
   </td>
   <td>
   <b><i>H</i><sub>1</sub> field</b>
   </td>
   </tr>
   <tr>
   <td>
   
   </td>
   <td>
   <i>H</i><sub>1</sub> (G) = 39.6 (G MHz/V) × <i>V</i><sub>p-p</sub> (V) / <i>f</i> (MHz)
   </td>
   </tr>
   <tr>
   <td>
   Antenna pickup [<i>V</i><sub>p-p</sub>] (V):
   </td>
   <td>
   <input name="Vpp" value="0.40" onchange="Hrf.value = (39.6 * this.value / 41.27)" type="text">
   </td>
   </tr>
   <tr>
   <td>
   RF frequency [<i>f</i>] (MHz):
   </td>
   <td>
   41.27
   </td>
   </tr>
   <tr>
   <td>
   RF field [<i>H</i><sub>1</sub>] (G):
   </td>
   <td>
   <input name="Hrf" value="0.38" onchange="Vpp.value = (41.27 * this.value / 39.6)" type="text">
   </td>
   </tr>
   </tbody>
   </table>
</form>
</center>

The above expression is accurate to ± 3 %.
Note that this expression is only valid for data collected before September 2019!

## β-NQR magnetic field calibration and calculator

<center>
<form>
   <table>
   <tbody>
   <tr>
   <td>
   
   </td>
   <td>
   <b>ILE2A1:HH</b>
   </td>
   </tr>
   <tr>
   <td>
   
   </td>
   <td>
   <i>H</i> (G) = <i>a</i> (G) + <i>b</i> (G/A) × <i>I</i> (A)
   </td>
   </tr>
   <tr>
   <td>
   Current setpoint [<i>I</i>] (A):
   </td>
   <td>
   <input name="I" value="90.292" onchange="H.value = (2.21309 * this.value + 0.17476)" type="text">
   </td>
   </tr>
   <tr>
   <td>
   Magnetic field [<i>H</i>] (G):
   </td>
   <td>
   <input name="H" value="200" onchange="I.value = (this.value - 0.17476 ) / 2.21309" type="text">
   </td>
   </tr>
   </tbody>
   </table>
</form>
</center>

The calibration constants are:
_a_ = 0.175 ± 0.046 G and _b_ = 2.2131 ± 0.0019 G / A.

## Demagnetization factors for common sample geometries

### Ellipsoid

{% highlight python %}
{% include_relative demagnetization_factor_ellipsoid.py %}
{% endhighlight %}

Download [`demagnetization_factor_ellipsoid.py`]({% link bnmr/demagnetization_factor_ellipsoid.py %}).

### Rectangular prism

{% highlight python %}
{% include_relative demagnetization_factor_prism.py %}
{% endhighlight %}

Download [`demagnetization_factor_prism.py`]({% link bnmr/demagnetization_factor_prism.py %}).

## Beamline optics

See: <https://beta.hla.triumf.ca/beam/tuneX/>.


[Python]: https://www.python.org/
[TRIUMF]: https://www.triumf.ca/
