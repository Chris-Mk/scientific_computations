import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
from labs.ssp.LDOS.clean_1D import g, H

# TASK 2 1D case
N = 502  # added one impurity

ones = np.ones((1, N))[0]  # just 1 x N matrix were all elements are 1
phi_i = np.diag(ones, k=0)  # N x N matrix were all elements in the main diagonal = 1


# construct the matrix in (9)
def H_ads(N, V_0, e_0):  # här det blir fel, ska vara N+1, blir istället N+2, löst, korrigerad

    add_column = np.zeros((N - 1, 1))
    add_column[0][0] = V_0

    H_intial = np.c_[H(N - 1), add_column]

    add_row = np.zeros((1, N))
    add_row[0][0] = V_0
    add_row[0][-1] = e_0

    H_final = np.r_[H_intial, add_row]

    return H_final


print(H_ads(N, 5, 4))

# a)

E_lambda, psi_lambda = eig(H_ads(N, V_0=0, e_0=-1))

# print(np.shape(phi_i))
# print(len(E_lambda))
# print(len(psi_lambda))

E = np.linspace(-6, 6, 1000)

plt.figure(figsize=(8, 6))

plt.plot(E, g(E, -1), label=r'$i=0$')  # ?
plt.plot(E, g(E, 0), label=r'$i=1$')
plt.plot(E, g(E, 1), label=r'$i=2$')
plt.plot(E, g(E, 2), label=r'$i=3$')
plt.plot(E, g(E, 4), label=r'$i=5$')
plt.plot(E, g(E, 9), label=r'$i=10$')
plt.plot(E, g(E, 49), label=r'$i=50$')
plt.plot(E, g(E, 99), label=r'$i=100$')
plt.plot(E, g(E, 250), label=r'$i=251$')

plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.title(r'$\epsilon_{0}=-1, V_{0}=0$')
plt.legend()
plt.show()

# b)

E_lambda, psi_lambda = eig(H_ads(N, V_0=-0.3, e_0=-1))

plt.figure(figsize=(8, 6))

plt.plot(E, g(E, -1), label=r'$i=0$')  # ?
plt.plot(E, g(E, 0), label=r'$i=1$')
plt.plot(E, g(E, 1), label=r'$i=2$')
plt.plot(E, g(E, 2), label=r'$i=3$')
plt.plot(E, g(E, 4), label=r'$i=5$')
plt.plot(E, g(E, 9), label=r'$i=10$')
plt.plot(E, g(E, 49), label=r'$i=50$')
plt.plot(E, g(E, 99), label=r'$i=100$')
plt.plot(E, g(E, 250), label=r'$i=251$')

plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.title(r'$\epsilon_{0}=-1, V_{0}=-0.3$')
plt.legend()
plt.show()

# c)
E_lambda, psi_lambda = eig(H_ads(N, V_0=3.0, e_0=-1))

plt.plot(E, g(E, -1), label=r'$i=0$')  # ?
plt.plot(E, g(E, 0), label=r'$i=1$')
plt.plot(E, g(E, 1), label=r'$i=2$')
plt.plot(E, g(E, 2), label=r'$i=3$')
plt.plot(E, g(E, 4), label=r'$i=5$')
plt.plot(E, g(E, 9), label=r'$i=10$')
plt.plot(E, g(E, 49), label=r'$i=50$')
plt.plot(E, g(E, 99), label=r'$i=100$')
plt.plot(E, g(E, 250), label=r'$i=251$')

plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.title(r'$\epsilon_{0}=-1, V_{0}=3.0$')
plt.legend()
plt.show()
