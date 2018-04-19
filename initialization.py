# Initialization for AllenCahn

import numpy as np


def initpara():
    global alpha, beta, a, b
    alpha = 4
    beta = 3
    a = 1
    b = 3


def initu(xx, yy):
    # type: (xx, yy) -> exu
    # to test Poisson,
    # alpha u - beta Lap u = f
    # a dn u + b u = g
    initpara()
    pi = np.pi
    tmp1 = np.sin(xx*pi)
    tmp2 = np.cos(pi*yy)
    exu = np.multiply(tmp1, tmp2)
    f = alpha*exu-beta*(-2*exu*pi**2)
    g = np.zeros([2, xx.shape[1]])
    g[0, :] = -pi*np.cos(pi*xx[0, :])*tmp2([0, 0])
    g[1, :] = pi*np.cos(pi*xx[0, :])*tmp2([yy.shape[0]-1, 0])
    return exu, f, g


