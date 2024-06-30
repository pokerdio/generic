#!/bin/bash


# webp to jpg
for f in *.webp; do
    echo "testing $f"
    if [ -s "${f%.webp}.jpg" ] ; then
        echo "${f%.webp}.jpg already here"
        continue
    fi
    echo "convertint $f to ${f%.webp}.png"
    dwebp "$f" -o "${f%.webp}.png"

    if [ -s "${f%.webp}.png" ] ; then
        echo "success - now converting png to jpg"
    else
        echo "fail - abandon file"
        continue
    fi
    convert "${f%.webp}.png" "${f%.webp}.jpg"

    if [ -s "${f%.webp}.png" ] ; then
        echo "op success - now deleting png intermediary"
    fi
    rm "${f%.webp}.png"
done



#jpg to gif
for f in *.jpg; do
    if [ -s "${f%.jpg}.gif" ] ; then
       continue
    fi
    if [ -s "$f" ] ; then
	echo "converting $f to ${f%.jpg}.gif"
	convert "$f" -resize 400x400\> "${f%.jpg}.gif"

        if [ -s "${f%.jpg}.gif" ] ; then
            echo "success - adding new entry to list.py"
	    echo -en "\ngif_list.append (\"${f%.jpg}.gif\")" >> list.py
        fi

    fi
done

