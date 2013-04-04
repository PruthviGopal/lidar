#!/usr/bin/python

import sys
from math import pow
from math import sqrt
import numpy as np
import scipy.spatial as sp
import liblas
import matplotlib.pyplot as plt

def pointValueInvDist(x,y,power,smoothing,xv,yv,values):
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


f = liblas.file.File(sys.argv[1],mode='r')
h = f.header

minx = h.min[0]
maxx = h.max[0]
xscale = 1 # h.scale[0]
miny = h.min[1]
maxy = h.max[1]
yscale = 1 # h.scale[1]
minz = h.min[2]
maxz = h.max[2]
zscale = 1 # h.scale[2]
xsize = int(maxx-minx)
ysize = int(maxy-miny)
power = 1
smoothing = 20

#print "Initializing array."

xv=np.zeros(h.count)
yv=np.zeros(h.count)
zv=np.zeros(h.count)

#print "Array initialized."

#print "Populating array."

i=0
for p in f:
    xv[i] = p.x
    yv[i] = p.y
    zv[i] = p.z
    i+=1

#print "Arrays populated."

xyz = zip(xv.ravel(), yv.ravel(), zv.ravel())

#print pointValueNN(xyz, ([minx, maxy, minz]), 3)

print "Creating grid."
valuesGrid = np.zeros((xsize,ysize))

print "Grid created."

print "Finding grid point values."
for x in range(0, int(maxx-minx)):
    for y in range(0, int(maxy-miny)):
        valuesGrid[x][y] = pointValueNN(xyz, ([minx+x, miny+y, 0]), 3)
#        print int(minx+x), int(miny+y), valuesGrid[x][y]

print "Grid values found."

#plt.subplot(111)
#n = plt.normalize(407, 435)
#img = plt.imshow(valuesGrid, norm=n, interpolation='nearest', cmap=plt.cm.jet)
#plt.colorbar()
#plt.show()

print "Done."

