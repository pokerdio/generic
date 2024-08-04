#!/usr/bin/python
import sys
import re
import commands


episode = ["[sS]...?[eE]%02d" % int(sys.argv[1]),
           "[sS]eries.%02d" % int(sys.argv[1])]

o, f = commands.getstatusoutput('ls *.mp4 *.avi *.mpg *.mkv')

for s in f.splitlines():
    for e in episode:
        if re.search(e, s):
            cmd = 'vlc --start-time=0 "%s"' % s
            print "executing " + cmd
            o, f = commands.getstatusoutput(cmd)
            if o != 0:
                print("failure %d - %s" % (o, f))

            sys.exit(0)


print "couldn't find episode " + sys.argv[1]
