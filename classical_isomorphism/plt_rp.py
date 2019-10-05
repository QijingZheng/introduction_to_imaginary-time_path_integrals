#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt

N = 6
sigma = 0.1

xx = np.exp(1j * np.pi * 2 * np.arange(N+1) / float(N))
xx[1:N] *= (sigma * np.random.randn(N-1) + 1.0)

np.savetxt('rp.dat', np.c_[xx.real, xx.imag], fmt='(%8.4f, %8.4f)', newline=',\n')

figure = plt.figure()
ax = plt.subplot()

ax.plot(xx.real, xx.imag)

ax.set_xlabel('X-label', labelpad=5)
ax.set_ylabel('Y-label', labelpad=5)
plt.show()
