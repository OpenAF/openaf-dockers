#!/bin/sh

PATH=$PATH:/openaf
export PATH

if [ -z "$OPENAF_MINRAMPERC" ]; then
   OPENAF_MINRAMPERC=50.0
   export OPENAF_MINRAMPERC
fi

if [ -z "$OPENAF_MAXRAMPERC" ]; then
   OPENAF_MAXRAMPERC=25.0
   export OPENAF_MAXRAMPERC
fi

if [ ! -f /openaf/.installed ]; then
   if [ ! -z "$OPACKS" ] || [ ! -z "$OPACKS_DIR" ]; then
      /openaf/openaf -f /openaf/.docker/installOPacks.js
      echo "1" > /openaf/.installed
   fi
fi

if [ ! -z "$OPENAF" ]; then
   /openaf/openaf -f "$OPENAF" -e "$@"
fi

if [ ! -z "$OJOB" ]; then
   /openaf/ojob "$OJOB" "$@"
fi 

if [ ! -z "$OPACK_EXEC" ]; then
   /openaf/opack exec "$OPACK_EXEC" "$@"
fi

if [ -z "$OPENAF" ] && [ -z "$OJOB" ]; then
   if [ -z $1 ] && [ -z "$OPACK_EXEC" ]; then
      /bin/bash
   else
      /openaf/openaf "$@"
   fi
fi
