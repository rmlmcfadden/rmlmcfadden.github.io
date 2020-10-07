---
layout: default
title: Autorun
description: β-NMR Automatic Run Control
permalink: /bnmr/autorun
parent: β-NMR
---

# Autorun
{: .no_toc }

<i>
This page is a reproduction of the content found at
[http://cmms.triumf.ca/howto/op/autobnmr.html](http://cmms.triumf.ca/howto/op/autobnmr.html "βNMR Automatic Run Control").
Though this is mainly to test the formatting of the markdown to html convension,
I have made minor changes thoughout the text to improve readability.
</i>

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

The automatic run control operates as a separate process, distinct
from other data acquisition front- and back-ends, including the run-control
user-interface. It should be started automatically, but if it is not,
then one can execute:

{% highlight bash %}
$MUSR_DIR/musr_midas/mui/autoruns.tcl
{% endhighlight %}

The autorun server is controlled by a few parameters in the ODB, under 
`/autorun`, but it is mostly controlled by the autorun plan file, which
it monitors continuously for changes.

(The ODB is the [MIDAS] data acquisition system's central storage of experiment
parameters. It can be explored and edited using the `odbedit` program or a web
browser.)

## Control Panel

The custom [MIDAS] web page for β-NMR and β-NQR experiments includes an area
for controlling autorun parameters. (If there are problems setting
parameters from the main control page, you may try to set them by 
navigating the ODB tree.)

Edit the plan file in your preferred text editor. Every time it is saved,
the autorun program re-reads it.

If there are problems with the syntax of a plan file, the autorun processor 
usually only reports the first error it encounters. Check the [MIDAS]
message log for error messages. There is also a stand-alone command, 
`checkplan` or

{% highlight bash %}
$MUSR_DIR/musr_midas/mui/checkplan.tcl
{% endhighlight %}

(used as "checkplan <i>filename</i> [<i>first_run</i>]")
that performs checks on a plan file, useful for verifying a hand-edited plan.
Nevertheless, the autorun processor may encounter some errors that the preliminary 
scan does not detect, so these checks will not completely replace a good proofread.

## Control Parameters

There are a few parameters to set on the autorun control panel.
Most of these are passed to the autorun processor through the [MIDAS] ODB
(in the area `/autorun`).

### Autoruns Operation Enabled

ODB: `/autorun/enable`, boolean (1/0)<br>
Set this to control whether the autorun process operates at all. It does not actually
shut down when disabled, but it checks only this parameter, waiting
to be enabled again.

### Autorun State

Autoruns status read-back.

ODB: `/autorun/state`, int<br>
The values are interpreted as:
<table>
<thead>
<tr>
<th>Value</th>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td> disabled</td><td>Operation is not enabled</td></tr>
<tr><td>1</td><td> idle</td><td>Waiting for a plan</td></tr>
<tr><td>2</td><td> acquiring</td><td>Run is in progress and active</td></tr>
<tr><td>3</td><td> paused</td><td>Run is paused</td></tr>
<tr><td>4</td><td> ending</td><td>Ending a run</td></tr>
<tr><td>5</td><td> stopped</td><td>Run has ended</td></tr>
<tr><td>6</td><td> setting</td><td>Setting Camp variables</td></tr>
<tr><td>7</td><td> changing</td><td>Waiting for "requirements"</td></tr>
<tr><td>8</td><td> starting</td><td>Starting a new run</td></tr>
<tr><td>9</td><td> reload</td><td>Trigger reload of plan file</td></tr>
</tbody>
</table>

Most state values are set by the autorun server, strictly for monitoring its 
progress, but a value of "reload" (9) may be set by other clients to force
the autorun server to re-read the plan file, and perhaps resume processing
after being "idle" (1); the Reload&Start button will trigger reloading this way.
(The other way to force a reload is to modify the plan file itself, perhaps 
like `touch plan.dat`.)

### Plan file

Full file specification for the run plan.

ODB: `/autorun/plan file`, string<br>
The autorun processor watches this file for changes, and if any occur, it
re-reads the run plan.

### Pausing Runs

Enable/Disable run pausing.

ODB: `/autorun/enable pausing`, boolean-int (1/0)<br>
Tells the autoruns processor whether to keep checking requirements after
starting a run, and to pause the run while requirements are not
satisfied. See below for "Requirements" in an autorun plan.
(A [CAMP] alarm with a hardware veto gives better response.)

### Refresh Period

Cycle time of autorun processor.

ODB: `/autorun/refresh seconds`, int<br>
Tells how often the autorun processor checks status and looks for a new plan.
Sensible values range from 5 to 30 seconds.

### Target Cycles

Desired total cycles for TD/Type-2 runs.

ODB: `/autorun/target cycles`, int<br>
Tells how many frontend cycles to run for Type-2 modes.
(This parameter applies to any runs, not just automatic runs.)

### Target Counts

Desired total counts for TD/Type-2 runs.

ODB: `/autorun/target counts`, int<br>
Tells how many events to accumulate in histograms before ending the run.
This number is reset for every run, according to the run plan setting
(if that run has a `Counts` setting in the plan),
but it can be changed during the run to take more or less data.

### Count Histogram

What "Target Counts" applies to.

ODB: `/autorun/count histogram`, int<br>
The "Target Counts" may be compared with the counts in any particular
histogram or with the total of all histograms, as indicated by the "Count
Histogram" setting. The first histogram is number 1. Enter zero or negative
to use the total of all histograms.

### Time Limit (minutes)

Maximum time before ending a run.

ODB: `/autorun/time limit (minutes)`, float<br>
You may enter the time limit in various formats, but the value will be
displayed and saved as a number of minutes. Use a very high value or
zero if there is to be no time limit. Between runs, this value may
be reset by any specifications in the run plan. It can be manually changed
during a run without editing the plan.

### Reload & Start

Apply the settings.

If autoruns are enabled, but idle, then force reloading the plan, 
even if the plan file hasn't changed.

## Run plan file: commands and syntax

The run plan consists of a series of commands, in plain text, grouped
by run number - all commands in a group apply to a particular run.
Each command consists of a keyword, optionally followed by a colon (`:`), 
and white space before any values. Besides the trailing colon, embeded
underscore characters (`_`) are ignored, as is capitalization
of the command. Although they are ignored, capitalization, underscores,
or colons can make a plan file more readable, especially when 
there are continued lines. In this documentation, the optional 
capitalization is usually used, and the colon used occasionally.

Commands may be broken across multiple lines by ending the partial line(s) with `\`.

Lines that begin with certain characters (`!#%;`) are comments, and are ignored,
as are blank lines.

In the command syntax below, <b>bold</b> indicates a literal keyword,
<i>italics</i> indicate some sort of value, 
"|" separates multiple possibilities, 
and "[ ]" brackets indicate some optional parameter.
<i>
The `|`, `[`, and `]` characters should not be typed into a run plan!
</i>

One command, <b>Run</b>, is absolutely required, and it comes first:

<b>Run</b> &nbsp;<i>number</i><br>
<b>Run</b> &nbsp;<b>next</b><br>
<b>Next</b> &nbsp;<b>run</b>

The `Run` command begins the commands for that particular run; all ensuing 
commands apply to that run, until the next Run command.
The specified run number must be consecutive with the previous. You
can use the `next` keyword instead of a number, but the first 
run must be explicitly numbered. (The reason the numbering must
be defined is so that the plan can be edited and reloaded in the
middle, without having to remove all the runs that have already been
performed.)

If there are settings to be made after the last run has completed, use

<b>Finally</b>

to separate those settings from the preceding run; it is like a Run command, but
no run will be performed.

The remaining commands can be in any order.

In the case of TI (type-1) runs, there is the required sweep range:

<b>SweepRange</b> &nbsp;<i>from</i> &nbsp;<i>delim</i> &nbsp;<i>to</i>&nbsp;<i>delim</i> &nbsp;<i>step</i>

The delimiter <i>delim</i> signifies white-space and/or punctuation
characters or even any of the letters in `toby`
(e.g., `10,100:2`, `5000 7000 500`, or `1 to 10 by 1`).
People might try to use `200-300:10` for a range,
but `-` is <i>not</i> a legal delimiter since the dangers of
misinterpreting a minus sign are too great.
All the values (<i>from</i>, <i>to</i>, <i>step</i>) are integers.

Other commands (all the commands listed below) are strictly optional, 
and, if omitted, they retain the previous settings; that is, the values 
will not be actively set to any values, but will be retained by the 
respective [MIDAS] or [CAMP] systems.

There are four possible commands to control when the run should be
ended:

<table border=0 cellspacing=0 cellpadding=0>
<tr><td><b>Counts</b> &nbsp;<i>number</i> [ <b>M</b> ] &nbsp;[ <i>hist_number</i> ] </td><td> &nbsp;&nbsp; ( for TD )</td></tr>
<tr><td><b>Time_limit</b> &nbsp;<i>elapsed_time</i></td><td> &nbsp;&nbsp;&nbsp; ( for TD or I )</td></tr>
<tr><td><b>Sweeps</b> &nbsp;<i>number_of_sweeps</i></td><td> &nbsp;&nbsp;&nbsp; ( for I )</td></tr>
<tr><td><b>Cycles</b> &nbsp;<i>number_of_cycles</i></td><td> &nbsp;&nbsp;&nbsp; ( for TD )</td></tr>
</table>

Typically, one should use Counts to tell the total number of events 
to accumulate in a TD/Type-2 run; it can be given in "real"
number form, and with an optional `M` suffix to indicate
"millions" (e.g., `3200000`, `32e5`, and `3.2M` are all the same).
This parameter will replace the value in the ODB at the beginning of a run,
but a user may manually change it in the ODB while the run is in progress, 
which is the best way to extend an automatic run in progress.
If no `Counts` command is given for a run, the existing value of
`/autorun/total counts` from the ODB is kept.
If the optional <i>hist_number</i> is specified, then the counts
are checked for that histogram only, rather than the total of all histograms.

The Time_limit setting (with alias `Elapsed`) tells the longest time that 
may be spent on a run.
The <i>elapsed_time</i> can be in many formats, and a simple number is interpreted
as minutes; all of the following are equal: `1:30`, `5400 s`, `90 min`, `1.5hr`,
`01:30:00`, `90`.
Units are any strings that begin with `s`, `m`, or `h`.
Notice that `1:30` means 1.5 hours, not 1.5 minutes! For 1.5 minutes
you would need `0:01:30` (or `1.5 min` or `90s`).
You can specify both counts and time limits, in which case the run ends when either 
is satisfied. Note that using an elapsed-time limit may result in runs with no data 
if the beam is off for a long time.

The `Sweeps` command is for TI runs only, and tells how many sweeps to make.
It updates the corresponding parameter in the ODB: 
`/Equipment/MUSR_I_acq/settings/input/num sweeps`,
which applies to any run, not only autoruns.

The `Cycles` command is for TD runs only, and tells how many cycles to perform.
It applies to all runs, even when autoruns are disabled or idle.

Arrange to have autorun error and warning messages forwarded by email with

<b>Email</b> &nbsp;<i>addr</i>&nbsp; [ <b>,</b> <i>addr</i> <code>...</code> ]

providing a list of email addresses, separated by commas. When there are problems,
the corresponding messages will be emailed to these addresses. If you have an
address that gets forwarded to a cell phone or pager, that would be good to use.

Several commands apply to the run headers, corresponding to the [MIDAS]
"edit on start" variables.

<b>Sample</b> &nbsp; <code> ...</code><br>
<b>Orientation</b> &nbsp; <code> ...</code><br>
<b>Operator</b> &nbsp; <code> ...</code><br>
<b>Experiment</b> &nbsp; <i>number</i><br>
<b>Temperature</b> &nbsp; <i>temperature</i> &nbsp;| &nbsp;<i>Camp_var</i><br>
<b>Field</b> &nbsp; &nbsp; <i>field</i> &nbsp;| &nbsp;<i>Camp_var</i>

Note that temperature and field may be entered as numbers (with implicit
units of Kelvin and Gauss), as numbers with units (provided the conversion
to Kelvin or Gauss is known to the program), or as a the full [CAMP] path
for a temperature or field variable.

<b>Title: </b> &nbsp; <code> ...</code>

The run title allows automatic insertion of other header fields using the tags 
`<Sample>`, `<Operator>`, `<Experiment>`, `<Temperature>`, `<Field>`, and
`<Orientation>` (yes, you type the "angle brackets" `<...>` around the tag name).
For example:

{% highlight bash %}
Title: <Sample> annealed, T=<Temperature>, B=<Field> <Orientation>, p=+2%
{% endhighlight %}

The autorun system will replace these tags with the appropriate header
values, both at the beginning of the run and at intervals throughout
the run; this ensures that automatic Temperature and Field headers, as 
well as any manual settings, are propagated to the run title. The system 
will <strong>STOP</strong> updating the title if the user manually sets it
to something different. 

For time-integral runs, there is also the percentage tolerance for the beam normalization:

<b>Tolerance</b> &nbsp; <i>number</i> &nbsp; [ <b>%</b> ]

(The percent sign is optional, and does not affect the interpretation of
the number.)

<!-- 
Other acquisition control parameters have no "personalized" commands,
but should be set by loading a previously-saved configuration:
<p>
<b>Mode:</b>  &nbsp;<i>saved_TDmuSR_mode_name</i><br>
<b>Setup:</b> &nbsp;<i>saved_ImuSR_setup</i>
<p>
-->

Any ODB parameter can be set using the `SetOdb` command:

<b>SetOdb</b> &nbsp;<i>odb_variable</i>&nbsp; &nbsp;<i>value</i>

where <i>odb_variable</i> is the full ODB path to the variable, enclosed in
quotes if the name contains any spaces. The value should also be quoted
if it contains spaces (use double-quotes, not apostrophes).

You can control some portions of the beamline or platform:

<b>SetEpics:</b> &nbsp;<i>Epics_var</i> &nbsp; <i>value</i>

The `SetEpics` command (with spelling variants) sets a particular beam element 
to a value. [EPICS] variables are always in upper case, and contain
colons (`:`) as separators; they usually begin with the beamline or system name.
To find the <i>Epics_var</i>, go to the beamline [EPICS] control window and click the
middle mouse button on the entry field (blue text) where you would type the value. 
The <i>Epics_var</i> will be displayed in a small pop-up window (the text 
is "selected", so you can immediately "paste" it into the plan file).
The full <i>Epics_var</i> may be abbreviated for some elements
commonly adjusted in autoruns, especially for turning elements on or off.
When switching an element on or off, the <i>value</i> should
be "on" or "off" for clarity; thus the examples

{% highlight bash %}
SetEpics:  BNMR:HVBIAS:POS:VOL  16.0
SetEpics:  BIAS  16.0
{% endhighlight %}
(short for β-NQR's `ILE2:BIAS15:VOL`).

Make [CAMP] settings using either or both of:

<b>SetCamp</b> &nbsp;<i>Camp_var</i> &nbsp; <i>value</i><br>
<b>Camp_cmd</b> &nbsp;<i>Camp_command</i>

(`SetCamp` has aliases `set_camp`, `camp_set` and `CampSet`, because we all
forget.)

The <i>Camp_var</i> argument is a complete [CAMP] variable path,
including all slashes, such as `/Helios/mag_field`.

The <i>value</i> argument should be numeric or a text string, as 
appropriate for the particular <i>Camp_var</i>. Numeric values may be 
given as arithmetic expressions. For selection variables, one must
use the exact same string as used by [CAMP], including capitalization, or
an integer index, counting from zero. As a special shortcut, abbreviations 
of the form <<i>Camp_var</i>> (with explicit angle-brackets) may be 
used as (or in) the <i>value</i> argument, indicating that the value of 
another [CAMP] variable should be substituted.

The <i>Camp_command</i> is any command (or inline `Tcl` script) as 
documented in Appendix B of the [CAMP Software Manual](http://cmms.triumf.ca/software/camp_soft.pdf)

Examples are:

{% highlight bash %}
SetCamp:  /Magnet/mag_field  0.25
SetCamp:  /Sample/control_set  15
SetCamp:  /Diffuser/control_set  </Sample/control_set> - 0.5
SetCamp:  /field_control/setpoint  </Hall/field>
SetCamp:  /Diffuser/heat_range MED
camp_cmd: insLoad /defibrulator medical.kit
{% endhighlight %}

The autorun controller will perform all those [CAMP] and [EPICS] commands at once,
as soon as the preceding run has ended. This doesn't meet the full
needs for setting [CAMP] devices, particularly in cases such as the 
field control example above, where one would like to reference the
`/Hall/field` value after the magnet has stabilized. One way to handle
this is to schedule some settings after a fixed time delay:

<b>After</b> <i>elapsed_time</i>&nbsp;<b>:</b> 
    &nbsp;<b>SetCamp &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;|
    &nbsp;<b>camp_cmd &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;| 
    &nbsp;<b>SetEpics &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;| 
    &nbsp;<b>AutoTune &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;|


where the forms of <i>elapsed_time</i> is similar to the run time-limit, except that a bare
number is interpreted as <em>seconds</em> (six minutes could be given by any of
6m, 0:06, 0.1h, 360s, 360). This is the first of two 
composite commands, where a <i>required</i> colon (`:`) must separate the `After`
declaration from the ensuing, delayed, command. Note that only some commands can 
be deferred with `After`; any others give a syntax error (because they aren't allowed).

Before a run can begin, we must know that the experimental conditions 
have responded to the device settings, so we specify "requirements"

<table border=0 cellspacing=0 cellpadding=0>
<tr><td>        </td><td>    &nbsp; </td>
  <td width=1 rowspan=8 bgcolor=black><table border=0 cellspacing=0 cellpadding=0><tr><td></td></tr></table></td><td>&nbsp; </td>
  <td width=1 rowspan=3 bgcolor=black><table border=0 cellspacing=0 cellpadding=0><tr><td></td></tr></table></td>
   <td align=center><i>blank&nbsp; </i></td>
  <td width=1 rowspan=3 bgcolor=black><table border=0 cellspacing=0 cellpadding=0><tr><td></td></tr></table></td></tr>
<tr><td>        </td><td>    &nbsp; </td>
  <td>&nbsp; <b>stable</b>&nbsp; </td> 
   <td>&nbsp; <b>at</b>&nbsp; &nbsp;&nbsp; <i>number</i> &nbsp; </td>
             <td>&nbsp; <font size=+2>[</font> <b>within</b> &nbsp;<i>error</i> <font size=+2>]</font> </td>
             <td>&nbsp; <font size=+2>[</font> <b>for</b> &nbsp;<i>elapsed_time</i> <font size=+2>]</font> <br></td></tr>
<tr><td>        </td><td>    &nbsp; </td>
  <td>&nbsp; </td> 
   <td>&nbsp; <b>equal</b>&nbsp; <i>Variable</i>&nbsp;&nbsp; </td> </tr>
<tr><td><b>Require &nbsp;&nbsp; </b></td><td> <i>Variable</i>&nbsp; &nbsp; </td> <td> </td> </tr>
<tr><td>        </td><td>    &nbsp; </td>
  <td>&nbsp; <b>above</b>&nbsp;  &nbsp; </td><td></td><td>&nbsp; <i>number</i>  </td>
   <td width=1 rowspan=2 bgcolor=black><table border=0 cellspacing=0 cellpadding=0><tr><td></td></tr></table></td> 
   <td rowspan=2 colspan=2 valign=center>&nbsp; <font size=+2>[</font> <b>for</b> &nbsp;<i>elapsed_time</i> <font size=+2>]</font></td></tr>
<tr><td>&nbsp; </td><td>&nbsp; </td>
  <td>&nbsp; <b>below</b> &nbsp; </td><td></td><td>&nbsp; <i>number</i>  </td></tr>
<tr><td>  &nbsp;       </td><td>     &nbsp;           </td> </tr>
<tr><td></td><td> </td> <td>&nbsp; <b>is</b>&nbsp; </td><td></td><td>&nbsp; <i>string</i><br></td></tr>
</table>

The run will not begin until every requirement is satisfied simultaneously, 
<strong>and there are no [CAMP] alarms active</strong>. (Thus, you can enforce many typical 
constraints by setting alarms in [CAMP], rather than giving requirement commands.)

Each <i>Variable</i> is the full path specification of a [CAMP] variable, such as
`/Sample/sample_read`, or an [EPICS] variable, such as `M20:S1:HVNEG:VOL`
(distinguished by the presense of `/` or `:`).

For numeric variables, one should usually use the "stable" form of the command.
The autorun system will collect values of the primary <i>Variable</i>, retaining those over 
the latest <i>elapsed_time</i>. To satisfy the requirement, all retained values must be
within <i>error</i> of either: the latest value (blank comparison fields), or the 
given <i>number</i> ("at"), or the current value of the comparison variable 
("equal"). (Notice that `Require /foo/bar stable` is the same as `Require /foo/bar stable equal /foo/bar`.)

The default <i>elapsed_time</i>, if none was specified, is 1 second (almost 
immediately). The default units, if a bare number was given, is seconds.

Numeric variables can also be tested to be "above" or "below" some value.

For string or selection variables, use the "is" form for the requirement.
If the <i>string</i> contains spaces, then it should be quoted.

Examples:

{% highlight bash %}
Require /diffuser/control_read  stable  equal  /diffuser/control_set  within  0.5
Require /sample/sample_read  stable  within 0.5  for  2 m
Require /Hall_Probe/field  stable  at  1.0  for  30
Require /shield/sample_read below 100
Require M20:EXPT:RDCUR  stable  equal  M20:EXPT:CUR  within  2
Require /Magnet/ramp_status  is  Persistent
{% endhighlight %}

(Note that the last example specifies "Persistent"; "persistent" 
would not work because the actual value in [CAMP] is capitalized. Make sure the requirement 
string exactly matches what [CAMP] displays!)

Here is another example, part of a temperature scan, where the desired temperature
is specified just <emph>once</emph>, on the diffuser set-point.

{% highlight bash %}
Run  1234
Title  <Sample>, <Temperature>, automatically
Temperature  /sample/sample_read
Require  /sample/sample_read stable equal /diffuser/control_set within 3
Require  /sample/sample_read stable within 0.5 for 2m
Setcamp  /diffuser/control_set   22
{% endhighlight %}

The run will begin when the sample temperature levels off (within 0.5 K) for
2 minutes, and within 3 K of the diffuser setpoint (i.e., between 19 and 25 K).
Whatever the average sample temperature is, over the course of the run, it will be recorded 
in the temperature field of the run header, and thence the run title of the data file.
Note that, in this example as always, the `Setcamp` command is performed before ever
checking requirements; entering the `Setcamp` declaration after the requirements does
<i>not</i> imply that the settings are performed after requirements are satisfied.
For that feature, see the `When` command.

<b>Max_wait</b> &nbsp;<i>elapsed_time</i>

In case of conflicting requirements, or some other problem where the requirements
are never satisfied, there is a `Max_wait` command. After waiting for <i>elapsed_time</i>,
the autorun sequencer will start the next run even if the requirements are not satisfied.
The various formats for <i>elapsed_time</i> are that same as on the `Time_limit` command,
with default units of minutes (see above).

For greater control over the timing of [CAMP] settings than is provided by the `After` command,
one can schedule them the same way as specifying a requirement:

<b>When</b> &nbsp;<i>requirement_specification</i> 
    &nbsp;<b>:</b> 
  &nbsp;<b>SetCamp</b> &nbsp; <code>...</code> &nbsp;| 
  &nbsp;<b>camp_cmd</b>  &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>SetEpics</b>  &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>AutoTune</b> &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>After</b> &nbsp; <code>...</code> &nbsp;|
  &nbsp;<i>blank</i>

The <i>requirement_specification</i> is any valid parameter list for the `Require`
command (above), and is followed by a mandatory colon separator. Only the device 
setting commands for [CAMP] and [EPICS] (`SetCamp`, `SetEpics`, `camp_cmd`, and their aliases) 
and the `After` command may be scheduled this way. You can also specify a null action 
with no scheduled command, which behaves like a simple `Require` command except... 

Conditions specified by `When` must all be satisfied at some point
<i>before</i> a run can begin, but they need not <i>remain</i> satisfied
until the run begins. This makes a `When` command with a null action subtly
different from the same `Require` command: all `Require` conditions must be
simultaneously satisfied when the run begins, whereas all `When` actions (or
null actions) must have been performed sometime before the run begins.

If a [CAMP] setting must be delayed until after the run begins, then you must use 
an `After` command, either alone or scheduled by a `When` command, like:

{% highlight bash %}
When /sample/sample_read stable within .5 After 5m: setCamp /sample/setup/P 20
{% endhighlight %}

A typical use is to start controlling a variable after a previous setting is 
complete:

{% highlight bash %}
When /Hall/field stable within .5: setCamp /field_cont/setpoint </Hall/field>
When /Hall/field stable within .5: setCamp /field_cont/function 2
When /sample/sample_read below 8: setCamp /sample/heat_range LOW
When /diffuser/sample_read stable equal /diffuser/control_set within 1 for 1.5m: \
     After 3m: setCamp /nv_cont/function 2
{% endhighlight %}

(Note the use of `\` to join multiple lines when commands get too long,
and the substitution for the current value of the field readback.)
This example turns on (feedback) field control when the magnet current reaches its
setpoint, and turns on needle-valve control three minutes after the cryostat
diffuser temperature gets close to its setpoint. Notably, it also specifies the
same requirements for beginning the run;  thus, presuming the (diffuser) temperature
is the last to stabilize, the needle-valve control will begin about three minutes
after the run begins. 

In the example (and in practice) note the use of multiple `When` commands having the
same requirement but different actions. To save typing and computer processing, these can
be written as a <i>block</i>

<table border=0 cellpadding=0><tr><td>
<table valign=c>
<tr><td><b>When</b> &nbsp;<i>requirement_specification</i> &nbsp;&nbsp;<b>do</b> &nbsp;</td></tr>
<tr><td>  &nbsp;  &nbsp;<b>.&nbsp;&nbsp;.&nbsp;&nbsp;.</b></td></tr>
<tr><td><b>enddo</b></td></tr>
</table>
</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</td><td width=1 bgcolor=black>
</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>
<table valign=c>
<tr><td><b>When</b> &nbsp;<i>requirement_specification</i> &nbsp;&nbsp;<b>{</b> &nbsp;</td></tr>
<tr><td>  &nbsp;  &nbsp;<b>.&nbsp;&nbsp;.&nbsp;&nbsp;.</b></td></tr>
<tr><td><b>}</b></td></tr>
</table>
</td></tr>
</table>

where multiple [CAMP] or [EPICS] setting commands are surrounded
by "<b>do</b>`...`<b>enddo</b>", or their equivalents, curly braces
"<b>{</b>`...`<b>}</b>", and controlled by a single `When` command.
For example,

{% highlight bash %}
When /Hall/field stable within .5 {
   setCamp /field_cont/setpoint </Hall/field>
   setCamp /field_cont/function 2
}
{% endhighlight %}

Note which commands go on separate lines in this example.
You cannot combine those multiple lines onto one.


[MIDAS]: https://en.wikipedia.org/wiki/Maximum_Integrated_Data_Acquisition_System
[EPICS]: https://en.wikipedia.org/wiki/EPICS
[CAMP]: https://daq-plone.triumf.ca/SR/CAMP%20%28MUSR%29/
