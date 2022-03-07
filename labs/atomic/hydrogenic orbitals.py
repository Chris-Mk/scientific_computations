import numpy as np
from sympy import *
import matplotlib.pyplot as plt

Z = 1
# r = np.linspace(0, 40, 1000)
# P1s = 2 * Z ** (3 / 2) * r * E ** (-Z * r)
# P2s = (1 / sqrt(2)) * Z ** (3 / 2) * r * E ** ((-Z * r) / 2) * (1 - 0.5 * Z * r)
# P2p = (1 / (2 * sqrt(6))) * Z ** (5 / 2) * r ** 2 * E ** ((-Z * r) / 2)
# P3s = (2 / (3 * sqrt(3))) * Z ** (3 / 2) * r * E ** ((-Z * r) / 3) * (1 - (2 / 3) * Z * r + (2 / 27) * (Z * r) ** 2)
# P3p = (8 / (27 * sqrt(6))) * Z ** (5 / 2) * r ** 2 * E ** ((-Z * r) / 3) * (1 - (1 / 6) * Z * r)
# P3d = (4 / (81 * sqrt(30))) * Z ** (7 / 2) * r ** 3 * E ** ((-Z * r) / 3)
#
plt.xlabel('r')
# plt.ylabel('P')
# plt.plot(r, P1s, label='$P_{1s}$')
# plt.plot(r, P2s, label='$P_{2s}$')
# plt.plot(r, P2p, label='$P_{2p}$')
# plt.plot(r, P3s, label='$P_{3s}$')
# plt.plot(r, P3p, label='$P_{3p}$')
# plt.plot(r, P3d, label='$P_{3d}$')

r = np.linspace(0, 8, 1000)
for i in range(1, 5):
    # p = 2 * i ** (3 / 2) * r * E ** (-i * r)
    p = (1 / sqrt(2)) * i ** (3 / 2) * r * E ** ((-i * r) / 2) * (1 - 0.5 * i * r)
    plt.plot(r, p, label=f'Z={i}')
    plt.ylabel('$P_{1s}$')
plt.grid()
plt.legend()
# plt.savefig("./graphs/P1s_orbitals.pdf")
