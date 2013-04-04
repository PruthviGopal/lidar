#!/usr/bin/python

import os.path
import sys
import liblas

f = liblas.file.File(sys.argv[1],mode='r')
#h = f.header

#print str(h.major)+"."+str(h.minor)
#print h.count
#print h.return_count
#print h.scale
#print h.min
#print h.max
#
#s = h.srs
#print s.wkt
#
for p in f:
    print p.x, p.y, p.z