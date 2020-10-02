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
This is mainly a test of the quality of text formatting.
</i>

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

The automatic run control operates as a separate process, distinct
from other data acquisition front-ends and back-ends, including the
run-control user-interface.  It should be 
started automatically, but if it is not, then one can execute 
`$MUSR_DIR/musr_midas/mui/autoruns.tcl`.
The autorun server is controlled by a few parameters in the ODB, under 
`/autorun`, but it is mostly controlled by the auto-run plan file, which
it monitors continuously for changes.

(The ODB is the [MIDAS] data acquisition system's central storage of experiment
parameters.  It can be explored and edited using the `odbedit` 
program or a web browser.)

## Control Panel

The custom web page for bnmr and bnqr experiments includes an area
for controlling autorun parameters.  (If there are problems setting
parameters from the main control page, you may try to set them by 
navigating the odb tree.)

Edit the plan file in your preferred text editor. Every time it is saved,
the autorun program re-reads it.

If there are problems with the syntax of a plan file, the autorun processor 
usually only reports the first error it encounters.  Check the [MIDAS]
message log for error messages. There is also a stand-alone command, 
`checkplan` (executing `$MUSR_DIR/musr_midas/mui/checkplan.tcl`; usage

&ldquo;checkplan&nbsp;&nbsp;<i>filename</i>&nbsp;&nbsp;[<i>first_run</i>]&rdquo;)
that performs checks on a plan file, useful for verifying a hand-edited plan.
Nevertheless, the autorun processor may encounter some errors that the preliminary 
scan does not detect, so these checks will not completely replace a good proofread.

## Auto-run Control Parameters

There are a few parameters to set on the autorun control panel.
Most of these are passed to the autorun processor through the [MIDAS] ODB (in the area “/autorun”).


<p>
<strong>Autoruns Operation Enabled</strong><br>
ODB:&nbsp; /autorun/enable,&nbsp; boolean (1/0)<br>
Set this to control whether the autorun process operates at all.  It does not actually
shut down when disabled, but it checks only this parameter, waiting
to be enabled again.
<p>
<strong>Autorun State</strong>&nbsp; Autoruns status read-back<br>
ODB:&nbsp; /autorun/state, &nbsp; int &nbsp; interpreted as:<br>
<table border=0 cellpadding=0 cellspacing=0>
<tr><td>&nbsp; &nbsp; 0 &nbsp; </td><td> disabled&nbsp; &nbsp; </td><td>Operation is not enabled</td></tr>
<tr><td>&nbsp; &nbsp; 1 &nbsp; </td><td> idle&nbsp; &nbsp; </td><td>Waiting for a plan</td></tr>
<tr><td>&nbsp; &nbsp; 2 &nbsp; </td><td> acquiring&nbsp; &nbsp; </td><td>Run is in progress and active</td></tr>
<tr><td>&nbsp; &nbsp; 3 &nbsp; </td><td> paused&nbsp; &nbsp; </td><td>Run is paused</td></tr>
<tr><td>&nbsp; &nbsp; 4 &nbsp; </td><td> ending&nbsp; &nbsp; </td><td>Ending a run</td></tr>
<tr><td>&nbsp; &nbsp; 5 &nbsp; </td><td> stopped&nbsp; &nbsp; </td><td>Run has ended</td></tr>
<tr><td>&nbsp; &nbsp; 6 &nbsp; </td><td> setting&nbsp; &nbsp; </td><td>Setting Camp variables</td></tr>
<tr><td>&nbsp; &nbsp; 7 &nbsp; </td><td> changing&nbsp; &nbsp; </td><td>Waiting for &ldquo;requirements&rdquo;</td></tr>
<tr><td>&nbsp; &nbsp; 8 &nbsp; </td><td> starting&nbsp; &nbsp; </td><td>Starting a new run</td></tr>
<tr><td>&nbsp; &nbsp; 9 &nbsp; </td><td> reload&nbsp; &nbsp; </td><td>Trigger reload of plan file</td></tr>
</table>
<p>
Most state values are set by the autorun server, strictly for monitoring its 
progress, but a value of &lquo;reload&rquo;&nbsp;(9) may be set by other clients to force
the autorun server to re-read the plan file, and perhaps resume processing
after being idle&nbsp;(1); the Reload&amp;Start button will trigger reloading this way.
(The other way to force a reload is to modify the plan file itself, perhaps 
like <code>touch plan.dat</code>.)
<p>
<strong>Plan file</strong>&nbsp; Full file specification for the run plan<br>
ODB:&nbsp; /autorun/plan file, &nbsp; string<br>
The autorun processor watches this file for changes, and if any occur, it
re-reads the run plan.
<p>
<strong>Pausing Runs</strong>&nbsp; Enable/Disable run pausing<br>
ODB:&nbsp; /autorun/enable pausing, &nbsp; boolean-int (1/0)<br>
Tells the autoruns processor whether to keep checking requirements after
starting a run, and to pause the run while requirements are not
satisfied.  See below for &ldquo;Requirements&rdquo; in an autorun plan.
(A [CAMP] alarm with a hardware veto gives better response.)
<p>
<strong>Refresh Period</strong>&nbsp; Cycle time of autorun processor<br>
ODB:&nbsp; /autorun/refresh seconds, &nbsp; int<br>
Tells how often the autorun processor checks status and looks for a new plan.
Sensible values range from 5 to 30 seconds.
<p>
<strong>Target Cycles</strong>&nbsp; Desired total cycles for TD/Type-2 runs<br>
ODB:&nbsp; /autorun/target cycles, &nbsp; int<br>
Tells how many frontend cycles to run for Type-2 modes. (This parameter
applies to any runs, not just automatic runs.)
<p>
<strong>Target Counts</strong>&nbsp; Desired total counts for TD/Type-2 runs<br>
ODB:&nbsp; /autorun/target counts, &nbsp; int<br>
Tells how many events to accumulate in histograms before ending the run. This number is 
reset for every run, according to the run plan setting (if that run has a &ldquo;counts&rdquo
setting in the plan), but it can be changed during the run to take more or less data.
<p>
<strong>Count Histogram</strong>&nbsp; What &ldquo;Target Counts&rdquo; applies to<br>
ODB:&nbsp; /autorun/count histogram, &nbsp; int<br>
The &ldquo;Target Counts&rdquo; may be compared with the counts in any particular 
histogram or with the total of all histograms, as indicated by the &ldquo;Count 
Histogram&rdquo; setting. The first histogram is number 1. Enter zero or negative 
to use the total of all histograms.
<p>
<strong>Time Limit (minutes)</strong>&nbsp; Maximum time before ending a run<br>
ODB:&nbsp; /autorun/time limit (minutes), &nbsp; float<br>
You may enter the time limit in various formats, but the value will be
displayed and saved as a number of minutes.  Use a very high value or
zero if there is to be no time limit.  Between runs, this value may
be reset by any specifications in the run plan. It can be manually changed
during a run without editing the plan.
<p>
<strong>Reload &amp; Start</strong>&nbsp; Apply the settings.<br>
If autoruns are enabled, but idle, then force reloading the plan, 
even if the plan file hasn't changed. 
<p>

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

Commands may be broken across multiple lines 
by ending the partial line(s) with `\`.


Lines that begin with certain characters (`!#%;`) are comments, and are ignored,
as are blank lines.


In the command syntax below, <b>bold</b> indicates a literal keyword,
<i>italics</i> indicate some sort of value, 
&ldquo;|&rdquo; separates multiple possibilities, 
and &ldquo;[ ]&rdquo; brackets indicate some optional parameter.  
The &ldquo;|&rdquo;, &ldquo;[&rdquo;, and &ldquo;]&rdquo; characters 
should not be typed into a run plan!
<p>

One command, <b>Run</b>, is absolutely required, and it comes first:
<p>
<b>Run</b> &nbsp;<i>number</i><br>
<b>Run</b> &nbsp;<b>next</b><br>
<b>Next</b> &nbsp;<b>run</b>
<p>
The Run command begins the commands for that particular run; all ensuing 
commands apply to that run, until the next Run command.  
The specified run number must be consecutive with the previous. You
can use the <b>next</b> keyword instead of a number, but the first 
run must be explicitly numbered.  (The reason the numbering must
be defined is so that the plan can be edited and reloaded in the
middle, without having to remove all the runs that have already been
performed.)
<p>
If there are settings to be made after the last run has completed, use
<p>
<b>Finally</b>
<p>
to separate those settings from the preceding run; it is like a Run command, but
no run will be performed.
<p>

The remaining commands can be in any order.
<p>
In the case of TI (type-1) runs, there is the required sweep range:
<p>
<b>SweepRange</b> &nbsp;<i>from</i> &nbsp;<i>delim</i> &nbsp;<i>to</i> 
      &nbsp;<i>delim</i> &nbsp;<i>step</i>
<p>
The delimiter <i>delim</i> signifies white-space and/or punctuation
characters or even any of the letters in &ldquo;toby&rdquo;; &nbsp; e.g.,&nbsp;
&ldquo;<code>10,100:2</code>&rdquo;&nbsp; or&nbsp; 
&ldquo;<code>5000 7000 500</code>&rdquo;&nbsp; 
or&nbsp; &ldquo;<code>1 to 10 by 1</code>&rdquo;.  People might 
try to use&nbsp; &ldquo;<code>200-300:10</code>&rdquo;&nbsp; for a range, 
but &ldquo;-&rdquo; is <em>not</em> a legal delimiter since the dangers of 
misinterpreting a minus sign are too great.  
All the values (<i>from</i>, <i>to</i>, <i>step</i>) are integers.
<p>

Other commands (all the commands listed below) are strictly optional, 
and, if omitted, they retain the previous settings; that is, the values 
will not be actively set to any values, but will be retained by the 
respective [MIDAS] or [CAMP] systems.  
<p>
There are four possible commands to control when the run should be
ended:
<p>
<table border=0 cellspacing=0 cellpadding=0>
<tr><td><b>Counts</b> &nbsp;<i>number</i> [ <b>M</b> ] &nbsp;[ <i>hist_number</i> ] </td><td> &nbsp;&nbsp; ( for TD )</td></tr>
<tr><td><b>Time_limit</b> &nbsp;<i>elapsed_time</i></td><td> &nbsp;&nbsp;&nbsp; ( for TD or I )</td></tr>
<tr><td><b>Sweeps</b> &nbsp;<i>number_of_sweeps</i></td><td> &nbsp;&nbsp;&nbsp; ( for I )</td></tr>
<tr><td><b>Cycles</b> &nbsp;<i>number_of_cycles</i></td><td> &nbsp;&nbsp;&nbsp; ( for TD )</td></tr>
</table>
<p>
Typically, one should use Counts to tell the total number of events 
to accumulate in a TD/Type-2 run; it can be given in &ldquo;real&rdquo; 
number form, and with an optional &ldquo;M&rdquo; suffix to indicate 
&ldquo;millions&rdquo; (e.g., 3200000, 32e5, and 3.2M are all the same).  
This parameter will replace the value in the ODB at the beginning of a run,  
but a user may manually change it in the ODB while the run is in progress, 
which is the best way to extend an automatic run in progress. If no Counts 
command is given for a run, the existing value of 
&ldquo;/autorun/total&nbsp;counts&rdquo; from the ODB  is kept.  
If the optional <i>hist_number</i> is specified, then the counts
are checked for that histogram only, rather than the total of all histograms.
<p>
The Time_limit setting (with alias &ldquo;Elapsed&rdquo;) tells the longest time that 
may be spent on a run.
The <i>elapsed_time</i> can be in many formats, and a simple number is interpreted
as minutes; all of the following are equal:&nbsp; 1:30,&nbsp; 5400&nbsp;s,&nbsp; 
90&nbsp;min,&nbsp; 1.5hr,&nbsp; 01:30:00,&nbsp; 90.&nbsp;
Units are any strings that begin with &ldquo;s&rdquo;, &ldquo;m&rdquo;, or &ldquo;h&rdquo;.  
Notice that &ldquo;1:30&rdquo; means 1.5 hours, not 1.5 minutes!  For 1.5 minutes 
you would need &ldquo;0:01:30&rdquo; (or &ldquo;1.5 min&rdquo; or &ldquo;90s&rdquo;).  
You can specify both counts and time limits, in which case the run ends when either 
is satisfied. Note that using an elapsed-time limit may result in runs with no data 
if the beam is off for a long time.  
<p>
The Sweeps command is for TI runs only, and tells how many sweeps 
to make.  It updates the corresponding parameter in the ODB:
&ldquo;/Equipment/MUSR_I_acq/settings/input/num&nbsp;sweeps&rdquo;, which 
applies to any run, not only auto-runs.
<p>
The Cycles command is for TD runs only, and tells how many cycles to perform.
It applies to all runs, even when autoruns are disabled or idle.
<p>
Arrange to have autorun error and warning messages forwarded by email with
<p>
<b>Email</b> &nbsp;<i>addr</i>&nbsp; [ <b>,</b> <i>addr</i> <code>...</code> ]
<p>
providing a list of email addresses, separated by commas.  When there are problems,
the corresponding messages will be emailed to these addresses.  If you have an
address that gets forwarded to a cell phone or pager, that would be good to use.
<p>
Several commands apply to the run headers, corresponding to the [MIDAS]
&ldquo;edit on start&rdquo; variables.
<p>
<b>Sample</b> &nbsp; <code> ...</code><br>
<b>Orientation</b> &nbsp; <code> ...</code><br>
<b>Operator</b> &nbsp; <code> ...</code><br>
<b>Experiment</b> &nbsp; <i>number</i><br>
<b>Temperature</b> &nbsp; <i>temperature</i> &nbsp;| &nbsp;<i>Camp_var</i><br>
<b>Field</b> &nbsp; &nbsp; <i>field</i> &nbsp;| &nbsp;<i>Camp_var</i>
<p>
Note that temperature and field may be entered as numbers (with implicit
units of Kelvin and Gauss), as numbers with units (provided the conversion
to Kelvin or Gauss is known to the program), or as a the full [CAMP] path
for a temperature or field variable.
<p>
<b>Title: </b> &nbsp; <code> ...</code>
<p>
The run title allows automatic insertion of other header fields using the tags 
&lt;Sample>, &lt;Operator>, &lt;Experiment>, &lt;Temperature>, &lt;Field>, and 
&lt;Orientation> (yes, you type the &lquo;angle brackets&rquo; around the tag name).
For example:
<p>
<code>Title: &lt;Sample> annealed, T=&lt;Temperature>, B=&lt;Field> &lt;Orientation>, p=+2%</code>
<p>
The autorun system will replace these tags with the appropriate header
values, both at the beginning of the run and at intervals throughout
the run; this ensures that automatic Temperature and Field headers, as 
well as any manual settings, are propagated to the run title. The system 
will <strong>STOP</strong> updating the title if the user manually sets it to something 
different. 
<p>
For time-integral runs, there is also the percentage tolerance for the beam normalization:
<p>
<b>Tolerance</b> 
    &nbsp; <i>number</i> &nbsp; [ <b>%</b> ]
<p>
(The percent sign is optional, and does not affect the interpretation of
the number.)
<p>

<!-- 
Other acquisition control parameters have no "personalized" commands,
but should be set by loading a previously-saved configuration:
<p>
<b>Mode:</b>  &nbsp;<i>saved_TDmuSR_mode_name</i><br>
<b>Setup:</b> &nbsp;<i>saved_ImuSR_setup</i>
<p>
-->
Any Odb parameter can be set using the SetOdb command:
<p>
<b>SetOdb</b> &nbsp;<i>odb_variable</i>&nbsp; &nbsp;<i>value</i>
<p>
where <i>odb_variable</i> is the full Odb path to the variable, enclosed in
quotes if the name contains any spaces.  The value should also be quoted
if it contains spaces (use double-quotes, not apostrophes).
<p>
You can control some portions of the beamline  or platform:
<p>
<b>SetEpics:</b> &nbsp;<i>Epics_var</i> &nbsp; <i>value</i>
<p>
The SetEpics command (with spelling variants) sets a particular beam element 
to a value.  [EPICS] variables are always in upper case, and contain
colons (&ldquo;:&rdquo;) as separators; they usually begin with the beamline or system name.
To find the <i>Epics_var</i>, go to the beamline [EPICS] control window and click the
middle mouse button on the entry field (blue text) where you would type the value. 
The <i>Epics_var</i> will be displayed in a small pop-up window (the text 
is &ldquo;selected&rdquo;, so you can immediately &ldquo;paste&rdquo; it into
the plan file). The full <i>Epics_var</i> may be abbreviated for some elements
commonly adjusted in autoruns, especially for turning elements on or off.
When switching an element on or off, the <i>value</i> should
be &ldquo;on&rdquo; or &ldquo;off&rdquo; for clarity; thus the examples
<p>
<code>SetEpics:  BNMR:HVBIAS:POS:VOL  16.0</code><br>
<code>SetEpics:  BIAS  16.0</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Short for &beta;NQR's <code>ILE2:BIAS15:VOL</code>)<p>

Make [CAMP] settings using either or both of:
<p>
<b>SetCamp</b> &nbsp;<i>Camp_var</i> &nbsp; <i>value</i><br>
<b>Camp_cmd</b> &nbsp;<i>Camp_command</i>
<p>
(SetCamp has aliases set_camp, camp_set and CampSet, because we all
forget.)
<p>
The <i>Camp_var</i> argument is a complete Camp variable path,
including all slashes, such as &ldquo;/Helios/mag_field&rdquo;.  
<p>
The <i>value</i> argument should be numeric or a text string, as 
appropriate for the particular <i>Camp_var</i>.  Numeric values may be 
given as arithmetic expressions.  For selection variables, one must
use the exact same string as used by Camp, including capitalization, or
an integer index, counting from zero. As a special shortcut, abbreviations 
of the form &lt;<i>Camp_var</i>> (with explicit angle-brackets) may be 
used as (or in) the <i>value</i> argument, indicating that the value of 
another [CAMP] variable should be substituted.  
<p>
The <i>Camp_command</i> is any command (or inline Tcl script) as 
documented in Appendix&nbsp;B of the 
<a href=http://cmms.triumf.ca/software/camp_soft.pdf>Camp Software Manual</a>.
<p>
Examples are:
<p>
<code>SetCamp:  /Magnet/mag_field  0.25</code><br>
<code>SetCamp:  /Sample/control_set  15</code><br>
<code>SetCamp:  /Diffuser/control_set  &lt;/Sample/control_set> - 0.5</code><br>
<code>SetCamp:  /field_control/setpoint  &lt;/Hall/field></code><br>
<code>SetCamp:  /Diffuser/heat_range MED</code><br>
<code>camp_cmd: insLoad /defibrulator medical.kit</code>
<p>


The autorun controller will perform all those [CAMP] and [EPICS] commands at once,
as soon as the preceding run has ended.  This doesn't meet the full
needs for setting [CAMP] devices, particularly in cases such as the 
field control example above, where one would like to reference the
/Hall/field value after the magnet has stabilized.  One way to handle
this is to schedule some settings after a fixed time delay:
<p>
<b>After</b> <i>elapsed_time</i>&nbsp;<b>:</b> 
    &nbsp;<b>SetCamp &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;|
    &nbsp;<b>camp_cmd &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;| 
    &nbsp;<b>SetEpics &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;| 
    &nbsp;<b>AutoTune &nbsp;.&nbsp;.&nbsp;.</b> &nbsp;|
<p>
where the forms of <i>elapsed_time</i> is similar to the run time-limit, except that a bare
number is interpreted as <em>seconds</em> (six minutes could be given by any of
6m, 0:06, 0.1h, 360s, 360). This is the first of two 
composite commands, where a <em>required</em> colon (:) must separate the &ldquo;After&rdquo;
declaration from the ensuing, delayed, command.  Note that only some commands can 
be deferred with After; any others give a syntax error (because they aren't allowed).
<p>
Before a run can begin, we must know that the experimental conditions 
have responded to the device settings, so we specify &ldquo;requirements&rdquo;
<p>
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
<p>
The run will not begin until every requirement is satisfied simultaneously, 
<strong>and there are no [CAMP] alarms active</strong>.  (Thus, you can enforce many typical 
constraints by setting alarms in [CAMP], rather than giving requirement commands.)
<p>
Each <i>Variable</i> is the full path specification of a [CAMP] variable, such as
&ldquo;<code>/Sample/sample_read</code>&rdquo;, or an [EPICS] variable, such as 
&ldquo;<code>M20:S1:HVNEG:VOL</code>&rdquo;
(distinguished by the presense of <code>/</code> or <code>:</code>).
<p>
For numeric variables, one should usually use the &ldquo;stable&rdquo; form of the command.  
The autorun system will collect values of the primary <i>Variable</i>, retaining those over 
the latest <i>elapsed_time</i>.  To satisfy the requirement, all retained values must be 
within <i>error</i> of either: the latest value (blank comparison fields), or the 
given <i>number</i> (&ldquo;at&rdquo;), or the current value of the comparison variable 
(&ldquo;equal&rdquo;).  (Notice that&nbsp; <code>Require /foo/bar stable</code>&nbsp; is the 
same as&nbsp; <code>Require /foo/bar stable equal /foo/bar</code>.)
<p>
The default <i>elapsed_time</i>, if none was specified, is 1&nbsp;second (almost 
immediately). The default units, if a bare number was given, is seconds.
<p>
Numeric variables can also be tested to be &ldquo;above&rdquo; or &ldquo;below&rdquo; some value.
<p>
For string or selection variables, use the &ldquo;is&rdquo; form for the requirement.  
If the <i>string</i> contains spaces, then it should be quoted.
<p>
Examples:
<p>
<code>Require /diffuser/control_read  stable  equal  /diffuser/control_set  within  0.5 </code><br>
<code>Require /sample/sample_read  stable  within 0.5  for  2 m</code><br>
<code>Require /Hall_Probe/field  stable  at  1.0  for  30</code><br>
<code>Require /shield/sample_read below 100</code><br>
<code>Require M20:EXPT:RDCUR  stable  equal  M20:EXPT:CUR  within  2</code><br>
<code>Require /Magnet/ramp_status  is  Persistent</code>
<p>
(Note that the last example specifies &ldquo;Persistent&rdquo;; &ldquo;persistent&rdquo; 
would not work because the actual value in [CAMP] is capitalized. Make sure the requirement 
string exactly matches what [CAMP] displays.)
<p>
Here is another example, part of a temperature scan, where the desired temperature
is specified just <emph>once</emph>, on the diffuser set-point.  
<p>
<code>Run  1234</code><br>
<code>Title  &lt;Sample>, &lt;Temperature>, automatically</code><br>
<code>Temperature  /sample/sample_read</code><br>
<code>Require  /sample/sample_read stable equal /diffuser/control_set within 3</code><br>
<code>Require  /sample/sample_read stable within 0.5 for 2m</code><br>
<code>Setcamp  /diffuser/control_set   22</code>
<p>
The run will begin when the sample temperature levels off (within 0.5&nbsp;K) for
2&nbsp;minutes, and within 3&nbsp;K of the diffuser setpoint (i.e., between 19 and 25&nbsp;K).
Whatever the average sample temperature is, over the course of the run, it will be recorded 
in the temperature field of the run header, and thence the run title of the data file.
Note that, in this example as always, the Setcamp command is performed before ever
checking requirements; entering the Setcamp declaration after the requirements does
<em>not</em> imply that the settings are performed after requirements are satisfied.
For that feature, see the When command.
<p>
<b>Max_wait</b> &nbsp;<i>elapsed_time</i>
<p>
In case of conflicting requirements, or some other problem where the requirements
are never satisfied, there is a Max_wait command.  After waiting for <i>elapsed_time</i>,
the autorun sequencer will start the next run even if the requirements are not satisfied.
The various formats for <i>elapsed_time</i> are that same as on the Time_limit command,
with default units of minutes (see above).
<p>
For greater control over the timing of Camp settings than is provided by the After command,
one can schedule them the same way as specifying a requirement:
<p>
<b>When</b> &nbsp;<i>requirement_specification</i> 
    &nbsp;<b>:</b> 
  &nbsp;<b>SetCamp</b> &nbsp; <code>...</code> &nbsp;| 
  &nbsp;<b>camp_cmd</b>  &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>SetEpics</b>  &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>AutoTune</b> &nbsp; <code>...</code> &nbsp;|
  &nbsp;<b>After</b> &nbsp; <code>...</code> &nbsp;|
  &nbsp;<i>blank</i>
<p>
The <i>requirement_specification</i> is any valid parameter list for the Require 
command (above), and is followed by a mandatory colon separator. Only the device 
setting commands for [CAMP] and [EPICS] (SetCamp, SetEpics, camp_cmd, and their aliases) 
and the After command may be scheduled this way. You can also specify a null action 
with no scheduled command, which behaves like a simple Require command except... 
<p>
Conditions specified by When must all be satisfied at some point
<em>before</em> a run can begin, but they need not <em>remain</em> satisfied
until the run begins.  This makes a When command with a null action subtly
different from the same Require command: all Require conditions must be
simultaneously satisfied when the run begins, whereas all When actions (or
null actions) must have been performed sometime before the run begins.
<p>
If a [CAMP] setting must be delayed until after the run begins, then you must use 
an After command, either alone or scheduled by a When command, like
<p>
<code>When &nbsp;/sample/sample_read&nbsp;stable&nbsp;within&nbsp;.5&nbsp;:&nbsp;After&nbsp;5m:&nbsp;setCamp&nbsp;/sample/setup/P 20</code>
<p>
A typical use is to start controlling a variable after a previous setting is 
complete:
<p>
<code>When&nbsp;/Hall/field&nbsp;stable&nbsp;within&nbsp;.5:&nbsp;setCamp&nbsp;/field_cont/setpoint&nbsp;&lt;/Hall/field></code><br>
<code>When&nbsp;/Hall/field&nbsp;stable&nbsp;within&nbsp;.5:&nbsp;setCamp&nbsp;/field_cont/function&nbsp;2</code><br>
<code>When&nbsp;/sample/sample_read&nbsp;below&nbsp;8:&nbsp;setCamp&nbsp;/sample/heat_range&nbsp;LOW</code><br>
<code>When&nbsp;/diffuser/sample_read&nbsp;stable&nbsp;equal&nbsp;/diffuser/control_set&nbsp;within&nbsp;1&nbsp;for&nbsp;1.5m:&nbsp;\</code><br>
<code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After&nbsp;3m:&nbsp;setCamp&nbsp;/nv_cont/function&nbsp;2</code>
<p>
(Note the use of <code>\</code> to join multiple lines when commands get too long,
and the substitution for the current value of the field readback.)
This example turns on (feedback) field control when the magnet current reaches its
setpoint, and turns on needle-valve control three minutes after the cryostat
diffuser temperature gets close to its setpoint.  Notably, it also specifies the
same requirements for beginning the run;  thus, presuming the (diffuser) temperature
is the last to stabilize, the needle-valve control will begin about three minutes
after the run begins. 
<p>
In the example (and in practice) note the use of multiple When commands having the
same requirement but different actions.  To save typing and computer processing, these can
be written as a <em>block</em>
<p>
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
<p>
where multiple [CAMP] or [EPICS] setting commands are surrounded
by &ldquo;<b>do</b><code>...</code><b>enddo</b>&rdquo;, or their equivalents, curly braces
&ldquo;<b>{</b><code>...</code><b>}</b>&rdquo;, and controlled by a single When 
command.  For example,
```
When /Hall/field stable within .5 {
   setCamp /field_cont/setpoint </Hall/field>
   setCamp /field_cont/function 2
}
```
Note which commands go on separate lines in this example.  You cannot combine
those multiple lines onto one.

<p><p>
That completes the definition of the plan file.  Please relate your experiences, 
frustrations, and suggestions to Donald.

[MIDAS]: https://en.wikipedia.org/wiki/Maximum_Integrated_Data_Acquisition_System
[EPICS]: https://en.wikipedia.org/wiki/EPICS
[CAMP]: https://daq-plone.triumf.ca/SR/CAMP%20%28MUSR%29/
