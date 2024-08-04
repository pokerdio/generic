#!/bin/bash

echo "bash ver ${BASH_VERSION}..."

for i in $(ls *.sh)
do
    echo "welcome $i times"
done
