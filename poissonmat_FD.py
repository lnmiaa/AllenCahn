# Solve Poisson equation
# alpha u - beta Lap u = f
# a dn u + b u = g
# This is the subroutine to generate the matrix for LHS using
# uniform mesh finite difference method.
import numpy as np


def poissonmat_FD(ind, nx, ny, hx, hy, alpha, beta, a, b):
    n = (nx+1)*(ny+1)
    mat = np.zeros((n, n))
    # inner grid
    for i in range(1, nx+1):
        for j in range(1, ny):
            mat[ind[j, i], ind[j, i]] = beta*2*(1/hx**2+1/hy**2)+alpha
            if i == nx:
                mat[ind[j, i], ind[j, 2]] = -beta/hx**2
            else:
                mat[ind[j, i], ind[j, i+1]] = -beta/hx**2
            mat[ind[j, i], ind[j, i-1]] = -beta/hx**2
            mat[ind[j, i], ind[j+1, i]] = -beta/hy**2
            mat[ind[j, i], ind[j-1, i]] = -beta/hy**2

    # Boundary condition, bottom: -a uy + b u =*, top: a u_y + b u
    for i in range(1, nx+1):
        # bottom
        mat[ind[0, i], ind[0, i]] = a*3/2/hy+b
        mat[ind[0, i], ind[1, i]] = -2*a/hy
        mat[ind[0, i], ind[2, i]] = a/2/hy
        # top
        mat[ind[ny, i], ind[ny, i]] = a*3/2/hy+b
        mat[ind[ny, i], ind[ny-1, i]] = -2*a/hy
        mat[ind[ny, i], ind[ny-2, i]] = a/2/hy

    # Set periodic condition, first column x=0
    for j in range(0, ny+1):
        mat[ind[j, 0], ind[j, 0]] = 1
        mat[ind[j, 0], ind[j, nx]] = -1

    return mat
