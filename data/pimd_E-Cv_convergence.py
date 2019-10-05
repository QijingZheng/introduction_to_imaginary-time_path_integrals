#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

theta = 5
E_errs = []
C_errs = []
for r in np.arange(0.5, 10, 0.1):
    P = 2 * r * theta
    E = 1 - np.tanh(theta) * np.sum(
            theta / (
                theta**2 + P**2 * np.sin(np.arange(P)*np.pi/P)**2
                )
            )
    C = 1 + np.sinh(theta)**2 * np.sum(
            1.0 / (
                theta**2 + P**2 * np.sin(np.arange(P)*np.pi/P)**2
                )
            -
            2*theta**2 / (
                (theta**2 + P**2 * np.sin(np.arange(P)*np.pi/P)**2)**2
                )
            )

    E_errs += [(P/2/theta, E * 100)]
    C_errs += [(P/2/theta, C * 100)]

E_errs = np.array(E_errs)
C_errs = np.array(C_errs)

with open("E_error.csv", 'w+') as out:
    # out.write(' x, y\n')
    # np.savetxt(out, E_errs, fmt='%8.4f, %8.4f')
    np.savetxt(out, E_errs, fmt='%8.4f')
with open("C_error.csv", 'w+') as out:
    np.savetxt(out, C_errs, fmt='%8.4f')

figure = plt.figure()
ax = plt.subplot()

# ax.plot(E_errs[:,0], E_errs[:, 1])
ax.plot(C_errs[:,0], C_errs[:, 1])

# ax.set_xlabel('X-label', labelpad=5)
# ax.set_ylabel('Y-label', labelpad=5)
plt.show()
