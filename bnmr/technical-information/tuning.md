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

Once the ISAC operators have established transport of <sup>8</sup>Li<sup>+</sup>
up the last Farady cups before the NMR and NQR spectrometers,
they will notify us (usually by phone) and prompt us for some input.
This is, pragmatically, the beginning of the "fine" tuning of the beam
(but we'll just call it tuning for brevity).

The tuning "algorithm" is:

1. Perform a `1n` scan (i.e., Na or Rb cell). The is to find the optimal bias
   needed to Doppler-shift the beam onto resonance with the counter propagating
   polarizing laser light. Use the NBM for this. For <sup>8</sup>Li, a typical
   optimum is ~100 V.
1. Tune to the NMR spectrometer at 0 T with `BNMR:EL3` on (at its theory value).
   Get a centred beamspot. Does varying `ILE2A3:EL1` or `ILE2A3:EL2` by 
   ±300 V move the beamspot or just vary its shape/intensity?
   If the former (i.e., it moves), adjust the upstream elements.
   The goal is to get the beam going into the centre of the magnet
   (i.e., on axis with the field).
1. Move the cryostat so the beamspot is centred (if necessary).
1. Turn `BNMR:EL3` off and degauss the magnetic field to the desired setpoint
   (e.g., 6.55 T or whatever field is planned for the run).
1. Look at the beamspots at NQR (but do not place too much emphasis on it).
1. Tune on the forward detector rate (`ILE2:SCALER:CH4` in [EPICS]) at high platform bias
   (e.g., 19.5 kV for a ~20 keV beam).
1. Check the NMR beamspots at all biases. Should have a single tune when the
   beamspot does not move position, but focuses/de-focuses at different
   implantation energies.
1. Fine tune the beamspot at NQR (usually easy - just vertical/horizontal steering to compensate
   for field/bias). Except for at low magnetic fields (e.g. < 50 G), a separate tune is
   usually necessary for each field/bias combination (i.e., to have beamspots
   the exact same size in the exact same positions). For some experiments, this
   may be overkill.

The optimum settings for the steering elements on the beamline can be calculated
and viewed using the [tuneX] application.

Note that when using a <sup>31</sup>Mg<sup>+</sup> beam, it is perhaps best to
skip the "adjustments" given in step 2 and go directly to step 4 (i.e., ramp
up the magnet). This will focus the betas into the detectors and give a better
metric for the rates/beamspot. Without the focusing effect from the field, the
rates may be lower enough (on the order of ~1k s<sup>-1</sup>) that it is hard
to judge if all of the beam is delivered to the spectrometer.
See the bnmr logbooks from, for example, October 2019 and July 2021 for further
notes.

[EPICS]: https://en.wikipedia.org/wiki/EPICS
[TRIUMF]: https://www.triumf.ca/
[tuneX]: https://beta.hla.triumf.ca/beam/tuneX/