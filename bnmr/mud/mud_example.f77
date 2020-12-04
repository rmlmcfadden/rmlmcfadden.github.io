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
