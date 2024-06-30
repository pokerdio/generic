#!/bin/bash


echo -n "gif_list=[" > list.py

comma=""

for f in *.jpg; do
    if [ -s "$f" ] ; then
	echo "$comma" >> list.py
	echo -n "\"${f%.jpg}.gif\"" >> list.py
    
	echo "converting $f to ${f%.jpg}.gif"
	convert "$f" -resize 400x400\> "${f%.jpg}.gif"
	comma=","
    fi
done

echo "]" >> list.py

rm list_order.py
