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
