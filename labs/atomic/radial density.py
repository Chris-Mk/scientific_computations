import numpy as np
from sympy import *
import matplotlib.pyplot as plt

Z = 1
r = np.linspace(0, 30, 1000)
P3s = (2 / (3 * sqrt(3))) * Z ** (3 / 2) * r * E ** ((-Z * r) / 3) * (1 - (2 / 3) * Z * r + (2 / 27) * (Z * r) ** 2)
P3p = (8 / (27 * sqrt(6))) * Z ** (5 / 2) * r ** 2 * E ** ((-Z * r) / 3) * (1 - (1 / 6) * Z * r)
P3d = (4 / (81 * sqrt(30))) * Z ** (7 / 2) * r ** 3 * E ** ((-Z * r) / 3)

plt.grid()
plt.xlabel('r')
plt.ylabel('D(r)')
plt.plot(r, P3s ** 2, label='$|P_{3s}|^2$')
plt.plot(r, P3p ** 2, label='$|P_{3p}|^2$')
plt.plot(r, P3d ** 2, label='$|P_{3d}|^2$')
plt.legend()
# plt.savefig('./graphs/radial_density.pdf')
