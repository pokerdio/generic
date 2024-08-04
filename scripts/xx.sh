#!/bin/bash

#echo $1 "-" $2

if [ "$1" = "bit" ]; then
    echo "disabling internets for 60 seconds"
    nmcli networking off
    sleep 60
    nmcli networking on
    echo "be good"
elif [ "$1" = "plz" ]; then
    echo "enabling the internets for 5 minutes! in 2 minutes"
    sleep 120
    nmcli networking on
    sleep 5
    echo "have fun"
    aplay /home/dio/scripts/chime.wav
    sleep 360
    nmcli networking off
elif [ "$1" = "on" ]; then
    echo "enabling the internets - wait 600 seconds!"
    sleep 600
    nmcli networking on
    echo "INTERNETS IS ON"
else
    echo "echo disabling the internets; use 'xx on' to restore "
    nmcli networking off
fi

