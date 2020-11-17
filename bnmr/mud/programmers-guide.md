---
layout: default
title: Programmer's Guide
description: MUD Programmer's Guide.
parent: MUD
grand_parent: β-NMR
---

# Programmer's Guide
{: .no_toc }

<i>
This page is a reproduction of the content found at
[http://cmms.triumf.ca/mud/mud_friendly.html](http://cmms.triumf.ca/mud/mud_friendly.html "MUD Programmer's Guide").
Though this is mainly to test the formatting of the markdown to html convension,
I have made minor changes thoughout the text to improve readability.
</i>

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Introduction

Routines begin with `MUD_` for applications written in C and
`fMUD_` for applications written in Fortran.
This document refers to all routines as `MUD_*`,
but all descriptions apply equally (unless stated otherwise)
to the Fortran equivalents, `fMUD_*`.
The MUD file's data structures can be accessed directly
using routines in both C and Fortran,
but this document is concerned with the higher level "friendly" interface.

Routines come generally under two categories:
those to read a file (`MUD_*Read`, `MUD_get*`, see Reading a data file)
and those to write a file (`MUD_*Write`, `MUD_set*`, see Writing a data file).
Each routine for performing some aspect of reading the file
has an equivalent for writing.
There is a seperate routine for each item to be read/written.
A file may be opened for reading, writing, or both (modification).
If you are programming in C,
you may also need to use the routine `MUD_pack` (see Miscellaneous routines).

### Prototyle delcarations

The prototype declarations listed in this file are
intended to give guidance to programming applications.
The prototypes are declared in the include files:
`mud.h` (C), `mud.finc` (Vax Fortran),
`mud.f90` (Fortran 90+), `mud.f77` (Fortran 77).

For C, the type `UINT32` is also defined in `mud.h`.
It is used to ensure a 32-bit (4-byte) unsigned integer across architectures.
The type `REAL64` declares 64-bit (8-byte) floating-point.
(Other data types will undoubtedly be used
in the future as new MUD sections are added.)
Strings for the C routines are zero-terminated.

In the Fortran prototypes displayed below,
the parameters are named according to their type:

{% highlight fortran %}
i_  =  integer*4
c_  =  character*n
d_  =  double precision (real*8)
{% endhighlight %}

Parameters of type `?` indicate an array that may be of several different types.
Parameters ending in `(?)` indicate an array of unknown size.
It is left to the programmer to ensure that the type
and size of the arrays passed to these routines is sensible.
Fortran character strings are returned padded with spaces.

### Common parameters

All routines except `MUD_open*` and `MUD_pack` return a boolean status value
(`0` for failure, `1` for success).
The `MUD_open*` routines return a file handle, or `-1` for failure.
`MUD_pack` returns the number of bytes in the resultant array.

The file handle, `fh`, is a small integer returned by `MUD_open*`,
and must be passed to other routines.

The `MUD_get-string` functions (for C) take an integer parameter (`strdim`)
specifying the maximum acceptable string length.
The returned string will have no more than `strdim - 1` significant characters
(plus the null terminator).
The Fortran routines have no need for an explicit length parameter
(the dimensioned length is passed implicitly).

Many routines take an integer parameter (`num`)
indicating which of many instances is to be dealt with.
For example, which histogram.

### A note on time

All measures of time (single values or arrays) are stored in 32 bit integers
as the number of seconds since 00:00:00 GMT, January 1, 1970.
This is, or was, the same as used by the standard C library function time
and stored in the C type definition `time_t`,
but on newer systems `time_t` is 64-bit.
Programmers should beware that MUD files continue to use 32-bit time values
regardless of the local system's `time_t` type.
MUD's time will run out in the year 2038.

### Platforms supported

The MUD library of routines has been written so that
data files may be used on all supported platforms.
All non-portable issues (byte ordering, floating-point representation)
are handled by the library.
The library has been built on the following platforms:

- Linux (32 and 64 bit)
- Windows XP and later
- DOS (Borland C++ 3.1 - 16 bit) (no Fortran routines)
- VAX/VMS
- Alpha/VMS
- SGI
- Sun Solaris
- Mac OSX (Darwin) (no Fortran routines)

and should build easily on many others.

## Reading a data file

### Opening and closing a data file for reading

Opening the file is the first thing that must be done when reading a file,
and closing is the last.
The open routine returns a small integer identifier
("file handle") or `-1` for failure.
The file handle needs to be passed to all of the other routines
(parameter `fh`) to specify the file and data to be acted on.
The file type is passed back in `pType`.
Valid file types include (defined in the include file):

{% highlight c %}
MUD_FMT_GEN_ID,
MUD_FMT_TRI_TD_ID /* TD-MuSR */
MUD_FMT_TRI_TI_ID /* I-MuSR */
{% endhighlight %}

The close routine returns a boolean status.

Note that, in the present implementation,
the entire file is read into memory by the
`MUD_openRead` (or `MUD_openReadWrite`) operation.
Any subsequent "get" operation is a simple look-up in the MUD structure.
The file handle is therefore an index selecting among loaded MUD structures.
The `MUD_closeRead` operation closes the file and
releases the memory used to hold the MUD structure.

#### C routines

{% highlight c %}
int MUD_openRead( char* filename, UINT32* pType );
int MUD_closeRead( int fh );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_openRead( c_filename, i_Type )
integer*4 fMUD_closeRead( i_fh )
{% endhighlight %}

See below for a description of `MUD_openReadWrite`,
which is almost identical to `MUD_openRead`.

### Reading the Run Description

The routine `MUD_getRunDesc` returns the run description type in `pType`.
Valid types are (defined in `mud.h`):

{% highlight c %}
MUD_SEC_GEN_RUN_DESC_ID    /* TD-MuSR */
MUD_SEC_TRI_TI_RUN_DESC_ID /* TI-MuSR */
{% endhighlight %}

#### C routines

{% highlight c %}
int MUD_getRunDesc( int fh, UINT32* pType );
int MUD_getExptNumber( int fh, UINT32* pExptNumber );
int MUD_getRunNumber( int fh, UINT32* pRunNumber );
int MUD_getElapsedSec( int fh, UINT32* pElapsedSec );
int MUD_getTimeBegin( int fh, UINT32* TimeBegin );
int MUD_getTimeEnd( int fh, UINT32* TimeEnd );
int MUD_getTitle( int fh, char* title, int strdim );
int MUD_getLab( int fh, char* lab, int strdim );
int MUD_getArea( int fh, char* area, int strdim );
int MUD_getMethod( int fh, char* method, int strdim );
int MUD_getApparatus( int fh, char* apparatus, int strdim );
int MUD_getInsert( int fh, char* insert, int strdim );
int MUD_getSample( int fh, char* sample, int strdim );
int MUD_getOrient( int fh, char* orient, int strdim );
int MUD_getDas( int fh, char* das, int strdim );
int MUD_getExperimenter( int fh, char* experimenter, int strdim );
{% endhighlight %}

Not in I-MuSR:

{% highlight c %}
int MUD_getTemperature( int fh, char* temperature, int strdim );
int MUD_getField( int fh, char* field, int strdim );
{% endhighlight %}

I-MuSR only:

{% highlight c %}
int MUD_getSubtitle( int fh, char* subtitle, int strdim );
int MUD_getComment1( int fh, char* comment1, int strdim );
int MUD_getComment2( int fh, char* comment2, int strdim );
int MUD_getComment3( int fh, char* comment3, int strdim );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_getRunDesc( i_fh, i_Type )
integer*4 fMUD_getExptNumber( i_fh, i_ExptNumber )
integer*4 fMUD_getRunNumber( i_fh, i_RunNumber )
integer*4 fMUD_getElapsedSec( i_fh, i_ElapsedSec )
integer*4 fMUD_getTimeBegin( i_fh, i_TimeBegin )
integer*4 fMUD_getTimeEnd( i_fh, i_TimeEnd )
integer*4 fMUD_getTitle( i_fh, c_title )
integer*4 fMUD_getLab( i_fh, c_lab )
integer*4 fMUD_getArea( i_fh, c_area )
integer*4 fMUD_getMethod( i_fh, c_method )
integer*4 fMUD_getApparatus( i_fh, c_apparatus )
integer*4 fMUD_getInsert( i_fh, c_insert )
integer*4 fMUD_getSample( i_fh, c_sample )
integer*4 fMUD_getOrient( i_fh, c_orient )
integer*4 fMUD_getDas( i_fh, c_das )
integer*4 fMUD_getExperimenter( i_fh, c_experimenter )
{% endhighlight %}

Not in I-MuSR:

{% highlight fortran %}
integer*4 fMUD_getTemperature( i_fh, c_temperature )
integer*4 fMUD_getField( i_fh, c_field )
{% endhighlight %}

I-MuSR only:

{% highlight fortran %}
integer*4 fMUD_getSubtitle( i_fh, c_subtitle )
integer*4 fMUD_getComment1( i_fh, c_comment1 )
integer*4 fMUD_getComment2( i_fh, c_comment2 )
integer*4 fMUD_getComment3( i_fh, c_comment3 )
{% endhighlight %}

### Reading the Comments

MUD data files contain a section for comments,
but to date the feature has been underutilized.
The routine `MUD_getComments` returns the type of the comment group in `pType`
and the number of comments in `pNum`.
The only valid type currently defined in `mud.h` is `MUD_GRP_CMT_ID`,
in which comments are plain text.
Should comments start being used,
an enhanced type could be defined to support various text encoding,
mark-up style (such as html), and (graphical) attachments.

#### C routines

{% highlight c %}
int MUD_getComments( int fh, UINT32* pType, UINT32* pNum );
int MUD_getCommentPrev( int fh, int num, UINT32* pPrev );
int MUD_getCommentNext( int fh, int num, UINT32* pNext );
int MUD_getCommentTime( int fh, int num, UINT32* pTime );
int MUD_getCommentAuthor( int fh, int num, char* author, int strdim );
int MUD_getCommentTitle( int fh, int num, char* title, int strdim );
int MUD_getCommentBody( int fh, int num, char* body, int strdim );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_getComments( i_fh, i_Type, i_Num )
integer*4 fMUD_getCommentPrev( i_fh, i_num, i_Prev )
integer*4 fMUD_getCommentNext( i_fh, i_num, i_Next )
integer*4 fMUD_getCommentTime( i_fh, i_num, i_Time )
integer*4 fMUD_getCommentAuthor( i_fh, i_num, c_author )
integer*4 fMUD_getCommentTitle( i_fh, i_num, c_title )
integer*4 fMUD_getCommentBody( i_fh, i_num, c_body )
{% endhighlight %}

### Reading the Histograms

The routine `MUD_getHists` returns the type of the histogram group in `pType`
and the number of histograms in `pNumHists`;
it does not get the histograms themselves.
Valid types are (defined in the include file `mud.h`):

{% highlight c %}
MUD_GRP_GEN_HIST_ID,
MUD_GRP_TRI_TD_HIST_ID /* TD-MuSR */
MUD_GRP_TRI_TI_HIST_ID /* TI-MuSR */
{% endhighlight %}

The routine `MUD_getHistType` tells the type of a particular histogram,
typically `MUD_SEC_TRI_TD_HIST_ID` or `MUD_SEC_TRI_TI_HIST_ID`
which equal the corresponding `MUD_GRP_...` codes.

The routine `MUD_getHistSecondsPerBin` stands out because
it does not retrieve a separate item of data,
but duplicates the function of `MUD_getHistFsPerBin`.
Cases have arisen where the histogram bin size was
not exactly represented as an integer number of femtoseconds,
so scaled or coded values were saved.
`MUD_getHistSecondsPerBin` is intended to always return
the correct time per bin (in seconds).

Note that the routine `MUD_getHistData` returns
the entire (unpacked) array in `pData`.
For C usage, it is possible to access the
original packed data array using `MUD_getHistpData`,
which returns a pointer to the data which
can be unpacked later - see Packing Histograms below.
Note that a value of `0` (zero) in `pBytesPerBin` indicates a packed array.
Arrays that are returned already unpacked by `MUD_getHistData`
always have `4` bytes per bin.
Make sure that your array `pData` is large enough. 

#### C routines

{% highlight c %}
int MUD_getHists( int fh, UINT32* pType, UINT32* pNumHists );
int MUD_getHistType( int fh, int Histnum, UINT32* pType );
int MUD_getHistNumBytes( int fh, int Histnum, UINT32* pNumBytes );
int MUD_getHistNumBins( int fh, int Histnum, UINT32* pNumBins );
int MUD_getHistBytesPerBin( int fh, int Histnum, UINT32* pBytesPerBin );
int MUD_getHistFsPerBin( int fh, int Histnum, UINT32* pFsPerBin );
int MUD_getHistT0_Ps( int fh, int Histnum, UINT32* pT0_ps );
int MUD_getHistT0_Bin( int fh, int Histnum, UINT32* pT0_bin );
int MUD_getHistGoodBin1( int fh, int Histnum, UINT32* pGoodBin1 );
int MUD_getHistGoodBin2( int fh, int Histnum, UINT32* pGoodBin2 );
int MUD_getHistBkgd1( int fh, int Histnum, UINT32* pBkgd1 );
int MUD_getHistBkgd2( int fh, int Histnum, UINT32* pBkgd2 );
int MUD_getHistNumEvents( int fh, int Histnum, UINT32* pNumEvents );
int MUD_getHistTitle( int fh, int Histnum, char* title, int strdim );
int MUD_getHistSecondsPerBin( int fh, int Histnum, REAL64* pSecondsPerBin );
int MUD_getHistData( int fh, int Histnum, void* pData );
int MUD_getHistpData( int fh, int Histnum, void** ppData );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_getHists( i_fh, i_Type, i_NumHists )
integer*4 fMUD_getHistType( i_fh, i_num, i_Type )
integer*4 fMUD_getHistNumBytes( i_fh, i_num, i_NumBytes )
integer*4 fMUD_getHistNumBins( i_fh, i_num, i_NumBins )
integer*4 fMUD_getHistBytesPerBin( i_fh, i_num, i_BytesPerBin )
integer*4 fMUD_getHistFsPerBin( i_fh, i_num, i_FsPerBin )
integer*4 fMUD_getHistT0_Ps( i_fh, i_num, i_T0_ps )
integer*4 fMUD_getHistT0_Bin( i_fh, i_num, i_T0_bin )
integer*4 fMUD_getHistGoodBin1( i_fh, i_num, i_GoodBin1 )
integer*4 fMUD_getHistGoodBin2( i_fh, i_num, i_GoodBin2 )
integer*4 fMUD_getHistBkgd1( i_fh, i_num, i_Bkgd1 )
integer*4 fMUD_getHistBkgd2( i_fh, i_num, i_Bkgd2 )
integer*4 fMUD_getHistNumEvents( i_fh, i_num, i_NumEvents )
integer*4 fMUD_getHistTitle( i_fh, i_num, c_title )
integer*4 fMUD_getHistSecondsPerBin( i_fh, i_num, d_SecondsPerBin )
integer*4 fMUD_getHistData( i_fh, i_num, ?_pData(?) )
{% endhighlight %}

### Reading the Scalers

The routine `MUD_getScalers` returns the type of the scaler group in `pType`
and the number of scalers in `pNumScal`.
Valid types are (defined in the include file):

{% highlight c %}
MUD_GRP_GEN_SCALER_ID
MUD_GRP_TRI_TD_SCALER_ID /* TD-MuSR */
{% endhighlight %}

The function `MUD_getScalerLabel` gives the scaler
label for a particular numbered scaler,
and `MUD_getScalerCounts` gives an array of two 4-byte integers:
the scaler total, and the most recent rate.

#### C routines

{% highlight c %}
int MUD_getScalers( int fh, UINT32* pType, UINT32* pNumScal );
int MUD_getScalerLabel( int fh, int Scalnum, char* label, int strdim );
int MUD_getScalerCounts( int fh, int Scalnum, UINT32* pCounts );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_getScalers( i_fh, i_Type, i_NumScal )
integer*4 fMUD_getScalerLabel( i_fh, i_num, c_label )
integer*4 fMUD_getScalerCounts( i_fh, i_num, i_Counts(2) )
{% endhighlight %}

### Reading the Independent Variables

The routine `MUD_getIndVars` returns the
type of the independent variable group in `pType` and
the number of independent variables in `pNumIV`.
Valid types are (defined in `mud.h`):

{% highlight c %}
MUD_GRP_GEN_IND_VAR_ID     /* TD-MuSR */
MUD_GRP_GEN_IND_VAR_ARR_ID /* TI-MuSR */
{% endhighlight %}

The type `MUD_GRP_GEN_IND_VAR_ID` has statistics data only.
The type `MUD_GRP_GEN_IND_VAR_ARR_ID` has statistics data,
history data and possibly time data
(time that the data point was taken, in seconds since 00:00 Jan. 1, 1970).

For history data, the data type is returned in `pDataType`,
with values of `1` for integer, `2` for real and `3` for string.
The number of history data points is returned in `pNumData`.
The element size `pElemSize` is in bytes per element.
The boolean value `pHasTime` indicates whether or not there is time data.
It might be desireable to receive a pointer to the array data,
using `MUD_getIndVarpData` and `MUD_getIndVarpTimeData`.
In this case, it is up to the programmer to unpack the data (if necessary).
Note that time data is never packed.

#### C routines

{% highlight c %}
int MUD_getIndVars( int fh, UINT32* pType, UINT32* pNumIV );
int MUD_getIndVarLow( int fh, int num, double* pLow );
int MUD_getIndVarHigh( int fh, int num, double* pHigh );
int MUD_getIndVarMean( int fh, int num, double* pMean );
int MUD_getIndVarStddev( int fh, int num, double* pStddev );
int MUD_getIndVarSkewness( int fh, int num, double* pSkewness );
int MUD_getIndVarName( int fh, int num, char* name, int strdim );
int MUD_getIndVarDescription( int fh, int num, char* description, int strdim );
int MUD_getIndVarUnits( int fh, int num, char* units, int strdim );
{% endhighlight %}

For array data in `MUD_GRP_GEN_IND_VAR_ARR_ID` groups:

{% highlight c %}
int MUD_getIndVarNumData( int fh, int num, UINT32* pNumData );
int MUD_getIndVarElemSize( int fh, int num, UINT32* pElemSize );
int MUD_getIndVarDataType( int fh, int num, UINT32* pDataType );
int MUD_getIndVarHasTime( int fh, int num, UINT32* pHasTime );
int MUD_getIndVarData( int fh, int num, void* pData );
int MUD_getIndVarpData( int fh, int num, void** ppData );
int MUD_getIndVarTimeData( int fh, int num, UINT32* pTimeData );
int MUD_getIndVarpTimeData( int fh, int num, UINT32** ppTimeData );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_getIndVars( i_fh, i_Type, i_NumIV )
integer*4 fMUD_getIndVarLow( i_fh, i_num, real*8 pLow )
integer*4 fMUD_getIndVarHigh( i_fh, i_num, real*8 pHigh )
integer*4 fMUD_getIndVarMean( i_fh, i_num, real*8 pMean )
integer*4 fMUD_getIndVarStddev( i_fh, i_num, real*8 pStddev )
integer*4 fMUD_getIndVarSkewness( i_fh, i_num, real*8 pSkewness )
integer*4 fMUD_getIndVarName( i_fh, i_num, c_name )
integer*4 fMUD_getIndVarDescription( i_fh, i_num, c_description )
integer*4 fMUD_getIndVarUnits( i_fh, i_num, c_units )
{% endhighlight %}

For array data in `MUD_GRP_GEN_IND_VAR_ARR_ID` groups:

{% highlight fortran %}
integer*4 fMUD_getIndVarNumData( i_fh, i_num, i_NumData )
integer*4 fMUD_getIndVarElemSize( i_fh, i_num, i_ElemSize )
integer*4 fMUD_getIndVarDataType( i_fh, i_num, i_DataType )
integer*4 fMUD_getIndVarHasTime( i_fh, i_num, i_HasTime )
integer*4 fMUD_getIndVarData( i_fh, i_num, ?_pData(?) )
integer*4 fMUD_getIndVarTimeData( i_fh, i_num, i_TimeData(?) )
{% endhighlight %}

## Writing a data file

### Opening and closing a file for writing

Writing a data file can be handled in three different ways,
where the best choice depends on the origin of the data.

If the data does not come from a MUD file, but will be written to one,
then the destination file should first be opened with `MUD_openWrite`,
all the data should be inserted using the `MUD_set...` functions,
and then the file should be closed by `MUD_closeWrite`.
The open routine returns an integer file handle (or `-1` for failure)
which is passed to all of the other routines (parameter `fh`)
to specify the file for writing.
The file type is defined by type.
Valid file types include (defined in the include file):

{% highlight c %}
MUD_FMT_GEN_ID ,
MUD_FMT_TRI_TD_ID /* TD-MuSR */
MUD_FMT_TRI_TI_ID /* TI-MuSR */
{% endhighlight %}

The close routine returns a boolean status.
Note that, in the present implementation,
the file on disk is indeed opened by `MUD_openWrite`,
but nothing is written to it until `MUD_closeWrite`
writes out the entire MUD structure.

To modify an existing MUD file, it should be opened with `MUD_openReadWrite`,
which is the same as `MUD_openRead` except for the file-access mode.
There is no corresponding `MUD_closeReadWrite` function!
Use `MUD_closeWrite` to re-write the MUD file,
or MUD_closeRead to close the file,
abandoning any changes that were made.

To write modifications of an existing MUD file to a different file,
access the original data beginning with `MUD_openRead`,
modify the data (`MUD_set...`),
then write the altered data using `MUD_closeWriteFile`
specifying the new file name to write.

#### C routines

{% highlight c %}
int MUD_openWrite( char* filename, UINT32 type );
int MUD_openReadWrite( char* filename, UINT32* pType );
int MUD_closeWrite( int fh );
int MUD_closeWriteFile( int fh, char* filename );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_openWrite( c_filename, i_type )
integer*4 fMUD_openReadWrite( c_filename, i_Type )
integer*4 fMUD_closeWrite( i_fh )
integer*4 fMUD_closeWriteFile( i_fh, c_filename )
{% endhighlight %}

### Writing the Run Description

The routine `MUD_setRunDesc` initializes a
run description section of type `type`.
This must be done before specifying any of the
other parts of the run description.
Valid types are:

{% highlight c %}
MUD_SEC_GEN_RUN_DESC_ID    /* TD-MuSR */
MUD_SEC_TRI_TI_RUN_DESC_ID /* TI-MuSR */
{% endhighlight %}

#### C routines

{% highlight c %}
int MUD_setRunDesc( int fh, UINT32 type );
int MUD_setExptNumber( int fh, UINT32 exptNumber );
int MUD_setRunNumber( int fh, UINT32 runNumber );
int MUD_setElapsedSec( int fh, UINT32 elapsedSec );
int MUD_setTimeBegin( int fh, UINT32 timeBegin );
int MUD_setTimeEnd( int fh, UINT32 timeEnd );
int MUD_setTitle( int fh, char* title );
int MUD_setLab( int fh, char* lab );
int MUD_setArea( int fh, char* area );
int MUD_setMethod( int fh, char* method );
int MUD_setApparatus( int fh, char* apparatus );
int MUD_setInsert( int fh, char* insert );
int MUD_setSample( int fh, char* sample );
int MUD_setOrient( int fh, char* orient );
int MUD_setDas( int fh, char* das );
int MUD_setExperimenter( int fh, char* experimenter );
{% endhighlight %}

Not in I-MuSR:

{% highlight c %}
int MUD_setTemperature( int fh, char* temperature );
int MUD_setField( int fh, char* field );
{% endhighlight %}

I-MuSR only:

{% highlight c %}
int MUD_setSubtitle( int fh, char* subtitle );
int MUD_setComment1( int fh, char* comment1 );
int MUD_setComment2( int fh, char* comment2 );
int MUD_setComment3( int fh, char* comment3 );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_setRunDesc( i_fh, i_type )
integer*4 fMUD_setExptNumber( i_fh, i_exptNumber )
integer*4 fMUD_setRunNumber( i_fh, i_runNumber )
integer*4 fMUD_setElapsedSec( i_fh, i_elapsedSec )
integer*4 fMUD_setTimeBegin( i_fh, i_timeBegin )
integer*4 fMUD_setTimeEnd( i_fh, i_timeEnd )
integer*4 fMUD_setTitle( i_fh, c_title )
integer*4 fMUD_setLab( i_fh, c_lab )
integer*4 fMUD_setArea( i_fh, c_area )
integer*4 fMUD_setMethod( i_fh, c_method )
integer*4 fMUD_setApparatus( i_fh, c_apparatus )
integer*4 fMUD_setInsert( i_fh, c_insert )
integer*4 fMUD_setSample( i_fh, c_sample )
integer*4 fMUD_setOrient( i_fh, c_orient )
integer*4 fMUD_setDas( i_fh, c_das )
integer*4 fMUD_setExperimenter( i_fh, c_experimenter )
{% endhighlight %}

Not in I-MuSR:

{% highlight fortran %}
integer*4 fMUD_setTemperature( i_fh, c_temperature )
integer*4 fMUD_setField( i_fh, c_field )
{% endhighlight %}

I-MuSR only:

{% highlight fortran %}
integer*4 fMUD_setSubtitle( i_fh, c_subtitle )
integer*4 fMUD_setComment1( i_fh, c_comment1 )
integer*4 fMUD_setComment2( i_fh, c_comment2 )
integer*4 fMUD_setComment3( i_fh, c_comment3 )
{% endhighlight %}

### Writing the Comments

The routine `MUD_setComments` initializes a
comment group of type `type` with `numCom` comments.
This must be done before defining the comments.
The only valid type is (defined in the include file): `MUD_GRP_CMT_ID`.

#### C routines

{% highlight c %}
int MUD_setComments( int fh, UINT32 type, UINT32 numCom );
int MUD_setCommentPrev( int fh, int num, UINT32 prev );
int MUD_setCommentNext( int fh, int num, UINT32 next );
int MUD_setCommentTime( int fh, int num, UINT32 time );
int MUD_setCommentAuthor( int fh, int num, char* author );
int MUD_setCommentTitle( int fh, int num, char* title );
int MUD_setCommentBody( int fh, int num, char* body );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_setComments( i_fh, i_type, i_num )
integer*4 fMUD_setCommentPrev( i_fh, i_num, i_rev )
integer*4 fMUD_setCommentNext( i_fh, i_num, i_next )
integer*4 fMUD_setCommentTime( i_fh, i_num, i_time )
integer*4 fMUD_setCommentAuthor( i_fh, i_num, c_author )
integer*4 fMUD_setCommentTitle( i_fh, i_num, c_title )
integer*4 fMUD_setCommentBody( i_fh, i_num, c_body )
{% endhighlight %}

### Writing the Histograms

The routine `MUD_setHists` initializes a
histogram group of type `type` with `numHists` histograms.
This must be done before defining the individual histograms.
Valid types are (defined in `mud.h`):

{% highlight c %}
MUD_GRP_GEN_HIST_ID ,
MUD_GRP_TRI_TD_HIST_ID /* TD-MuSR */
MUD_GRP_TRI_TI_HIST_ID /* TI-MuSR */
{% endhighlight %}

Note that you pass an array of 32 bit integers to the routine `MUD_setHistData`.
This routine will pack the array, if necessary,
depending on the previous definition of `bytesPerBin`.
Note that a value of `0` (zero) in `bytesPerBin` indicates a packed array.

For C usage, it might be desireable to pass a
pointer to the array using `MUD_setHistpData`.
In this case, it is left to the programmer to pack the array (if necessary).

#### C routines

{% highlight c %}
int MUD_setHists( int fh, UINT32 type, UINT32 numHists );
int MUD_setHistType( int fh, int Histnum, UINT32 type );
int MUD_setHistNumBytes( int fh, int Histnum, UINT32 numBytes );
int MUD_setHistNumBins( int fh, int Histnum, UINT32 numBins );
int MUD_setHistBytesPerBin( int fh, int Histnum, UINT32 bytesPerBin );
int MUD_setHistFsPerBin( int fh, int Histnum, UINT32 fsPerBin );
int MUD_setHistT0_Ps( int fh, int Histnum, UINT32 t0_ps );
int MUD_setHistT0_Bin( int fh, int Histnum, UINT32 t0_bin );
int MUD_setHistGoodBin1( int fh, int Histnum, UINT32 goodBin1 );
int MUD_setHistGoodBin2( int fh, int Histnum, UINT32 goodBin2 );
int MUD_setHistBkgd1( int fh, int Histnum, UINT32 bkgd1 );
int MUD_setHistBkgd2( int fh, int Histnum, UINT32 bkgd2 );
int MUD_setHistNumEvents( int fh, int Histnum, UINT32 numEvents );
int MUD_setHistTitle( int fh, int Histnum, char* title );
int MUD_setHistSecondsPerBin( int fh, int Histnum, REAL64 secondsPerBin );
int MUD_setHistData( int fh, int Histnum, void* pData );
int MUD_setHistpData( int fh, int Histnum, void* pData );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_setHists( i_fh, i_type, i_numHists )
integer*4 fMUD_setHistType( i_fh, i_num, i_type )
integer*4 fMUD_setHistNumBytes( i_fh, i_num, i_numBytes )
integer*4 fMUD_setHistNumBins( i_fh, i_num, i_numBins )
integer*4 fMUD_setHistBytesPerBin( i_fh, i_num, i_bytesPerBin )
integer*4 fMUD_setHistFsPerBin( i_fh, i_num, i_fsPerBin )
integer*4 fMUD_setHistT0_Ps( i_fh, i_num, i_t0_ps )
integer*4 fMUD_setHistT0_Bin( i_fh, i_num, i_t0_bin )
integer*4 fMUD_setHistGoodBin1( i_fh, i_num, i_goodBin1 )
integer*4 fMUD_setHistGoodBin2( i_fh, i_num, i_goodBin2 )
integer*4 fMUD_setHistBkgd1( i_fh, i_num, i_bkgd1 )
integer*4 fMUD_setHistBkgd2( i_fh, i_num, i_bkgd2 )
integer*4 fMUD_setHistNumEvents( i_fh, i_num, i_numEvents )
integer*4 fMUD_setHistTitle( i_fh, i_num, c_title )
integer*4 fMUD_setHistSecondsPerBin( i_fh, i_num, d_secondsPerBin )
integer*4 fMUD_setHistData( i_fh, i_num, ?_Data(?) )
{% endhighlight %}

### Writing the Scalers

The routine `MUD_setScalers` intializes a
scaler group of type `type` with `numScal` scalers.
Valid types are (defined in the include file):

{% highlight c %}
MUD_GRP_GEN_SCALER_ID
MUD_GRP_TRI_TD_SCALER_ID /* TD-MuSR */
{% endhighlight %}

Note that scaler counts are passed in
an array of two four-byte unsigned integers.
The first element is the scaler total, and the second is the most recent rate.

#### C routines

{% highlight c %}
int MUD_setScalers( int fh, UINT32 type, UINT32 numScal );
int MUD_setScalerLabel( int fh, int num, char* label );
int MUD_setScalerCounts( int fh, int num, UINT32* pCounts );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_setScalers( i_fh, i_type, i_num )
integer*4 fMUD_setScalerLabel( i_fh, i_num, c_label )
integer*4 fMUD_setScalerCounts( i_fh, i_num, i_Counts(2) )
{% endhighlight %}

### Writing the Independent Variables

The routine `MUD_setIndVars` initializes a
independent variable group of type `type` with `numIV` independent variables.
Valid types are (defined in the include file):

{% highlight c %}
MUD_GRP_GEN_IND_VAR_ID     /* TD-MuSR */
MUD_GRP_GEN_IND_VAR_ARR_ID /* TI-MuSR */
{% endhighlight %}

The type `MUD_GRP_GEN_IND_VAR_ID` has statistics data only.
The type `MUD_GRP_GEN_IND_VAR_ARR_ID` has statistics data,
history data and possibly time data
(time that the data point was taken, in seconds since 00:00 Jan. 1, 1970).

For history data, the data type is specified in `dataType`,
with values of `1` for integer, `2` for real and `3` for string.
The number of history data points is set in `numData`.
The element size `elemSize` is in bytes per element.
It might be desireable to pass a pointer to the array data,
using `MUD_setIndVarpData` and `MUD_setIndVarpTimeData`.
In this case, it is up to the programmer to pack the data (if necessary).
Note that time data is never packed.

#### C routines

{% highlight c %}
int MUD_setIndVars( int fh, UINT32 type, UINT32 numIV );
int MUD_setIndVarLow( int fh, int num, double low );
int MUD_setIndVarHigh( int fh, int num, double high );
int MUD_setIndVarMean( int fh, int num, double mean );
int MUD_setIndVarStddev( int fh, int num, double stddev );
int MUD_setIndVarSkewness( int fh, int num, double skewness );
int MUD_setIndVarName( int fh, int num, char* name );
int MUD_setIndVarDescription( int fh, int num, char* description );
int MUD_setIndVarUnits( int fh, int num, char* units );
{% endhighlight %}

for `MUD_GRP_GEN_IND_VAR_ARR_ID` groups:

{% highlight c %}
int MUD_setIndVarNumData( int fh, int num, UINT32 numData );
int MUD_setIndVarElemSize( int fh, int num, UINT32 elemSize );
int MUD_setIndVarDataType( int fh, int num, UINT32 dataType );
int MUD_setIndVarHasTime( int fh, int num, UINT32 hasTime );
int MUD_setIndVarData( int fh, int num, void* pData );
int MUD_setIndVarTimeData( int fh, int num, UINT32* pTimeData );
int MUD_setIndVarpData( int fh, int num, void* pData );
int MUD_setIndVarpTimeData( int fh, int num, UINT32* pTimeData );
{% endhighlight %}

#### Fortran routines

{% highlight fortran %}
integer*4 fMUD_setIndVars( i_fh, i_type, i_numIV )
integer*4 fMUD_setIndVarLow( i_fh, i_num, real*8 low )
integer*4 fMUD_setIndVarHigh( i_fh, i_num, real*8 high )
integer*4 fMUD_setIndVarMean( i_fh, i_num, real*8 mean )
integer*4 fMUD_setIndVarStddev( i_fh, i_num, real*8 stddev )
integer*4 fMUD_setIndVarSkewness( i_fh, i_num, real*8 skewness )
integer*4 fMUD_setIndVarName( i_fh, i_num, c_name )
integer*4 fMUD_setIndVarDescription( i_fh, i_num, c_description )
integer*4 fMUD_setIndVarUnits( i_fh, i_num, c_units )
{% endhighlight %}

for `MUD_GRP_GEN_IND_VAR_ARR_ID` groups:

{% highlight fortran %}
integer*4 fMUD_setIndVarNumData( i_fh, i_num, i_numData )
integer*4 fMUD_setIndVarElemSize( i_fh, i_num, i_elemSize )
integer*4 fMUD_setIndVarDataType( i_fh, i_num, i_dataType )
integer*4 fMUD_setIndVarHasTime( i_fh, i_num, i_hasTime )
integer*4 fMUD_setIndVarData( i_fh, i_num, ?_pData(?) )
integer*4 fMUD_setIndVarTimeData( i_fh, i_num, i_TimeData(?) )
{% endhighlight %}

## Miscellaneous routines

### Packing/unpacking Integer Histograms

`MUD_pack` is used to pack or unpack integer histogram data.
This routine is not necessary in typical use involving the routines
`MUD_getData`, `MUD_getIndVarData`, or their `MUD_set` companions,
which do the packing/unpacking internally if necessary.
This is always the case for Fortran access.
`MUD_pack` may be necessary when using the routines
`MUD_getpData`, `MUD_getIndVarpData`, or their set equivalents.
Valid bin sizes are: `0`, `1`, `2`, `4` (bytes per bin),
where a packed array is indicated by a bin size of `0` (zero),
and `numBins` is the number of bins.
You must make sure that `outArray` has enough space for the resultant array.

#### C routine

{% highlight c %}
int MUD_pack( int num, int inBinSize, void* inArray, int outBinSize, void* outArray );
{% endhighlight %}

#### Fortran routine

{% highlight fortran %}
integer*4 fMUD_pack( i_num, i_inBinSize, ?_inArray(?), i_outBinSize, ?_outArray(?) )
{% endhighlight %}

## Examples

### Fortran test

(works with `g77`):

{% highlight fortran %}
      implicit none
      include 'mud.f77'

      integer*4 idat(102400)

      character*64 fname
      integer*4 stat, fmtid
      integer*4 fh, pType
      integer*4 RunNumber 
      character*80 RunTitle
      integer*4 htype,hnum,nh
      integer*4 nbins,nt1
      integer*4 i,is,type,num
      real*8 seconds
      character*10 scl,hnam(16)
      integer*4 sclval(2)

      write(*,100) 
 100  format( ' Enter mud file name: ',$ )
      read(*,200,end=999) fname
 200  format(a)

      fmtid=1234
      fh = fMUD_openRead( fname, fmtid )
      write (*,*) 'After open, fh = ',fh
      write (*,*) 'format id =', fmtid,'; TRI_TD = ',MUD_FMT_TRI_TD_ID

      if (fMUD_getRunDesc(fh,pType) .eq. 0) goto 666

      if (fMUD_getRunNumber(fh,RunNumber) .eq. 0) goto 666
      if (fMUD_getTitle(fh,RunTitle) .eq. 0) goto 666

      write(*,300) RunNumber,RunTitle(:66)
 300  format(' Run',I6,1x,A)

      if (fMUD_gethists(fh,htype,nh) .eq. 0) goto 666
      do 333 i=1,nh
	 if (fMUD_gethisttitle(fh,i,hnam(i)) .eq. 0) goto 666
 333  continue
      write(*,*) 'There are ',nh,' histograms:'
      write(*,*) (hnam(i),i=1,nh)

      hnum = 1
      if (fMUD_gethistnumbins(fh,hnum,nbins) .eq. 0) goto 666
      write(*,*) 'Histogram ',hnum,' has ',nbins,' bins'
      if (fMUD_getHistGoodBin1( fh,hnum,nt1 ) .eq. 0) goto 666
      if (nbins>102400) then
         write(*,*) 'That''s too many bins'
      else
         if (fMUD_getHistSecondsPerBin(fh,hnum,seconds) .eq. 0) goto 666
	 write(*,*) seconds*1.0d9,' ns per bin'
         if (fMUD_getHistData(fh,hnum,idat) .eq. 0) goto 666
         write(*,500) nt1,(idat(i),i=nt1,nt1+39)
 500     format(' Data starting from bin',I5,':',4(/10I7))
      endif

      if (fMUD_getScalers( fh, Type, Num ) .gt. 0 .and. 
     >    Type .eq. MUD_GRP_TRI_TD_SCALER_ID) then

	 write(*,*) 'There are ',Num,' scalers.'
         do i = 1, Num
            is = fMUD_getScalerLabel( fh, i, scl )
            is = fMUD_getScalerCounts( fh, i, sclval )
	    write (*,*) i,'  ',scl,': ',sclval(1)
	 enddo
      endif

 666  continue
      stat = fMUD_closeRead( fh )
*      write (*,*) 'After close, stat = ',stat

 999  continue

      end
{% endhighlight %}
