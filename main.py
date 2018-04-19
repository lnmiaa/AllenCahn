# main function to compute the AllenCahn model


import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from initialization import *

Lx = 2
Ly = 4
# number of intervals
nx = 20
ny = 40
hx = Lx/nx
hy = Ly/ny
x = np.linspace(-Lx/2, Lx/2, nx+1)
y = np.linspace(-Ly/2, Ly/2, ny+1)
ind = np.arange(1, (nx+1)*(ny+1)+1)
ind = np.reshape(ind, (ny+1, nx+1))
xx, yy = np.meshgrid(x, y)

exu, f, g = initu(xx, yy)
#
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, exu, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()
