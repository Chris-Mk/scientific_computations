# import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import *
# import scipy.integrate as integrate

L = 500E-12  # H
C = 500E-15  # F
C_c = 5E-15  # F
G = 1E-6  # S
Z_0 = 50  # Ohm

omega_resonance = 1 / np.sqrt(L * (C + C_c))  # s^-1
kappa_c = (Z_0 * omega_resonance ** 2 * C_c ** 2) / C
kappa_QD = G / (C + C_c)
kappa_QD_CB = G / (C + C_c) * 0.05
delomega_QD = omega_resonance * 1E-3
R_i = 1 / G  # Ohm
kappa_i = 1 / R_i
kappa_tot = kappa_c + kappa_QD + kappa_i


def Reflectance(omega, k_QD):
    R = (1 - ((k_QD + kappa_i) * kappa_c) / ((kappa_tot / 2) ** 2 + (omega - omega_resonance - delomega_QD) ** 2))
    return R


x_omega = np.linspace(.995 * omega_resonance, 1.005 * omega_resonance, 500)

# fig, ax = plt.subplots()
# ax.plot(x_omega, Reflectance(x_omega, kappa_QD))
# ax.plot(x_omega, Reflectance(x_omega, kappa_QD_CB))
# ax.set_title('Reflectance')

plot(x_omega, Reflectance(x_omega, kappa_QD))
plot(x_omega, Reflectance(x_omega, kappa_QD_CB))
