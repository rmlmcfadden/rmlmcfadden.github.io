---
layout: default
title: Tuning
description: Tuning instructions and resources for β-NMR experiments at TRIUMF.
parent: β-NMR
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
   beamspot does not move position, but focuses/defocuses at different implantation energies.
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

## The β-NQR "extension"

In 2021, the high parallel field extension the "β-NQR" leg of the ISAC low-energy
beamline was completed. This new end station offers the ability to apply ~2 kG
magnetic fields perpendicular to a sample surface - a desirable feature for
certain scientific applications.

There is less experience using the new beamline optics and these notes
(originally by Edward Thoeng) serve as an aid for tuning to the extension.

### Objectives

- Establish a common tune to both the NMR and NQR spectrometers with the NMR magnetic on.
- Make sure that the beam is always centered on-axis going into the NQR leg.
  This detail is crucial for the ability to focus the beam using electrostatic quadrupoles
  without moving the beamspot (i.e., the beam position).

### Procedure

1. Turn all magnets off at both the NMR and NQR spectrometers.
  - Set the NMR magnet (in CAMP) to 0 T.
  - Set `BNQR:HH3` to 0 A.
  - Set `BNQR:HH6` to 0 A.
1. Tune using stable <sup>7</sup>Li<sup>+</sup> to NQR.
  - Make sure the beam is centred on `ILE2A:RPM2`.
    Should see peaks at 0.5 mm (horizontal) and 1.5 mm (vertical).
    If not, only adjust `ILE2:B21` for X-steering and `ILE2:YCB19` for Y-steering.
    The beam profile should also be circular and roughly 2 rms in both X- and Y-directions.
    If not, adjust `ILE2:Q16`, `ILE2:Q17`, `ILE2:Q18`, and/or `ILE2:Q19`.
    Check that the `ILE2A:RPM2` peak positions do not move when `ILE2A:Q2` is changed.
    If they do, the beam is not centred and `ILE2:B21`/`ILE2:YCB19` need to be adjusted.
  - Make sure the beam in centred on `ILE2A:LPM0`.