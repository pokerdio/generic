#!/bin/bash

if [ "$1" = "!" ]; then
    if [ -z "$2" ]; then
        echo "moving..."
        a=`ls -ct ~/Downloads/* | head -1` 
    else
        a=`ls -ct ~/Downloads/* | head -$2 | tail -1`
    fi
    mv "$a" .
elif [ "$1" = "c" ]; then
    if [ -z "$2" ]; then
        cp `ls -ct ~/Downloads/* | head -1` .
    else
        cp `ls -ct ~/Downloads/* | head -$2 | tail -1` .
    fi
elif [ "$1" = "-h" ]; then
    echo "usage: d ! to move last downloaded file, d c to copy it"
    echo "d ! 2 to move second to last downloaded file"
    echo "d ! 3 to copy third to last downloaded file"
    echo "d by itself displays the last 5 files..." 
else
    if [ -z "$1" ]; then
        ls -ct ~/Downloads/* | head -5
    else
        ls -ct ~/Downloads/* | head -$1
    fi
fi 

