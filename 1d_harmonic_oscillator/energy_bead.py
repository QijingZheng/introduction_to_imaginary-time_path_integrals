#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

theta = 5
erros = []
for r in np.arange(0.5, 10, 0.1):
    P = 2 * r * theta
    E = 1 - np.tanh(theta) * np.sum(
            theta / (
                theta**2 + P**2 * np.sin(np.arange(P)*np.pi/P)**2
                )
            )
    erros += [(P/2/theta, E * 100)]
erros = np.array(erros)

with open("Error.csv", 'w+') as out:
    out.write(' x, y\n')
    np.savetxt(out, erros, fmt='%8.4f, %8.4f')

figure = plt.figure()
ax = plt.subplot()

ax.plot(erros[:,0] / (2*theta), erros[:, 1])

# ax.set_xlabel('X-label', labelpad=5)
# ax.set_ylabel('Y-label', labelpad=5)
plt.show()
