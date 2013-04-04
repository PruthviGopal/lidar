#!/usr/bin/python

import os.path
import sys
import liblas
import gdal
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import Rbf  

class LidarGrid (object) :

    def __init__ (self, f) :
        
        self.h = f.header
        self.minx = self.h.min[0]
        self.maxx = self.h.max[0]
        self.xscale = self.h.scale[0]
        self.miny = self.h.min[1]
        self.maxy = self.h.max[1]
        self.yscale = self.h.scale[1]
        self.minz = self.h.min[2]
        self.maxz = self.h.max[2]
        self.zscale = self.h.scale[2]
        
        self.xsize = int((self.maxx-self.minx)*1)+1
        self.ysize = int((self.maxy-self.miny)*1)+1
        
        print "minx: "+str(self.minx)
        print "maxx: "+str(self.maxx)
        print "miny: "+str(self.miny)
        print "maxy: "+str(self.maxy)
        
        print "Creating "+str(self.xsize)+" x "+str(self.ysize)+" grid."
        self.grid = np.zeros ((self.xsize, self.ysize))
        print "Grid created."

    def add (self, x, y, z) :
        self.grid[int(x-self.minx)][int(y-self.miny)] = z

    def get (self, x, y):
        return self.grid[x][y]

if __name__ == '__main__' :

    f = liblas.file.File(sys.argv[1],mode='r')

    lgrid = LidarGrid (f)

    print lgrid.minz
    print lgrid.maxz
    
    print "Adding data to grid"
    for p in f:
        if p.return_number == 1:
            lgrid.add (p.x, p.y, p.z)
    #   print "Add: "+str(p.x)+", "+str(p.y)+", "+str(p.z)

    print "Data added to grid."

    

    plt.subplot(111)
    n = plt.normalize(75, 155)
#img = plt.imshow(lgrid.grid, extent=(0, lgrid.xsize, lgrid.ysize, 0), cmap=plt.cm.Greys_r)
    img = plt.imshow(lgrid.grid, norm=n, interpolation='nearest', cmap=plt.cm.jet)
#    img.set_clim(lgrid.minz, 120)
    plt.colorbar()
    plt.show()

    print "Done."

#for x in range (0, lidar_grid.xsize):
#   for y in range (0, lidar_grid.ysize):
#       print "Get: "+str(lidar_grid.get (x, y))