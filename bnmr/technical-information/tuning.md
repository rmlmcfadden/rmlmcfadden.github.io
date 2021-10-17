---
layout: default
title: Tuning
description: Tuning instructions and resources for β-NMR experiments at TRIUMF.
parent: Technical Information
grand_parent: β-NMR
---

# Tuning

In contrast to μSR experiments at [TRIUMF],
tuning the radioactive beam for a
β-NMR experiment is done primarily by the ISAC operators,
not the β-NMR experimenter(s).

The role of the experimenter then is largely to provide guidance to the
operators so that they may deliver a beam with a "good" tune that satisfies the
(rather stringent) criteria for the experiment.
This mainly comes in towards the end of the startup - once the RIB has been
delivered up to the front of either spectrometer.

## General Instructions

The tuning "algorithm" is:

1. Perform a 1n (i.e., Na or Rb cell) scan. The is to find the optimal bias
   needed to Doppler-shift the beam onto resonance with the counter propagating
   polarizing laser light. Use the NBM for this. For <sup>8</sup>Li, a typical
   optimum is ~100 V.
2. Tune NMR at ZF with EL3 on; get a centred spot; does varying EL1/EL2 by 
   ±300 V move the beamspot or just vary its shape/intensity? If the former
   (i.e., it moves), adjust the upstream elements. The goal is to get the beam
   going into the centre of the magnet (i.e., on axis with the field).
3. Move the cryostat so the beamspot is centred.
4. Turn EL3 off and degauss the magnetic field to 6.55 T (or whatever field is
   planned for the run).
5. Look at the beamspots at NQR (but do not place too much emphasis on it).
6. Tune on the forward detector rate (CH4 Scaler in EPICS) at high platform bias
   (e.g., 19.5 kV for a ~20 keV beam).
7. Check the NMR beamspots at all biases. Should have a single tune when the
   beamspot does not move position, but focuses/defocuses at different
   implantation energies.
8. Fine tune NQR (usually easy - just vertical/horizonal steering to compensate
   for field/bias). Except at low fields (e.g. < 50 G), a sperate tune is
   usually necessary for each field/bias combination (i.e., to have beamspots
   the exact same size in the exact same positions). For some experiments, this
   may be overkill.

The optimum settings for the steering elements on the beamline can be calculated
and viewed using the [tuneX] application.

Note that when using a <sup>31</sup>Mg<sup>+</sup> beam, it is perhaps best to
skip the "adjustements" given in step 2 and go directly to step 4 (i.e., ramp
up the magnet). This is focus the beta into the detectors and give better
metrics for the rates/beamspot. Without the fousing effect from the field, the
rates may be lower enough (on the order of ~1k s<sup>-1</sup>) that it is hard
to judge if all of the beam is delivered to the spectrometer.
See the bnmr logbooks from, for example, October 2019 and July 2021 for further
notes during tuning.

[EPICS]: https://en.wikipedia.org/wiki/EPICS
[TRIUMF]: https://www.triumf.ca/
[tuneX]: https://beta.hla.triumf.ca/beam/tuneX/
