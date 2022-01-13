from matplotlib.pyplot import *
from numpy import *


# epsilon = -3.999018587
# n = 1

def get_phi(energy, s):
    q = sqrt(-energy)
    phi = [1, exp(q * h)]
    nodes = 0

    # def f(x):
    #     return -nu0 * cosh(x) ** (-2) - energy

    def f(x):
        nu_left = -nu0 * cosh(x + s) ** (-2)
        nu_right = -nu0 * cosh(x - s) ** (-2)
        return nu_left + nu_right - energy

    for i in range(len(xi) - 2):
        phi.append((2 + (h ** 2) * f(xi[i + 1])) * phi[i + 1] - phi[i])
        if phi[-2] * phi[-1] < 0:
            nodes += 1

    return nodes, phi


def bisection(nodes, s):
    e_min, e_max = -2 * nu0, -0.1
    energy = 0

    while abs((e_min - e_max) / (e_min + e_max)) > 1e-12:
        mid_energy = (e_max + e_min) / 2
        curr_nodes, phi = get_phi(mid_energy, s)
        energy = mid_energy

        if curr_nodes < nodes:
            e_min = mid_energy
        elif curr_nodes > nodes:
            e_max = mid_energy
        elif curr_nodes == nodes:
            q = sqrt(-mid_energy)
            phi_test = phi[-2] * phi[-1] - exp(q * h) * phi[-1] ** 2
            if phi_test < 0:
                e_min = mid_energy
            elif phi_test > 0:
                e_max = mid_energy
    return energy


# xi_max = int(8 + 4)
# xi_min = -xi_max
# steps = 100 * 2 * xi_max
# nu0 = 6
# xi = linspace(xi_min, xi_max, steps)
# h = (xi_max - xi_min) / steps
# energy = (bisection(1, 4))
# p = get_phi(energy, 4)[1]
# print(energy)
# plot(xi, p)

S = linspace(0, 4, 100)
for n in range(4):
    energies = zeros(len(S))

    for j in range(len(S)):
        xi_max = int(8 + S[j])
        xi_min = -xi_max
        steps = 100 * 2 * xi_max
        nu0 = 6

        xi = linspace(xi_min, xi_max, steps)
        h = (xi_max - xi_min) / steps

        print("s = ", S[j])
        energies[j] = bisection(n, S[j])
    plot(S, energies)
