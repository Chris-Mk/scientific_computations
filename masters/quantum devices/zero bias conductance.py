from matplotlib.pyplot import *
from numpy import *
from scipy.constants import *
from scipy.integrate import *

temp, alpha, Vg, Vg0 = 50e-3, 0.03, 5.9, 6.78  # K, -, V, V
gamma_L, gamma_R, epsilon = 6e-6, 55e-6, -alpha * (Vg - Vg0)  # eV, eV, -
kT = Boltzmann * temp


def f_prime(E):
    return exp(E / (Boltzmann * temp)) / ((Boltzmann * temp) * (1 + exp(E / (Boltzmann * temp))) ** 2)


def T(E):
    return (gamma_L * gamma_R) / (E ** 2 - 2 * epsilon * E + epsilon ** 2 + ((gamma_L + gamma_R) / 2) ** 2)


G = quad(lambda E: f_prime(E) * T(E), -1, 1)
E_array = linspace(-10 * kT, 10 * kT, 1000)

plot(E_array, f_prime(E_array))
show(block=True)
