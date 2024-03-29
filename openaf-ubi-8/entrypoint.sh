#!/bin/sh

# Ensure that the user exists in /etc/passwd
if ! whoami >/dev/null 2>&1; then
   if [ -w /etc/passwd ]; then
      echo "$(id -u):x:$(id -u):0:$(id -u) user:${HOME}:/sbin/nologin" >> /etc/passwd
   fi
fi

# This script is used to run OpenAF as a container
PATH=$PATH:/openaf
export PATH

JAVA_ARGS=""
if [ ! -z "$JVM_MEMMXPERC" ]; then
   JAVA_ARGS="$JAVA_ARGS -XX:MinRAMPercentage=$JVM_MEMMXPERC -XX:MaxRAMPercentage=$JVM_MEMMXPERC"
fi

if [ ! -z "$JVM_MEMMSPERC" ]; then
   JAVA_ARGS="$JAVA_ARGS -XX:InitialRAMPercentage=$JVM_MEMMSPERC"
fi
export JAVA_ARGS

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
