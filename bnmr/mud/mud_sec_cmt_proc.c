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
