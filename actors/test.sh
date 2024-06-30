#!/bin/bash

#foo=$(grep -o -m 1 "src=\"//[^\"]*" a.htm | cut -c 8-)
#echo "foo is $foo"


#####

# echo "ifs = '$IFS'"


# IFS=\| read a b <<< "the_beatles|is the best in the world"

# echo "a = '$a'"
# echo "b = '$b'"

# if [ ! -z "$b" ] ; then
#     echo "doing it $a.gif.txt"
#     echo "$b" > "$a.gif.txt"
# fi


# echo "ifs = '$IFS'"


#b=$'Spencer_Tracy|bad day at black rock\nguess who\'s coming to dinner'
#b='Jeff_Daniels|the martian suit\\nlooper gangster'
b="zzz|a\nb"

echo ${#b}
echo "$b"
echo -e "$b"


IFS=\| read -r foo txt <<< "$b"


echo "$foo"
echo "$txt"

