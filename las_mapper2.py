#!/usr/bin/python

import sys
from math import pow
from math import sqrt
import numpy as np
import scipy as sp
import liblas

def pointValueNN(xyz, point, num_neighbors):
    points = sp.cKDTree(xyz)
    
    num_neighbors = 3
    
    nnq = points.query(point, num_neighbors)
    
    z=np.zeros(num_neighbors)
    
    j=0
    for n in nnq[1] :
        z[j] = xyz[n][2]
        j+=1
    
    neighbor_mean = np.mean(z)
    return neighbor_mean


#minx = h.min[0]
#maxx = h.max[0]
#xscale = 1 # h.scale[0]
#miny = h.min[1]
#maxy = h.max[1]
#yscale = 1 # h.scale[1]
#minz = h.min[2]
#maxz = h.max[2]
#zscale = 1 # h.scale[2]
#xsize = int(maxx-minx)
#ysize = int(maxy-miny)
power = 1
smoothing = 20

print "Initializing array."

xv=np.zeros(h.count)
yv=np.zeros(h.count)
zv=np.zeros(h.count)

for line in sys.stdin :
    x, y, z = line.split()
    xv.append(x)
    yv.append(y)
    zv.append(z)

xyz = zip(xv.ravel(), yv.ravel(), zv.ravel())

print "Creating grid."
valuesGrid = np.zeros((xv.size,yv.size))

print "Grid created."

print "Finding grid point values."
for x in range(0, xv.size):
    for y in range(0, yv.size):
        valuesGrid[x][y] = pointValueNN(xyz, ([minx+x, miny+y, 0]), 3)
#        print int(minx+x), int(miny+y), valuesGrid[x][y]

print "Grid values found."

#for i in range(0, len(xv)) :
#    print "%s\t%s\t%s" % (xv[i], yv[i], zv[i])

#print "Finding grid point values."
#for x in range(int(minx/xscale),int(maxx/xscale)):
#    for y in range(int(miny/yscale),int(maxy/yscale)):
#        print x*xscale, y*yscale, pointValue(x,y,power,smoothing,xv,yv,zv)

exit()