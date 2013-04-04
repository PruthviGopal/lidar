#!/usr/bin/python

import sys
import numpy as np
import scipy as sp
from scipy.interpolate import Rbf
from scipy import sparse
import liblas
import matplotlib.pyplot as plt


f = liblas.file.File(sys.argv[1],mode='r')
h = f.header

print "Initializing array."

#x = np.zeros(h.count)
#y = np.zeros(h.count)
#z = np.zeros(h.count)

x=[]
y=[]
z=[]

print "Array initialized."

print "Populating array."

for p in f:
    x.append(p.x)
    y.append(p.y)
    z.append(p.z)

print "Array populated."

#Creating the output grid (100x100, in the example)

print "Creating output grid."
ti = np.linspace(h.max[0]-h.min[0], h.max[1]-h.min[1])
XI, YI = sp.sparse.lil_matrix(x, y)
print "Output grid created"


#Creating the interpolation function and populating the output matrix value

print "Running RBF."
rbf = Rbf(x, y, z, function='inverse')
ZI = rbf(XI, YI)
print "RBF complete"

print "Plotting output."
# Plotting the result
n = plt.normalize(h.min[2], h.max[2])
plt.subplot(1, 1, 1)
plt.pcolor(XI, YI, ZI)
plt.scatter(x, y, z)
plt.title('RBF interpolation')
plt.xlim(h.min[0], h.max[0])
plt.ylim(h.min[1], h.max[1])
#plt.colorbar()
plt.show()

print "Done."