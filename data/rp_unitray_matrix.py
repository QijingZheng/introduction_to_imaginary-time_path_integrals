#!/usr/bin/env python

import numpy as np

N = 10
xx = np.diag(np.ones(N) * 2) - np.diag(np.ones(N-1), k=1) - np.diag(np.ones(N-1, dtype=np.float128), k=-1)
U = np.zeros((N, N))
fac = 1 / np.sqrt(N)

for ii in range(N):
    for jj in range(N):
        if jj == 0:
            U[ii, jj] = fac
        if jj == N/2:
            U[ii, jj] = fac * (-1)**ii
        if 1 <= jj <= N/2 -1:
            U[ii, jj] = np.sqrt(2) * fac * np.cos(2*np.pi * ii * jj / N)
        if N/2+1 <= jj <= N - 1:
            U[ii, jj] = np.sqrt(2) * fac * np.sin(2*np.pi * ii * jj / N)

# print U
print "\n".join([
        ' '.join(["%8.4f" % x for x in row])
        for row in U
        ])
print 
print "\n".join([
        ' '.join(["%8.4f" % x for x in row])
        for row in np.dot(U.T, U)
        ])
print 
print "\n".join([
        ' '.join(["%8.4f" % x for x in row])
        for row in np.dot(U, U.T)
        ])
