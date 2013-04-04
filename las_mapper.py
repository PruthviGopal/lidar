#!/usr/bin/python

import sys
from math import pow
from math import sqrt
import numpy as np
import scipy as sp
import liblas

def pointValue(x,y,power,smoothing,xv,yv,values):
    nominator=0
    denominator=0
    for i in range(0,len(values)):
        dist = sqrt((x-xv[i])*(x-xv[i])+(y-yv[i])*(y-yv[i])+smoothing*smoothing);
        #If the point is really close to one of the data points, return the data point value to avoid singularities
        if(dist<0.0000000001):
            return values[i]
        nominator=nominator+(values[i]/pow(dist,power))
        denominator=denominator+(1/pow(dist,power))
    #Return NODATA if the denominator is zero
    if denominator > 0:
        value = nominator/denominator
    else:
        value = -9999
    return value


f = liblas.file.File(sys.argv[1],mode='r')
h = f.header

minx = h.min[0]
maxx = h.max[0]
xscale = h.scale[0]
miny = h.min[1]
maxy = h.max[1]
yscale = h.scale[1]
minz = h.min[2]
maxz = h.max[2]
zscale = h.scale[2]
power = 1
smoothing = 20
print "Initializing array."

xv=[]
yv=[]
zv=[]

print "Array initialized."

print "Populating array."

for p in f:
    xv.append(p.x)
    yv.append(p.y)
    zv.append(p.z)

xyz = [xv, yv, zv]

print str(xyz[0][0][0])

#print "Finding grid point values."
#for x in range(int(minx/xscale),int(maxx/xscale)):
#    for y in range(int(miny/yscale),int(maxy/yscale)):
#        print x*xscale, y*yscale, pointValue(x,y,power,smoothing,xv,yv,zv)

exit()