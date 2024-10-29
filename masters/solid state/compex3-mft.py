# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:50:55 2021

@author: Erik
"""
import numpy as np
import matplotlib.pyplot as plt


def f(m, B, T):
    return -np.tanh((B - 2 * m) / T) / 2


def fake_tanh(x):
    return x - x ** 3 / 3


def f0(m, B, T):
    return -fake_tanh((B - 2 * m) / T) / 2


def solve(B, T, m0, n_cycles=100, f=f):
    for _ in range(n_cycles):
        m0 = f(m0, B, T)
    return m0


# %% M(T) at B=0
eps = 0.01

Ts = np.linspace(0, 2, 101)[1:]
Ms = [solve(0, T, eps) for T in Ts]

plt.plot(Ts, Ms, label='exact')

T_approx = np.linspace(0.5, 2, 101)[1:]
M_approx = [solve(0, T, eps, f=f0) for T in T_approx]

plt.plot(T_approx, M_approx, label='approx.')
plt.xlabel('T')
plt.ylabel('m')
plt.legend()

plt.savefig('fig3a.pdf')
plt.show()
# %% Close to Tc. Need many cycles!
eps = 0.5

Tsmall = np.linspace(0.6, 1, 101, endpoint=False)[1:]
Ms = [solve(0, T, eps, n_cycles=1000) for T in Tsmall]

plt.plot(1 - Tsmall, Ms, label='tanh')

M_approx = [solve(0, T, eps, f=f0, n_cycles=1000) for T in Tsmall]

plt.plot(1 - Tsmall, M_approx, label='approx')

plt.plot(1 - Tsmall, (1 - Tsmall) ** 0.5 * np.sqrt(3) / 2, c='black', label=r'$1/2 \sqrt{3} (1-T)^{1/2}$')

plt.xlabel(r'$1-T$')
plt.ylabel(r'$m(T)$')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.savefig('fig3b.pdf')
plt.show()

# %% m(T) for T<T_c

T0 = 0.8
Bs = np.linspace(-1, 1, 101)

eps = 0.5
Ms = [solve(B, T0, eps, n_cycles=1000) for B in Bs]
plt.plot(Bs, Ms, label='$+\\varepsilon$')

Ms = [solve(B, T0, -eps, n_cycles=1000) for B in Bs]
plt.plot(Bs, Ms, label='$-\\varepsilon$')

Ms = [solve(B, T0, 0, n_cycles=1000) for B in Bs]
plt.plot(Bs, Ms, label='0')

plt.xlabel(r'$B$')
plt.ylabel(r'$m$')
plt.legend(title='$m_0$')
plt.title('T=0.8')
plt.savefig('fig3c.pdf')

plt.show()

# %% m(T) and chi(T) for T>T_c

T0 = 1.2
Bs = np.linspace(-1, 1, 101)

Ms = [solve(B, T0, 0, n_cycles=1000) for B in Bs]
plt.plot(Bs, Ms, label='$m$')
Bmids = (Bs[:-1] + Bs[1:]) / 2.
plt.plot(Bmids, np.diff(Ms) / np.diff(Bs), label=r'$\chi=dm/dB$')

plt.xlabel(r'$B$')
# plt.ylabel(r'$$')
plt.legend(loc='lower right')
plt.savefig('fig3d.pdf')

plt.show()

# %% gamma exponent
eps = 0.00001

Tsmall = np.linspace(2, 1, 101, endpoint=False)[1:]
chis = [-solve(eps, T, eps, n_cycles=1000) / eps for T in Tsmall]
plt.plot(Tsmall - 1, chis, label='-chi', marker='x')

plt.plot(Tsmall - 1, (Tsmall - 1) ** -1 * 0.5, c='black', label=r'$1/2 (T-1)^{-1}$')

plt.xlabel(r'$T-1$')
plt.ylabel(r'$\chi(T)$')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.savefig('fig3e.pdf')
plt.show()
