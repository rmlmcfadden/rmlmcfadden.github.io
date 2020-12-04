---
layout: default
title: Data File Format
description: MUD Data File format.
parent: MUD
grand_parent: β-NMR
---

# Data File Format
{: .no_toc }

<i>
This page is a reproduction of the content found at
[http://cmms.triumf.ca/mud/mud_fmt.html](http://cmms.triumf.ca/mud/mud_fmt.html "MUD Data Format").
Though this is mainly to test the formatting of the markdown-to-html convension,
I have made minor changes thoughout the text to improve readability.
</i>

## Table of Contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Overview

The MUon Data (MUD) format used at [TRIUMF] is an
efficent framework for storing and retrieving μSR data.
Its existing structure is optimized for μSR data,
but the basic framework is universal and the definition is extensible,
so it can grow to meet new demands.

The MUD format is characterized by the organization of data into Sections.
The instance of each Section is defined by two long integers:
the Type identification (`secID`) and
a number specifying the instance of the type (`instanceID`).
The format has been designed to allow for quick implementation of
new Section types or modifications of old types,
high flexibility while maintaining a standard,
and ease of use for the application programmer.
Type identifiers can be assigned to
new Section types used for applications local to a lab,
but the ideal is to have shared data type specifications,
with generally-accepted ID codes.
To this end,
ranges of `secID` numbers are reserved for individual laboratories,
to prevent conflicts of local definitions,
and there is a range for generic `secID`s whose definitions can be collected
(at [TRIUMF]) and distributed with the MUD program libraries.

## File Contents

A MUD format data file consists of
sequential contiguous Sections in a stream file.
Common to all types of MUD Section is a small Core structure giving
Section type and instance, size, and a pointer to the next Section.
This design, with the relative file position of the
next Section encoded into the Core part of each Section,
allows for traversal of the file and for the modification of
the contents of a Section type while maintaining backwards compatibility in
the case of unknown new Section types.

Sections of any combination of types may be organized into Groups.
The Group is simply a class of MUD Section which indicates that
a number of following Sections are to be grouped together.
The Group provides an index of (relative file position)
pointers to those ensuing Sections,
which may be thought of as being contained within the Group Section.
The whole MUD file is a particular case of a MUD group.

The most important MUD Sections are those that hold data,
and the `secID` implies how to read that data.
Not only the content and the organization,
but also the encoding are specified by the definition of the Section type.
A specific `secID` implies a specific
data layout as well as specific byte order,
floating-point format (although floating-point should be avoided),
or character encoding for that section;
using, say, a different character encoding requires a
different `secID` so the data can be read without confusion.
The MUD library includes standard routines to read the
file's encoding into the computer's native format.

## Copying MUD files

MUD files are pure binary streams, without any record format.
This is attractive for moving files between operating systems,
some of which have no concept of file records.
On [VMS] systems, with a rich repertoire of record types,
MUD files are typically called "stream LF" because
that is what C programs automatically produce,
even though the correct type should be "stream".
[FTP] transfer between [VMS] and [Unix] systems does not work well,
because it usually assumes a particular record format
(fixed 512 byte records) on the [VMS] end.
To use [FTP] one should first "zip" the files, and transfer the zip archive.
NFS works well.

## Software Library/Applications

It is intended that the data be accessed via the set of
supplied routines for reading and writing the MUD format.
There are both high-level ([API]) routines for
accessing particular components of existing MUD Sections,
and low-level routines used to implement the [API] or
to read and write MUD files directly.
If such low-level access is desired,
inspection of the (C language) source code (which is not extensive)
should reveal the necessary information.

## Defining New Types

The specification of a Section type includes the following steps:

1. Definition of a structure in C and, optionally,
   a corresponding structure in Fortran
   (see [Sample MUD Format Structure](#sample-mud-format-structure)).
2. Writing one C subroutine that handles the specifics of the reading,
   writing, and management of the Section, in a brief and well-defined manner
   (see [Subroutine to Handle the Section Type](#subroutine-to-handle-the-section-type)).
3. Adding an entry to the C subroutine that dynamically creates instances of
   each Section.
4. Reserving the unique 32-bit integer identifier(s) for the new type.
5. Finally, (optionally) adding the corresponding "friendly" [API] functions.

The Section definition and its ID should be contributed to the
centralized library (maintained at [TRIUMF]),
allowing all MUD-aware applications to understand them.

Applications may be written in C or Fortran and linked to the MUD library,
although the natural language is C for low-level access.
In C, the Sections may be written from a linked list of structures.
Routines are available for the creation of Sections and maintaining the list.
In both languages, the entire file may be read into a linked list,
and then search routines are used to access specific Sections of the list
(see [Sample Application in C](#sample-application-in-c)).
Alternatively, the I/O of each Section may be done separately,
also in both languages
(see [Sample Applications in Fortran](#sample-applications-in-fortran)).
Access to individual Sections in the data file may be
sequential or pseudo-direct.
The pseudo-direct access involves the call to a
routine with the request for a Section of a certain ID;
the routine then searches the file (as a linked list)
from the current position for the requested Section and
positions the file pointer to the beginning of this Section.

## Programming Examples

Here are some programming examples using the MUD library routines.
For information on using the higher-level access routines,
see the MUD [Programmer's Guide]({% link bnmr/mud/programmers-guide.md %}).

### Sample MUD Format Structure

Sample MUD format structure for C (from `mud.h`):

{% highlight c %}
typedef struct {
    MUD_CORE    core;
    UINT32  ID;
    UINT32  prevReplyID;
    UINT32  nextReplyID;
    TIME    time;
    char*   author;
    char*   title;
    char*   comment;
} MUD_SEC_CMT;
{% endhighlight %}

The same structure for [VAX] Fortran (from `mud.finc`):

{% highlight fortran %}
structure /MUD_SEC_CMT/
   record /MUD_CORE/ core
   integer*4  ID
   integer*4  prevReplyID
   integer*4  nextReplyID
   integer*4  time
   integer*4  pcsAuthor
   integer*4  pcsTitle
   integer*4  pcsComment
end structure
{% endhighlight %}

The same structure for Fortran 90/95 (from `mud.f90`):

{% highlight fortran %}
type MUD_SEC_CMT
   sequence
   type(MUD_CORE) core
   integer(mf_i4)  ID
   integer(mf_i4)  prevReplyID
   integer(mf_i4)  nextReplyID
   integer(mf_i4)  time
   integer(mf_i4)  pcsAuthor
   integer(mf_i4)  pcsTitle
   integer(mf_i4)  pcsComment
end type
{% endhighlight %}

Note that the Fortran structures are identical to the C structure,
including the use of pointers to strings.
Subroutines are provided for conversion between these pointers and
ordinary Fortran character variables
(see [Sample Applications in Fortran](#sample-applications-in-fortran),
`fMUD_ctofString`).

### Subroutine to Handle the Section Type

Subroutine to handle the type in
[Sample MUD Format Structure](#sample-mud-format-structure).
The operations to perform are:

{% highlight c %}
MUD_FREE    /* Release memory used by section. */
MUD_DECODE  /* Convert buffer to variables in native format. */
MUD_ENCODE  /* Convert Section in native format to format for file. */
MUD_GETSIZE /* Tell size of Section. */
MUD_SHOW    /* Print diagnostic dump of Section. */
MUD_GETSIZE /* Print textual summary of section (skipping bulk data). */
{% endhighlight %}

The subroutine is:

{% highlight c %}
{% include_relative mud_sec_cmt_proc.c %}
{% endhighlight %}

### Sample Application in C

Sample C application:

{% highlight c %}
{% include_relative mud_test.c %}
{% endhighlight %}

### Sample Applications in Fortran

Modern Fortran:

{% highlight fortran %}
{% include_relative mud_test.f90 %}
{% endhighlight %}

[VAX] Fortran:

{% highlight fortran %}
{% include_relative mud_test.finc %}
{% endhighlight %}

Old (but extended) FORTRAN 77 (`g77`):

{% highlight fortran %}
{% include_relative mud_test.f77 %}
{% endhighlight %}

[API]: https://en.wikipedia.org/wiki/API
[FTP]: https://en.wikipedia.org/wiki/File_Transfer_Protocol
[TRIUMF]: https://www.triumf.ca/
[Unix]: https://en.wikipedia.org/wiki/Unix
[VAX]: https://en.wikipedia.org/wiki/VAX
[VMS]: https://en.wikipedia.org/wiki/OpenVMS
