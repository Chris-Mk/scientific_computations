import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

# onsite energy
e = 0

# hopping term

V = -1

gamma = 0.05
# number of atoms
N = 81
N_h = (N + 1) / 2  # N_h is defined in the manual
N_hprime = (N - 1) / 2
ones = np.ones((1, N * N))[0]  # just 1 x N*N matrix were all elements are 1
phi_i = np.diag(ones, k=0)  # N*N x N*N matrix with were all elemnts in the main diagonal = 1


def H(N):  # The Hamiltonian
    H = np.zeros((N * N, N * N))  # to create a zero matrix
    N_h = (N + 1) / 2  # N_h is defined in the manual
    N_hprime = (N - 1) / 2
    m = []
    for i in range(N * N):
        m.append(i)
    for i in m:
        if i - N + 1 >= N:
            H[i][i - N] = H[i - N][i] = V
        if i + N + 1 <= N * N:
            H[i][i + N] = H[i + N][i] = V
        if (i + 1 + 1) % N != 1 and i + 1 + 1 <= N * N:
            H[i][i + 1] = H[i + 1][i] = V
        if (i + 1 - 1) % N != 0 and i + 1 - 1 >= 1:
            H[i][i - 1] = H[i - 1][i] = V
    for i in m:
        H[i][i] = e
    return H


print(H(N))

E_lambda, psi_lambda = LA.eig(H(N))
print(E_lambda)
print(psi_lambda)


def g(E, i):
    a = []
    for lam in range(N * N):  # the set of lambda
        num = abs(np.dot(phi_i[:, i], psi_lambda[:, lam])) ** 2
        den = (E - E_lambda[lam]) ** (2) + gamma ** 2

        a.append(num / den)

    return (gamma / np.pi) * sum(a)


def convert_site_to_m(a):  # This converts the site to m
    m = N * (a[0] + N_h - 1) + (a[1] + N_h)
    return int(m)


E = np.linspace(-8, 8, 1000)

plt.figure(figsize=(8, 6))

plt.plot(E, g(E, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, g(E, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, g(E, convert_site_to_m([1, 0])), label=r'$1,0$')
# plt.plot(E,g(E,convert_site_to_m([2,0])), label=r'$2,0$')
# plt.plot(E,g(E,convert_site_to_m([2,1])), label=r'$2,1$')
# plt.plot(E,g(E,convert_site_to_m([2,2])), label=r'$2,2$')


plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

e = 0

# hopping term

V = -1

gamma = 0.05
# number of atoms
N = 81
N_h = (N + 1) / 2  # N_h is defined in the manual
N_hprime = (N - 1) / 2
ones = np.ones((1, N * N))[0]  # just 1 x N*N matrix were all elements are 1
phi_i = np.diag(ones, k=0)  # N*N x N*N matrix with were all elemnts in the main diagonal = 1


def H(N):  # The Hamiltonian
    H = np.zeros((N * N, N * N))  # to create a zero matrix
    N_h = (N + 1) / 2  # N_h is defined in the manual
    N_hprime = (N - 1) / 2
    m = []
    for i in range(N * N):
        m.append(i)
    for i in m:
        if i - N + 1 >= N:
            H[i][i - N] = H[i - N][i] = V
        if i + N + 1 <= N * N:
            H[i][i + N] = H[i + N][i] = V
        if (i + 1 + 1) % N != 1 and i + 1 + 1 <= N * N:
            H[i][i + 1] = H[i + 1][i] = V
        if (i + 1 - 1) % N != 0 and i + 1 - 1 >= 1:
            H[i][i - 1] = H[i - 1][i] = V
    for i in m:
        H[i][i] = e
    return H


print(H(N))

eigval, eigvec = LA.eig(H(N))


# print(E_lambda)
# print(psi_lambda)


def LocalDensityOfState(E, Eigvec, gamma, I):
    summa = 0
    for p in range(len(Eigvec[0])):
        numerator = abs((Eigvec[I][p])) ** 2
        denominator = (E - eigval[p]) ** 2 + gamma ** 2
        summa += numerator / denominator
    return summa * gamma / np.pi


# def g(E,i):

# a=[]
# for lam in range(N): #the set of lambda
# num= abs(np.dot(phi_i[:,i],psi_lambda[:,lam]))**2
# den=  (E-E_lambda[lam])**(2) + gamma**2

# a.append(num/den)


# return (gamma/np.pi)*sum(a)

def convert_site_to_m(a):  # This converts the site to m
    m = N * (a[0] + N_h - 1) + (a[1] + N_h)
    return int(m - 1)


E = np.linspace(-8, 8, 1000)
G = []
for i in range(len(E)):
    G.append(LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([0, 0])))
print(G)
plt.figure(figsize=(8, 6))

plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([1, 1])), label=r'$1,0$')
plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([2, 0])), label=r'$2,0$')
plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([2, 1])), label=r'$2,1$')
plt.plot(E, LocalDensityOfState(E, eigvec, 0.05, convert_site_to_m([2, 2])), label=r'$2,2$')

plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.legend()
plt.show()