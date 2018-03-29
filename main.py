# main function to compute the AllenCahn model


import numpy as np
import matplotlib.pyplot as plt

Lx = 2
Ly = 0.4
# number of intervals
nx = 2
ny = 4
hx = Lx/nx
hy = Ly/ny
x = np.linspace(-Lx/2, Lx/2, nx+1)
y = np.linspace(-Ly/2, Ly/2, ny+1)
ind = np.arange(1, (nx + 1) * (ny + 1)+1)
ind = np.reshape(ind, (ny+1, nx+1))

plt.plot(x)
plt.show()
print(ind)