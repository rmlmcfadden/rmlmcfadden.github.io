---
layout: default
title: Data File Format
description: MUD format.
parent: MUD
grand_parent: TRIUMF
---

# Data File Format
{: .no_toc }

<i>
This page is a reproduction of the content found at
[http://cmms.triumf.ca/mud/mud_fmt.html](http://cmms.triumf.ca/mud/mud_fmt.html "MUD Data Format").
Though this is mainly to test the formatting of the markdown to html convension,
I have made minor changes thoughout the text to improve readability.
</i>

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Overview

The muon data (MUD) format used at TRIUMF is
an efficent framework for storing and retrieving muSR data.
Its existing structure is optimized for muSR data,
but the basic framework is universal and the definition is extensible,
so it can grow to meet new demands.

The MUD format is characterized by the organization of data into Sections.
The instance of each Section is defined by two long integers:
the Type identification (secID) and
a number specifying the instance of the type (instanceID).
The format has been designed to allow for quick implementation of
new Section types or modifications of old types,
high flexibility while maintaining a standard,
and ease of use for the application programmer.
Type identifiers can be assigned to
new Section types used for applications local to a lab,
but the ideal is to have shared data type specifications,
with generally-accepted ID codes.
To this end, ranges of secID numbers are reserved for individual laboratories,
to prevent conflicts of local definitions,
and there is a range for generic secIDs whose definitions can be collected
(at TRIUMF) and distributed with the MUD program libraries.

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
and the secID implies how to read that data.
Not only the content and the organization,
but also the encoding are specified by the definition of the Section type.
A specific secID implies a specific data layout as well as specific byte order,
floating-point format (although floating-point should be avoided),
or character encoding for that section;
using, say, a different character encoding requires a
different secID so the data can be read without confusion.
The MUD library includes standard routines to read the
file's encoding into the computer's native format.

## Copying MUD files

MUD files are pure binary streams, without any record format.
This is attractive for moving files between operating systems,
some of which have no concept of file records.
On VMS systems, with a rich repertoire of record types,
MUD files are typically called "stream LF" because
that is what C programs automatically produce,
even though the correct type should be "stream".
FTP transfer between VMS and Unix systems does not work well,
because it usually assumes a particular record format
(fixed 512 byte records) on the VMS end.
To use FTP one should first "zip" the files, and transfer the zip archive.
NFS works well.

## Software Library/Applications

It is intended that the data be accessed via the set of
supplied routines for reading and writing the MUD format.
There are both high-level (API) routines for
accessing particular components of existing MUD Sections,
and low-level routines used to implement the API or
to read and write MUD files directly.
If such low-level access is desired,
inspection of the (C language) source code (which is not extensive)
should reveal the necessary information.

## Defining New Types

The specification of a Section type includes the following four steps:

1. Definition of a structure in C, and optionally a corresponding structure in Fortran (see Example 1)
2. Writing one C subroutine that handles the specifics of the reading, writing, and management of the Section, in a brief and well-defined manner (Example 2).
3. Adding an entry to the C subroutine that dynamically creates instances of each Section.
4. Reserving the unique 32-bit integer identifier(s) for the new type.
5. Optionally: Adding the corresponding "friendly" API functions. 

The Section definition and its ID should be contributed to the
centralized library (maintained at TRIUMF),
allowing all MUD-aware applications to understand them.

Applications may be written in C or Fortran and linked to the MUD library,
although the natural language is C for low-level access.
In C, the Sections may be written from a linked list of structures.
Routines are available for the creation of Sections and maintaining the list.
In both languages, the entire file may be read into a linked list,
and then search routines are used to access specific Sections of the list
(see Example 3).
Alternatively, the I/O of each Section may be done separately,
also in both languages (see Example 4).
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
see the MUD Programmer's Guide.

    
        Structure declaration in C
        Structure declaration in VAX Fortran
        Structure declaration in Fortran 90/95
        
        Modern Fortran
        VAX Fortran
        Extended Fortran-77 (g77)

### Sample MUD format structure

#### C

Sample MUD format structure for C (from `mud.h`)

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

#### VAX Fortran 

The same structure for VAX Fortran (from `mud.finc`)

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

#### Fortran

The same structure for Fortran 90/95 (from `mud.f90`)

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
ordinary Fortran character variables (see Example 4, `fMUD_ctofString`).

### Subroutine to handle the Section type

Subroutine to handle the type in Example 1.
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
int
MUD_SEC_CMT_proc( op, pBuf, pMUD )
    MUD_OPT op;
    BUF* pBuf;
    MUD_SEC_CMT* pMUD;
{
    int size;
    char tempStr1[32];

    switch( op )
    {
        case MUD_FREE:
            _free( pMUD->author );
            _free( pMUD->title );
            _free( pMUD->comment );
            break;
        case MUD_DECODE:
            decode_4( pBuf, &pMUD->ID );
            decode_4( pBuf, &pMUD->prevReplyID );
            decode_4( pBuf, &pMUD->nextReplyID );
            decode_4( pBuf, &pMUD->time );
            decode_str( pBuf, &pMUD->author );
            decode_str( pBuf, &pMUD->title );
            decode_str( pBuf, &pMUD->comment );
            break;
        case MUD_ENCODE:
            encode_4( pBuf, &pMUD->ID );
            encode_4( pBuf, &pMUD->prevReplyID );
            encode_4( pBuf, &pMUD->nextReplyID );
            encode_4( pBuf, &pMUD->time );
            encode_str( pBuf, &pMUD->author );
            encode_str( pBuf, &pMUD->title );
            encode_str( pBuf, &pMUD->comment );
            break;
        case MUD_GET_SIZE:
            size = 3*sizeof( UINT32 );
            size += 1*sizeof( TIME );
            size += sizeof( MUD_STR_LEN_TYPE ) + _strlen( pMUD->author );
            size += sizeof( MUD_STR_LEN_TYPE ) + _strlen( pMUD->title );
            size += sizeof( MUD_STR_LEN_TYPE ) + _strlen( pMUD->comment );
            return( size );
        case MUD_SHOW:
            printf( "  MUD_SEC_CMT: \n" );
            printf( "    number:[%ld],  prevReply:[%ld],  nextReply:[%ld]\n", 
                        pMUD->ID, pMUD->prevReplyID, pMUD->nextReplyID );
            strcpy( tempStr1, ctime( (time_t*)&pMUD->time ) );
            tempStr1[strlen(tempStr1)-1] = '\0';
            printf( "    time:[%s]\n", tempStr1 );
            if( pMUD->author ) printf( "    author:\"%s\"\n", pMUD->author );
            if( pMUD->title ) printf( "    title:\"%s\"\n", pMUD->title );
            if( pMUD->comment ) printf( "    comment:\"%s\"\n", pMUD->comment );
            break;
        case MUD_HEADS:
            printf( "Comment number %ld.     ", pMUD->ID );
            if( pMUD->prevReplyID > 0 )
              printf("  Re: #%ld.    ", pMUD->prevReplyID );
            if( pMUD->nextReplyID > 0 )
              printf("  Next: #%ld.", pMUD->nextReplyID );
            printf( "\n" );
            strcpy( tempStr1, ctime( (time_t*)&pMUD->time ) );
            tempStr1[strlen(tempStr1)-1] = '\0';
            if( pMUD->author ) printf( "    author: %s,     time: %s\n", pMUD->author, tempStr1 );
            if( pMUD->title ) printf( "    title: %s\n", pMUD->title );
            if( pMUD->comment ) printf( "%s\n", pMUD->comment );
            break;
    }
    return( 1 );
}
{% endhighlight %}

### Sample application in C

Sample C application:

{% highlight c %}
/*
 *  mud_test.c
 */

#include "mud.h"

int
main( void )
{
    FILE* fin;
    FILE* fout;
    MUD_SEC_GRP* pMUD_head = NULL;
    MUD_SEC_GEN_RUN_DESC* pMUD_desc = NULL;
    MUD_SEC_GEN_HIST_HDR* pMUD_hist = NULL;
    UINT32 run_fmt_ID;
    char* filename = "006663.msr";

    /*
     *  Read an MUD format file into a linked list
     */
    fin = MUD_openInput( filename );
    if( fin == NULL ) {
	fprintf( stderr, "failed to open file \"%s\"\n", filename );
        exit( 0 );
    }

    pMUD_head = MUD_readFile( fin );
    fclose( fin );
    if (pMUD_head == NULL) {
      fprintf( stderr, "failed to read file \"%s\"\n", filename );
      exit( 0 );
    }
 
    run_fmt_ID = MUD_instanceID( pMUD_head );
    if (run_fmt_ID == MUD_FMT_TRI_TD_ID) printf( "TRIUMF TD-muSR data\n" ); 
    if (run_fmt_ID == MUD_FMT_TRI_TI_ID) printf( "TRIUMF I-muSR data\n" ) ;

    /*
     *  Access the header for the third histogram, in the TD histogram group,
     *  in the overall data group.
     */
    pMUD_hist = MUD_search( pMUD_head,
                            MUD_SEC_GRP_ID, run_fmt_ID,
                            MUD_SEC_GRP_ID, MUD_GRP_TRI_TD_HIST_ID,
                            MUD_SEC_GEN_HIST_HDR_ID, 3, 
                            0 );
    /*
     *  Alternative but equivalent search starts at the members of
     *  the overall data group.
     */
    pMUD_hist = MUD_search( pMUD_head->pMem,
                            MUD_SEC_GRP_ID, MUD_GRP_TRI_TD_HIST_ID,
                            MUD_SEC_GEN_HIST_HDR_ID, 3, 
                            0 );

    if (pMUD_hist == NULL) {
      fprintf( stderr, "could not find a histogram 3\n" );
      exit( 0 );
    }
    printf( "Number of bins in histogram 3: %d\n", pMUD_hist->nBins );

    /*
     *  Add a second ("2") run description section to the list (silly nonsense)
     */
    pMUD_desc = (MUD_SEC_GEN_RUN_DESC*)MUD_new( MUD_SEC_GEN_RUN_DESC_ID, 2 );
    MUD_addToGroup( pMUD_head, pMUD_desc );

    /*
     :
     :  Do something not silly here
     :
     */

    /*
     *  Write MUD format file over the same filename (replace original)
     */
    fout = MUD_openOutput( filename );
    if( fout == NULL ) exit( 0 );

    MUD_writeFile( fout, pMUD_head );

    fclose( fout );

    /*
     *  Free the linked list
     */
    MUD_free( pMUD_head );
}

/*
 *  end mud_test.c
 */
{% endhighlight %}

### Sample application in Fortran

Sample Fortran applications:

#### Modern Fortran

{% highlight fortran %}
        program mud_test_fortran
        implicit none

        include 'mud.f90'

        integer, parameter :: i4 = selected_int_kind(9) ! integer*4

        integer(kind=i4) status
        integer(kind=i4) i
        character(len=32) filename
        integer(kind=i4) fileHandle
        character(len=20) title

        type(MUD_SEC_GEN_HIST_HDR) MUD_hist_hdr(32)


        !
        !  Open an MUD format file
        !
        filename = '001234.msr'

        fileHandle = fMUD_openInput( filename )
        if (fileHandle .eq. 0) then
           write (*,*) 'Could not open file ',filename, &
               '  (',fileHandle,')'
           stop
        endif
        write (*,*) 'Opened file ', filename

        !
        !  Position the file before the first histogram of the 
        !  TD histogram group
        !
        status = fMUD_fseek( fileHandle, &
                            MUD_SEC_GRP_ID, MUD_GRP_TRI_TD_HIST_ID, &
                            0, 0 )
        if( status .eq. -1 ) then
           write (*,*) 'Failed to find histogram group!  status=',status
           goto 999
        endif

        !
        !  Read the histogram headers
        !
        do i=1,32  !  we dimensioned MUD_hist_hdr(32)

            status = fMUD_fseek( fileHandle, &
                          MUD_SEC_GEN_HIST_HDR_ID, i, &
                          0)
            !
            !  If no more histograms, then we are finished:
            !
            if (status .eq. -1 ) exit

            status = fMUD_read( fileHandle, MUD_hist_hdr(i) )

            !
            !  Access the histogram title
            !
            if (status.eq.1) then
               ! OK, get character string from string pointer, then display.
               call fMUD_ctofString( title, MUD_hist_hdr(i)%pcsTitle )
               write (*,*) 'histogram ',i,'  title = "',trim(title),'"'
            else
               write (*,*) 'Failed to read header for histogram ',i
            endif

        end do

 999    continue

        call fMUD_close( fileHandle )

        end program mud_test_fortran
{% endhighlight %}

#### Sample for VAX Fortran

{% highlight fortran %}
        program mud_test_fortran
        implicit none

        include 'mud.finc'

        integer*4 status
        integer*4 i
        character*32 filename
        integer*4 fileHandle
        character*20 title

        record /MUD_SEC_GEN_HIST_HDR/ MUD_hist_hdr(8)


        !
        !  Open an MUD format file
        !
        filename = '001234.msr'

        fileHandle = fMUD_openInput( filename )
        if (fileHandle .eq. 0) then
           write (*,*) 'Could not open file ',filename,
     +          '  (',fileHandle,')'
           stop
        endif
        write (*,*) 'Opened file ', filename

        !
        !  Position the file before the first histogram of the 
        !  TD histogram group
        !
        status = fMUD_fseek( fileHandle, 
     +                       MUD_SEC_GRP_ID, MUD_GRP_TRI_TD_HIST_ID,
     +                       0, 0 )
        if( status .eq. -1 ) then
           write (*,*) 'Failed to find histogram group!  status=',status
           goto 999
        endif
        !
        !  Read the histogram headers
        !

        do i=1,8  !  we dimensioned MUD_hist_hdr(8)

            status = fMUD_fseek( fileHandle, 
     +                     MUD_SEC_GEN_HIST_HDR_ID, i, 
     +                     0)
            !
            !  If no more histograms, then we are finished:
            !
            if (status .eq. -1 ) goto 999

            status = fMUD_read( fileHandle, MUD_hist_hdr(i) )

            !
            !  Access the histogram title
            !
            if (status.eq.1) then
               call fMUD_ctofString( title, MUD_hist_hdr(i).pcsTitle )
               write (*,*) 'histogram ',i,'  title = "',title,'"'
            else
               write (*,*) 'Failed to read header for histogram',i
            endif

        end do

 999    continue

        call fMUD_close( fileHandle )

        end ! program mud_test_fortran
{% endhighlight %}

Sample for old (but extended) Fortran77 (g77)

{% highlight fortran %}
        program mud_test_fortran

        include 'mud.f77'

        integer*4 status
        integer*4 i
        character*32 filename
        integer*4 fileHandle
        character*20 title

        integer*4 MUD_hist_hdr

*  Hist header structure, implemented as a common block.
*  All hist header elements are named hh_... The core elements
*  are named hh_c_...

            integer*4   hh_c_pNext              !* pointer to next section *
            integer*4   hh_c_size
            integer*4   hh_c_secID              !* Ident of section type *
            integer*4   hh_c_instanceID
            integer*4   hh_c_sizeof
            integer*4   hh_c_proc
!         
            integer*4   hh_histType
            integer*4   hh_nBytes
            integer*4   hh_nBins
            integer*4   hh_bytesPerBin
            integer*4   hh_fsPerBin
            integer*4   hh_t0_ps
            integer*4   hh_t0_bin
            integer*4   hh_goodBin1
            integer*4   hh_goodBin2
            integer*4   hh_bkgd1
            integer*4   hh_bkgd2
            integer*4   hh_nEvents
            integer*4   hh_pcsTitle


        common /cmn_hdr/ 
     +   hh_c_pNext, hh_c_size, hh_c_secID, hh_c_instanceID, 
     +   hh_c_sizeof, hh_c_proc,
     +   hh_histType, hh_nBytes, hh_nBins, hh_bytesPerBin, 
     +   hh_fsPerBin, hh_t0_ps, hh_t0_bin, hh_goodBin1, hh_goodBin2,
     +   hh_bkgd1, hh_bkgd2, hh_nEvents, hh_pcsTitle

        equivalence(hh_c_pNext,MUD_hist_hdr)

        !
        !  Open an MUD format file
        !
        filename = '001234.msr'

        fileHandle = fMUD_openInput( filename )
        if (fileHandle .eq. 0) then
           write (*,*) 'Could not open file ',filename,
     +          '  (',fileHandle,')'
           stop
        endif
        write (*,*) 'Opened file ', filename

        !
        !  Position the file before the first histogram of the 
        !  TD histogram group
        !
        status = fMUD_fseek( fileHandle, 
     +                       MUD_SEC_GRP_ID, MUD_GRP_TRI_TD_HIST_ID,
     +                       0 )
        if( status .eq. -1 ) then
           write (*,*) 'Failed to find histogram group!  status=',status
           goto 999
        endif
        !
        !  Read the histogram headers
        !
        do i=1,16

            status = fMUD_fseek( fileHandle, 
     +                     MUD_SEC_GEN_HIST_HDR_ID, i, 
     +                     0 )

            if (status .eq. -1 ) goto 999

            status = fMUD_read( fileHandle, MUD_hist_hdr )

            !
            !  Access the histogram title
            !
            if (status.eq.1) then
               call fMUD_ctofString( title, hh_pcsTitle )
               write (*,*) ' histogram title = <', title, '>'
            else
               write (*,*) ' Failed to read header for histogram',i
            endif

        end do

 999    continue
        call fMUD_close( fileHandle )
        stop
        end
{% endhighlight %}
