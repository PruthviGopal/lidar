#!/usr/bin/python

import os.path
import sys
import liblas
import gdal
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = liblas.file.File(sys.argv[1],mode='r')
h = f.header
z = []

for p in f:
    z.append(p.z)

plt.subplot(111)
plt.hist(z, bins=255)
plt.show()
print "Done."