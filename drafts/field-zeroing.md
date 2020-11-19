---
layout: default
title: Field Zeroing
description: Zeroing the magnetic field at the β-NQR spectrometer.
parent: β-NMR
mathjax: true
---

# Field Zeroing
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

Here I give an updated version of the field-zeroing procedure at the NQR
spectrometer. The intention is that this delineation is more explicit and,
therefor, clearer than its predecessor.
Similarly, the infrastructure and know-how for doing the processing/analysis
of the data has improved dramatically over the last few years and the companion
scripts for this document have been updated accordingly.
This is should improve the automation and accuracy of the zeroing procedure.

## Theory

The magnitude of the total magnetic field $$\mathbf{B}_{0}$$ at the sample
position is:
$$
\begin{equation}
   B_{0} = \sqrt{ B_{x}^{2} + B_{y}^{2} + B_{z}^{2} } 
\end{equation}
$$
where each orthogonal component $$B_{i}$$ can be decomposed into
$$
\begin{equation}
   B_{i} = B_{i}^{s} + B_{i}^{a},
\end{equation}
$$
which is the sum of ambient/stray ($$s$$) and
deliberately applied ($$a$$) contributions.
The $$B_{i}^{a}$$ contributions come from sets of coils with (approximate)
Helmholtz geometry surrounding the NQR spectrometer's vacuum chamber. 
Recall that
$$
\begin{equation*}
   B_{i}^{a} \propto I_{i},
\end{equation*}
$$
where $$I$$ is the (direct) current and the implicit
proportionality factor just depends on the geometry of the coil
(i.e., number of turns, coil radius, etc.).
With this, we can re-cast our expression for $$B_{0}$$ more explicitly:
$$
\begin{equation}
   B_{0} = \sqrt{ \left ( B_{x}^{s} + c_{x} I_{x} \right )^{2} + \left ( B_{y}^{s} + c_{y} I_{y} \right )^{2} + \left ( B_{y}^{s} + c_{z} I_{z} \right )^{2} },
\end{equation}
$$
where the $$c_{i}$$s are the proportionality constants.


To achieve zero field, the idea is to set each $$I_{i}$$ such that the condition
$$
\begin{equation}
   c_{i} I_{i} = -B_{i}^{s}
\end{equation}
$$
is satisfied for every direction $$i$$.
A quick way to check this would be with a Hall probe, but this isn't possible
since the sample position is inaccessible inside the UHV beamline.
In this situation, the best way to determine the ideal coil current settings is,
in fact, with the <sup>8</sup>Li probe itself.
Recall that the Larmor frequency
$$
\begin{equation}
   \nu_{0} = \frac{\gamma}{2 \pi} B_{0},
\end{equation}
$$
where
$$
\begin{equation}
\gamma / 2 \pi = \SI{6.3016}{\mega\hertz\per\tesla}
\end{equation}
$$
is the gyromagnetic ratio of <sup>8</sup>Li.
This proportionality gives us an unambiguous means for measuring the magnetic
field at the probe stopping site and the procedure to do this is sketched below.

## Procedure

The basic idea is to vary the currents $$I_{i}$$ at look at how $$\nu_{0}$$ is
modified through a series of <sup>8</sup>Li resonance measurements.
By changing the current systematically between runs, an accurate determination
of the coefficients $$B_{i}^{s}$$ and $$c_{i}$$ (which are not known a priori)
is possible, which are then used identify the optimal current:
$$
\begin{equation}
   I_{i} = - \frac{ B_{i}^{s} }{ c_{i} }.
\end{equation}
$$
\citeauthor{2003-Morris-PB-326-252}~\cite{2003-Morris-PB-326-252} have good
advice on how to accomplish this task and I shamelessly quote them here:

<blockquote cite="https://doi.org/10.1016/S0921-4526(02)01618-6">
The objective of the field scans is to measure the field at trim coil currents
$$( I_{x}; I_{y}; I_{z} )$$ about the point where the net magnetic field is
zero, but to avoid taking a run in a field so small that an accurate
determination of [the resonance] frequency is difficult to obtain from the
asymmetry.
</blockquote>

<blockquote cite="https://doi.org/10.1016/S0921-4526(02)01618-6">
It is generally easiest to start with a field scan in an axis perpendicular to
the [<sup>8</sup>Li] spin. For example, with the [<sup>8</sup>Li] spin
approximately along $$z$$ ..., a scan of the vertical $$x$$ component ... is
certain to obtain a substantial [shift in $$\nu_{0}$$], at least at the higher
$$|I_{x}|$$. The other axis perpendicular to the initial [<sup>8</sup>Li] spin
($$y$$ in our example) is then scanned, with a [small or zero] field along $$x$$
... applied.
</blockquote>

<blockquote cite="https://doi.org/10.1016/S0921-4526(02)01618-6">
Finally, with a fair knowledge of the $$x$$ and $$y$$ field components and
coils, one can [scan $$I_{z}$$ such that $$B_{z}$$ is low, but non-zero, and
interpolate to identify the frequency minimum].
</blockquote>

<blockquote cite="https://doi.org/10.1016/S0921-4526(02)01618-6">
Passing through a frequency minimum in a weak field scan on each axis
unambiguously identifies the zero-field settings.
</blockquote>

In principle, any material can be used for this;
however, <sup>8</sup>Li's coupling to host nuclear spins tends to
result in substantial relaxation at low $B_{0}$,
generally making the measurement more difficult.
Similarly, a material with a non-vanishing EFG at the implanted probe site
will add structure to its resonance in a field-dependent way -
a complication best avoided here.
Years of experience suggests that gold is reasonable choice for the
field-zeroing since it is slow relaxing down to very low field~\cite{2008-Parolin-PRB-77-214107, 2018-MacFarlane-JPSCP-21-011020} with a relatively simple lineshape, especially near room temperature~\cite{2003-MacFarlane-PB-326-213, 2008-Parolin-PRB-77-214107}.
Using pulsed RF (i.e., 2e mode), resonances are well described by a simple
Gaussian:
$$
\begin{equation}
   G \left ( \nu \right ) = a \exp \left [ - \frac{ \left (\nu - \nu_{0} \right )^{2} }{2 \sigma^{2}} \right ] + b
\end{equation}
$$
where $$a$$ is the amplitude, $$b$$ is the baseline, $$\sigma$$ is the width
parameter (related to the linewidth by: $$\mathrm{FWHM} = 2 \sqrt{2 \ln 2} \sigma$$),
and $\nu_{0}$ is the resonance frequency.



This is a footnote.[^1]


> This is a quote.



[^2003-Morris-PB]: G. D. Morris and R. H. Heffner, <i>A method of achieving accurate zero-field conditions using muonium</i>, [Physica B <b>326</b>, 252 (2003)](https://doi.org/10.1016/S0921-4526(02)01618-6).

[^2008-Parolin-PRB]: T. J. Parolin, Z. Salman, K. H. Chow, Q. Song, J. Valiani, H. Saadaoui, A. O’Halloran, M. D. Hossain, T. A. Keeler, R. F. Kiefl, S. R. Kreitzman, C. D. P. Levy, R. I. Miller, G. D. Morris, M. R. Pearson, M. Smadella, D. Wang, M. Xu, and W. A. MacFarlane, <i>High resolution β-NMR study of <sup>8</sup>Li<sup>+</sup> implanted in gold</i>, [Phys. Rev. B <b>77</b>, 214107 (2008)](https://doi.org/10.1103/PhysRevB.77.214107).

[^2018-MacFarlane-JPSCP]: W. A. MacFarlane, K. H. Chow, M. D. Hossain, V. L. Karner, R. F. Kiefl, R. M. L. McFadden, G. D. Morris, H. Saadaoui, and Z. Salman, <i>The spin relaxation of <sup>8</sup>Li<sup>+</sup> in gold at low magnetic field</i>, [JPS Conf. Proc. <b>21</b>, 011020 (2018)](https://doi.org/10.7566/JPSCP.21.011020).

[^4]: W. A. MacFarlane, G. D. Morris, T. R. Beals, K. H. Chow, R. A. Baartman, S. Daviel, S. R. Dunsiger, A. Hatakeyama, S. R. Kreitzman, C. D. P. Levy, R. I. Miller, K. M. Nichol, R. Poutissou, and R. F. Kiefl, <i><sup>8</sup>Li<sup> β-NMR in thin metal films</i>, [Physica B <b>326</b>, 213 (2003)](https://doi.org/10.1016/S0921-4526(02)01604-6).




\begin{table}
\centering
\caption{ \label{tab:fz2014}
Tabulated results from the analysis of the <sup>8</sup>Li resonance (2e mode) in \ch{Au} foil fit to a Gaussian at different trim coil currents.
Included are: the current $I$ for the $x$, $y$, and $z$ coils; the resonance frequency $\nu_{0}$; the linewidth; the amplitude $a$; and the $b$.
The full table is plotted in \Cref{fig:fz2014}, grouped by common applied current.
The spectra were processed using bnmr\_2e.
}
\footnotesize
\begin{tabular}{l l S S S S S S S}
\toprule
{Year} & {Run} & {$I_{x}$ (\si{\ampere})} & {$I_{y}$ (\si{\ampere})} & {$I_{z}$ (\si{\ampere})} & {$\nu_{0}$ (\si{\hertz})} & {FWHM (\si{\hertz})} & {$a$} & {$b$} \\
%{Year} & {Run} & {$I_{x}$} & {$I_{y}$} & {$I_{z}$} & {$\nu_{0}$} & {FWHM} & {Amplitude} & {Baseline} \\
% & & {(\si{\ampere})} & {(\si{\ampere})} & {(\si{\ampere})} & {(\si{\hertz})} & {(\si{\hertz})} &  & \\
\midrule
2014 & 46080 & 0.00 & 0.00 & 4.43 & 7382 \pm 4 & 227 \pm 9 & 0.0532 \pm 0.0018 & -0.0019 \pm 0.0005 \\
2014 & 46081 & 6.25 & 0.00 & 4.43 & 7662 \pm 5 & 252 \pm 12 & 0.0438 \pm 0.0017 & -0.0010 \pm 0.0005 \\
2014 & 46082 & 3.00 & 0.00 & 4.43 & 7386 \pm 4 & 240 \pm 11 & 0.0481 \pm 0.0018 & -0.0018 \pm 0.0005 \\
2014 & 46083 & -6.25 & 0.00 & 4.43 & 8106 \pm 5 & 222 \pm 13 & 0.0390 \pm 0.0019 & -0.0010 \pm 0.0005 \\
2014 & 46084 & -3.00 & 0.00 & 4.43 & 7603 \pm 5 & 257 \pm 15 & 0.0411 \pm 0.0018 & -0.0010 \pm 0.0005 \\
2014 & 46085 & 1.37 & 0.00 & 4.43 & 7355 \pm 4 & 234 \pm 10 & 0.0529 \pm 0.0018 & -0.0018 \pm 0.0005 \\
2014 & 46086 & 1.37 & 10.30 & 4.43 & 7404 \pm 5 & 263 \pm 12 & 0.0484 \pm 0.0018 & -0.0003 \pm 0.0005 \\
2014 & 46087 & 1.37 & 5.00 & 4.43 & 7361 \pm 4 & 225 \pm 10 & 0.0513 \pm 0.0019 & -0.0013 \pm 0.0005 \\
2014 & 46088 & 1.37 & -10.30 & 4.43 & 7445 \pm 4 & 238 \pm 9 & 0.0521 \pm 0.0016 & -0.0019 \pm 0.0004 \\
2014 & 46089 & 1.37 & -5.00 & 4.43 & 7379 \pm 4 & 249 \pm 10 & 0.0544 \pm 0.0018 & -0.0012 \pm 0.0005 \\
2014 & 46090 & 1.37 & 0.08 & 4.43 & 7357 \pm 5 & 250 \pm 12 & 0.0449 \pm 0.0017 & -0.0013 \pm 0.0005 \\
2014 & 46092 & 1.37 & 0.08 & 8.96 & 13777 \pm 4 & 190 \pm 10 & 0.0509 \pm 0.0023 & -0.0011 \pm 0.0004 \\
2014 & 46094 & 1.37 & 0.08 & -4.43 & 5237 \pm 7 & 284 \pm 20 & 0.0487 \pm 0.0027 & -0.0004 \pm 0.0005 \\
2014 & 46097 & 1.37 & 0.08 & -8.96 & 11677 \pm 7 & 187 \pm 19 & 0.0486 \pm 0.0038 & -0.0007 \pm 0.0007 \\
\bottomrule
\end{tabular}
\end{table}



\begin{figure}
\centering
\includegraphics[scale=1.0]{data/field-zeroing-2014-revisited.pdf}
\caption{ \label{fig:fz2014}
<sup>8</sup>Li resonance frequency at different trim coil currents.
The measurements were acquired in order from top to bottom.
Only one $I_{i}$ was scanned per panel and the currents for the other coils are in indicated in the inset.
A clear frequency minimum can be identified for each field sweep.
The solid lines denote the fit to all data simultaneously (i.e., a true 3D fit).
}
\end{figure}




\section{Example \label{sec:example}}


As an example, I reproduce the results/analysis for last time the zeroing procedure was done ---  the Fall of 2014!


low field SLR in \ch{Au} foil~\cite{2018-MacFarlane-JPSCP-21-011020}.
field dependence at slightly higher field~\cite{2008-Parolin-PRB-77-214107}.















{% highlight cpp %}
void zero_field() {
  // read in the data (somehow)
  Data raw_data("results.dat");

  // magnetic field function
  TF3 *f_B = new TF3("f_B", B_0, -10, 10, -10, 10, -10, 10, 6);
  //
  f_B->SetTitle("Magnetic Field Magnitude;B_{x};B_{y};B_{z}");
  //
  // f_B->SetNpx(500);
  // f_B->SetNpy(500);
  // f_B->SetNpz(500);
  //
  f_B->SetParName(0, "[x] b_x");
  f_B->SetParName(1, "[x] c_x");
  f_B->SetParName(2, "[y] b_y");
  f_B->SetParName(3, "[y] c_y");
  f_B->SetParName(4, "[z] b_z");
  f_B->SetParName(5, "[z] c_z");
  //
  f_B->SetParameter(0, 1);
  f_B->SetParameter(1, -0.2);
  f_B->SetParameter(2, 2);
  f_B->SetParameter(3, 0.3);
  f_B->SetParameter(4, 3);
  f_B->SetParameter(5, -0.1);
  
  ROOT::Fit::BinData data(raw_data.size(), raw_data.I_x.data(),
                          raw_data.I_y.data(), raw_data.I_z.data(),
                          raw_data.nu.data(), nullptr, nullptr, nullptr,
                          raw_data.nu_error.data());

  ROOT::Fit::Fitter fitter;

  // wrapped the TF1 in a IParamMultiFunction interface for the Fitter class
  ROOT::Math::WrappedMultiTF1 wf(*f_B, 3);
  fitter.SetFunction(wf);

  fitter.Config().MinimizerOptions().SetPrintLevel(2);
  fitter.Config().SetMinimizer("Minuit2", "Migrad");

  fitter.LeastSquareFit(data);
  ROOT::Fit::FitResult result = fitter.Result();
  if (result.IsValid()) {
    fitter.Config().SetMinosErrors();
    fitter.LeastSquareFit(data);
    result = fitter.Result();
  } else {
    std::cout << "fit did not coverge -  consider constraining parameters\n";
  }

  result.Print(std::cout);

  std::cout << "rChi2 = " << result.Chi2() / result.Ndf() << "\n";

  f_B->SetFitResult(result);

  // Scale errors according to reduced chi2
  // result.NormalizeErrors();

  double x_min = I_min(result, 0, 1);
  double y_min = I_min(result, 2, 3);
  double z_min = I_min(result, 4, 5);

  double x_min_error = I_min_error(result, 0, 1);
  double y_min_error = I_min_error(result, 2, 3);
  double z_min_error = I_min_error(result, 4, 5);

  std::cout << "The minimum B = " << f_B->Eval(x_min, y_min, z_min) << " for\n";
  std::cout << "I_x = " << x_min << " +/- " << x_min_error << " A\n";
  std::cout << "I_y = " << y_min << " +/- " << y_min_error << " A\n";
  std::cout << "I_z = " << z_min << " +/- " << z_min_error << " A\n";
  
}
{% endhighlight %}


