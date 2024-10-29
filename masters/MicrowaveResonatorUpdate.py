# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:00:58 2023

@author: [Your Name Here]
"""

import numpy as np

import matplotlib.pyplot as plt

import scipy.integrate as integrate
# from scipy import inf
import scipy.special as special

L = 500E-12  # H
C = 500E-15  # F
C_c = 5E-15  # F
G = 1E-6  # S
Z_0 = 50  # Ohm

omega_res = 1 / np.sqrt(L * (C + C_c))  # s^-1

kappa_c = (Z_0 * omega_res ** 2 * C_c ** 2) / C
kappa_QD = G / (C + C_c)
delomega_QD = omega_res * 1E-3
R_i = 1 / G  # Ohm
kappa_i = 0.7e6 * 2*np.pi* C
kappa_tot = kappa_c + kappa_QD + kappa_i


def Reflectance(omega):
    R = (1 - ((kappa_QD + kappa_i) * kappa_c) / ((kappa_tot / 2) ** 2 + (omega - omega_res - delomega_QD) ** 2))
    return R


x_omega = np.linspace((.999) * omega_res, (1.003) * omega_res, 501)

fig, ax = plt.subplots()
ax.plot(x_omega*1e-9/(2*np.pi), Reflectance(x_omega))
ax.set_title('Reflectance')
ax.set_xlabel('Frequency (GHz)')

print(Reflectance(x_omega[250]))

e = 1.602E-19
h = 6.626E-34
hbar = h / (2 * np.pi)
k_B = 1.38E-23

T = 10E-3

kT = k_B * T / e

Gam_L = 0.25E-6  # eV
Gam_R = 0.5E-6  # eV
alpha = 0.03
V_G0 = 6
V_G = 6.01
epsilon = alpha * (V_G - V_G0) * 0
epsilon_array = np.linspace(-10, 10, 101)




def dFdE(E):
    return 1 / (1 + np.exp(E)) * 1 / (1 + np.exp(-1 * E))


def TFunc(E):
    return ((Gam_L * Gam_R)/kT**2) / ((E - epsilon)**2 + ((Gam_L + Gam_R)**2 / (4*kT**2)))


def integrand(E):
    return (dFdE(E) * TFunc(E))


# def integrnd(E):
#    (np.exp(E/(k_B*T))/((k_B*T) * (1 + np.exp(E/(k_B*T)))**2))*((Gam_L*Gam_R)/(E - epsilon + 1j*(Gam_L+Gam_R)/2) * (1)/(E - epsilon - 1j*(Gam_L+Gam_R)/2))

G_omega = integrate.quad(integrand, -10, 10)
G_DC = []
for epsilon in epsilon_array:
    G_DC.append(integrate.quad(integrand, -10, 10)[0])

G_DC = np.array(G_DC)


epsilon_array2 = np.linspace(-25, 25, 101)

G_DC2 = []
for epsilon in epsilon_array:
    G_DC2.append(integrate.quad(integrand, -10, 10)[0])

G_DC2 = np.array(G_DC2)



fig = plt.figure()
plt.plot(epsilon_array, G_DC*2*e**2/h*1e6)
plt.title('Conductance')
plt.xlabel('epsilon')
plt.ylabel('G')
plt.show()



fig2 = plt.figure()
E_array = np.linspace(-10, 10, 1000)
epsilon = 0
plt.plot(E_array, TFunc(E_array))
plt.title('T(E)')
plt.show()


# fig2, ax2 = plt.subplots()
# ax2.plot(E_array, TFunc(E_array))
#
# fig3, ax3 = plt.subplots()
# ax3.plot(E_array, dFdE(E_array))

fig4, ax4 = plt.subplots()
ax4.plot(E_array, integrand(E_array))
ax4.set_title('Integrand(E)')

R_pk = np.empty(len(G_DC))
for i in range(len(G_DC)):
    kappa_QD = G_DC[i]*2*e**2/h / C
    R_i = 1 / G_DC[i]*2*e**2/h  # Ohm
    kappa_i = 0.7e6 * 2*np.pi* C
    kappa_tot = kappa_c + kappa_QD + kappa_i
    
    R_temp = np.empty(len(x_omega))
    for k in range(len(x_omega)):
        R_temp[k] = Reflectance(x_omega[k])
    R_pk[i] = min(R_temp)
    
fig5, ax5 = plt.subplots()
ax5.plot(G_DC*2*e**2/h*1e6, R_pk)

G_Arr = np.logspace(-7,-3,200)

R_pk2 = np.empty(len(G_Arr))
for i in range(len(G_Arr)):
    kappa_QD = G_Arr[i] / C
    R_i = 1 / G_Arr[i]  # Ohm
    kappa_i = 0.7e6 * 2*np.pi* C
    kappa_tot = kappa_c + kappa_QD + kappa_i
    
    R_temp = np.empty(len(x_omega))
    for k in range(len(x_omega)):
        R_temp[k] = Reflectance(x_omega[k])
    R_pk2[i] = min(R_temp)

ax5.set_xscale('log')
ax5.set_title('Minimum Reflectance')
ax5.set_xlabel('Conductance G (S * 10^-6)')

fig6, ax6 = plt.subplots()
ax6.plot(G_Arr, R_pk2)

ax6.set_title('Minimum Reflectance')
ax6.set_xlabel('Conductance G (S)')
ax6.set_xscale('log')

Refl_Eps = np.empty(len(epsilon_array2))
for i in range(len(G_DC2)):
    kappa_QD = G_DC[i]*2*e**2/h / C
    R_i = 1 / G_DC[i]*2*e**2/h  # Ohm
    kappa_i = 0.7e6 * 2*np.pi* C
    kappa_tot = kappa_c + kappa_QD + kappa_i
    #Refl_Eps[i] = Reflectance(x_omega[250])
    
    R_temp = np.empty(len(x_omega))
    for k in range(len(x_omega)):
        R_temp[k] = Reflectance(x_omega[k])
    Refl_Eps[i] = min(R_temp)
    
fig7, ax7 = plt.subplots() 
ax7.plot(epsilon_array2, Refl_Eps)
ax7.set_title('Minimum Reflectance at resonance')
ax7.set_xlabel('epsilon')

    