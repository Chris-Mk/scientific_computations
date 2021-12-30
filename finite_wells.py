import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# define parameters
L = 7.3 * 10 ** (-9)  # width in meters
e = 1.6 * 10 ** (-19)  # electron charge
# c = 299792458  # speed of light
c = 300000000  # speed of light
V0 = 0.22 * e  # potential well height, in Joule
Esteps = 1000  # number of steps in energy vector
E = np.linspace(0, V0, Esteps)  # energy vector
m0 = 9.1 * 10 ** (-31)  # free electron mass
me = 0.067 * m0  # effective electron mass
mh = 0.48 * m0  # effective hole mass
hbar = 1.05 * 10 ** (-34)  # plancks constant
E_GaAs = 1.52
E_photon = hbar * 2 * np.pi * c
np.seterr(divide='ignore')

# Define left and right hand side of (**)
RHS = np.sqrt((V0 - E) / E)  # right hand side
LHSe = np.tan(L / 2 * np.sqrt(2 * me / hbar ** 2 * E))
LHSh = np.tan(L / 2 * np.sqrt(2 * mh / hbar ** 2 * E))


# plot functions, x-axis in electron volts
# plt.grid()
# plt.plot(E / e, RHS)
# plt.plot(E / e, LHSe)
# plt.plot(E / e, LHSh)
# plt.ylim([0, 2])  # set y-axis range
# plt.xlim([0, 0.22])  # set x-axis range
# plt.xlabel('E (Ev)')
# plt.ylabel('Left and right hand side functions')
# plt.show()


# solving the equations
def energy_electron(x):
    return np.sqrt((V0 - x) / x) - np.tan(L / 2 * np.sqrt(2 * me / hbar ** 2 * x))


def energy_hole(x):
    return np.sqrt((V0 - x) / x) - np.tan(L / 2 * np.sqrt(2 * mh / hbar ** 2 * x))


Ee = fsolve(energy_electron, 0.05 * e)
Eh = fsolve(energy_hole, 0.05 * e)

rhs = (Ee[0] + Eh[0]) / e
energy = E_photon / 743e-9
if rhs > energy / e - E_GaAs:
    print("Too high!")
elif rhs < energy / e - E_GaAs:
    print("Too low!")

print("Lambda = 660nm, L = 0.877nm")
print("Lambda = 690nm, L = 1.59nm")
print("Lambda = 723nm, L = 2.63nm")
print("Lambda = 744nm, L = 7.379638nm")
