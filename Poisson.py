# Solve Poisson equation
# alpha u - beta Lap u = f
# a dn u + b u = g
import numpy as np
import scipy as sp
from poissonmat_FD import *


def poisson(u, ind, nx, ny, hx, hy, alpha, beta, a, b, f, g):
    n = (nx+1)*(ny+1)
    u = np.zeros(n, n)
    mat = poissonmat_FD(ind, nx, ny, alpha, beta, a, b)
    [L, U] = sp.linalg.lu(mat, True)
    print (L)
    print (U)
    return u


