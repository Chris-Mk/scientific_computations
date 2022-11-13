import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig

# onsite energy

e = 0

# hopping term

V = -1

gamma = 0.05

# number of atoms

N = 501

ones = np.ones((1, N))[0]  # just 1 x N matrix were all elements are 1
phi_i = np.diag(ones, k=0)  # N x N matrix with were all elemnts in the main diagonal = 1


def H(N):  # create the Hamiltonian matrix

    main_diagonal = np.ones((1, N))[0] * e  # creating the main diagonal
    sub_diagonal = np.ones((1, N - 1))[0] * V  # creating the sub diagonals

    A = np.diag(main_diagonal, k=0)
    B = np.diag(sub_diagonal, k=1)
    C = np.diag(sub_diagonal, k=-1)

    return A + B + C


# find the eigenvalues and eigenvectors of the hamiltonian

E_lambda, psi_lambda = eig(H(N))


def g(E, i):
    a = []
    for lam in range(N):  # the set of lambda
        num = abs(np.dot(phi_i[:, i], psi_lambda[:, lam])) ** 2
        den = (E - E_lambda[lam]) ** (2) + gamma ** 2

        a.append(num / den)

    return (gamma / np.pi) * sum(a)


E = np.linspace(-6, 6, 1000)

plt.figure(figsize=(8, 6))

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
plt.legend()
plt.show()
