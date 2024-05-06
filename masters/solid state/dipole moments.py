from matplotlib.pyplot import *
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_hermite
import math


def integrand(x, a, n, m):
    psi_prefactor = 1. / math.sqrt(2. ** n * math.factorial(n)) * (1 / np.pi) ** 0.25
    phi_prefactor = 1. / math.sqrt(2. ** m * math.factorial(m)) * (1 / np.pi) ** 0.25
    psi = psi_prefactor * np.exp(-(x + a / 2) ** 2 / 2) * eval_hermite(n, (x + a / 2))
    phi = phi_prefactor * np.exp(-(x - a / 2) ** 2 / 2) * eval_hermite(m, (x - a / 2))
    return psi * phi * x


for i in range(1, 10):
    for j in range(1, 10):
        dipole_moment = []
        a_array = np.linspace(0.05, 5, 100)
        for k in a_array:
            dipole_moment.append(quad(integrand, -np.inf, np.inf, args=(k, i, j))[0])
        print(dipole_moment)
        xlabel('a')
        ylabel('$\mu_{nm}$')
        plot(a_array, dipole_moment, label=f'$\mu{i}{j}$')
        legend()
