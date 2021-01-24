---
layout: default
title: Software Manager's Guide
description: MUD Software Manager's Guide.
parent: MUD
---

# Software Manager's Guide
{: .no_toc }

<i>
This page is a reproduction of the content found at
[http://cmms.triumf.ca/mud/mud_managers.html](http://cmms.triumf.ca/mud/mud_managers.html "MUD Software Manager's Guide").
Though this is mainly to test the formatting of the markdown-to-html convension,
I have made minor changes thoughout the text to improve readability.
</i>

## Table of Contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Location of Files

The sources for MUD are kept in a [CVS repository],
which may be read over the [World Wide Web].

The subdirectories are explained as follows:

- `lib/`: library for reading and writing the data format.
- `bin/`: location of executable programs.
- `src/`: library sources.
- `util/`: sources for file conversion/dump utility `mud_util`.
- `extra/`: extra utility programs.
- `cmt/`: comment manager program (not used). 

The file `mud.zip` should contain the
sources necessary for building the library and
file conversion utility on any supported platform.
See the MUD
[Installation Guide]({% link bnmr/mud/installation-guide.md %})
for more details on installing MUD.

## Extending the Format

You may wish to extend the library with a
new section tailored to your lab or experiment type.
You will need to edit a few files in, and probably add one file to,
the directory `mud/src`.
The procedure is as follows:

1. Allocate Lab, Format and Section identifiers in the file `mud.h`.
   If your lab or format are already defined, do not allocate new numbers,
   but the new Section number must be unique. If the new MUD Section definition
   is of general interest to the µSR community, a Section ID should be chosen,
   with the agreement of other labs,
   incorporating the Generic ID rather than the local Lab ID.
   Follow the format of the other Section types.
   Similarly, add this identifier to the Fortran include files
   (`mud.f90`, `mud.f77`, `mud.finc`) to maintain Fortran compatibility.
2. Also in the file `mud.h`, add the definition of the structure
   (e.g., `MUD_SEC_GEN_HIST_DAT`)
   following the examples of the other definitions.
   The structure must begin with the member `MUD_CORE core;`.
   Similarly, add this structure definition to the Fortran include files
   (`mud.f90` and `mud.finc`).
3. Further down in the file `mud.h`,
   add a forward declaration of the procedure to read your new Section type
   (e.g., `MUD_SEC_TRI_TI_RUN_DESC_proc`).
   Similarly, add this forward declaration to
   the Fortran include file `mud.finc`.
4. In the module `mud_new.c`, add an entry in the switch statement of the
   procedure `mud_new` for your new section type.
   This routine allocates space for newly created sections.
5. Write the routine to read, write, etc., the new Section type in a new module.
   The name of the routine will be the same as the forward declaration in
   `mud.h` mentioned above.
   Take a look at the module `mud_tri_ti.c` for an example of how to do this.
   This routine should be able to free, read, write, get the size of,
   and display the contents of the Section.
   It should use the the routines provided to encode and decode data from the
   file to the platform-specific format (which is detected automatically).
6. Add the module to the `OBJS` list in the makefiles
   `descrip.mms`, `makefile.`, `makefile.dos`, and `makefile.linux`.
   Then, rebuild the installation zip file.
   This is the latest installation file for all platforms.

[CVS repository]: https://dasdevpc2.triumf.ca/cgi-bin/cvsweb.cgi/mud/?cvsroot=MUSR
[World Wide Web]: https://en.wikipedia.org/wiki/World_Wide_Web
