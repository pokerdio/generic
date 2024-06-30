#!/usr/bin/python3

import sys, os, re, random

exec (open("./list.py").read ())

list_order = []

def print_name (x):
    s = gif_list[list_order[x]]
    s = re.sub (r"\.gif", "", s)
    s = re.sub ("[_]+", " ", s)
    print ("%5d  -    %s" % (x, s))
    

if os.path.isfile ("list_order.py"):
    exec (open ("list_order.py"). read ())

    olen = len (list_order)

    n = olen
    if len (sys.argv) > 1:
        n = int(sys.argv[1])
        
    if n > olen:
        n = olen

    if n < -olen:
        n = -olen
            
    if n == 0:
        n = 1

    if n < 0:
        for i in range (-n):
            print_name (len (list_order) - i - 1)
    else:
        for i in range (n):
            print_name (i)

