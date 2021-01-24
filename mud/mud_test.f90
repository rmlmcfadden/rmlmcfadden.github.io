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
