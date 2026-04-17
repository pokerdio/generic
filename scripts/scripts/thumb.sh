#!/bin/bash
#makez thumbnails

for i in *.jpg; do
    echo $i
done;

#find . -type f -exec convert {} -resize 200x200 -background "rgb(25,50,50)" -gravity center -extent 200x200  "{}thumb.jpg" \;
