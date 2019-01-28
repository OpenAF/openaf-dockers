#!/bin/sh

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

if [ -z "$OPENAF" ] && [ -z "$OJOB" ]; then
   if [ -z $1 ]; then
      /bin/sh
   else
      /openaf/openaf "$@"
   fi
fi
