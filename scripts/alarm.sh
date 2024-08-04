#!/bin/bash

ret="$1" 

if [ ! $1 ]; then
    echo "default time: 60 seconds"
    ret="60"
fi
echo "sleep $ret"
sleep "$ret"
aplay /home/dio/scripts/chime.wav

if [ -n "$2" ]; then
    for i in {1..100}
    do
        sleep 10
        aplay /home/dio/scripts/chime.wav
    done
fi 
