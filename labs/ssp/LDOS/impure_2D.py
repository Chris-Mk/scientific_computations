from labs.ssp.LDOS.clean_2D import convert_site_to_m
import matplotlib.pyplot as plt
from numpy.linalg import eig
from labs.ssp.LDOS.clean_2D import g, H, N, E
import numpy as np

# for center adsorbate and impurity plots in task 4
# -----------------------------BEGIN CENTER------------------
V_0 = -5
e_0 = -2
# center adsorbate
i1 = convert_site_to_m([0, 0])
i2 = convert_site_to_m([1, 0])
i3 = convert_site_to_m([0, 1])
i4 = convert_site_to_m([1, 1])

add_column = np.zeros((N * N, 1))

add_column[i1][0] = V_0 / 2
add_column[i2][0] = V_0 / 2
add_column[i3][0] = V_0 / 2
add_column[i4][0] = V_0 / 2
add_row = np.zeros((1, N * N + 1))
add_row[0][i1] = V_0 / 2
add_row[0][i2] = V_0 / 2
add_row[0][i3] = V_0 / 2
add_row[0][i4] = V_0 / 2
add_row[0][-1] = e_0

H_intial = np.c_[H(N), add_column]

H_final = np.r_[H_intial, add_row]

E_lambda, psi_lambda = eig(H_final)

plt.figure(figsize=(8, 6))

plt.plot(E, g(E, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, g(E, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, g(E, convert_site_to_m([1, 0])), label=r'$1,0$')
plt.plot(E, g(E, convert_site_to_m([1, 1])), label=r'$1,1$')

plt.title(r'$\epsilon_{0}=-2.0, V_{0}=-5.0 $')
plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E[a.u]')
plt.legend()
plt.show()

# -------------Begin impurity-----------------------------
ones = np.ones((1, N * N))[0]  # just 1 x N*N matrix were all elements are 1
phi_i = np.diag(ones, k=0)  # N*N x N*N matrix with were all elemnts in the main diagonal = 1

V_0 = -5
e_0 = -2

i0 = convert_site_to_m([0, 0])
i1 = convert_site_to_m([1, 0])
i2 = convert_site_to_m([0, 1])
i3 = convert_site_to_m([-1, 0])
i4 = convert_site_to_m([0, -1])

N = 81
a = H(N)
a[i0][i0] = e_0
a[i1][i1] = V_0 / 2
a[i2][i2] = V_0 / 2
a[i3][i3] = V_0 / 2
a[i4][i4] = V_0 / 2

E_lambda, psi_lambda = eig(a)

plt.figure(figsize=(8, 6))

plt.plot(E, g(E, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, g(E, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, g(E, convert_site_to_m([1, 0])), label=r'$1,0$')
plt.plot(E, g(E, convert_site_to_m([-1, 0])), label=r'$-1,0$')
plt.plot(E, g(E, convert_site_to_m([0, -1])), label=r'$0,-1$')

plt.title(r'$\epsilon_{0}=-2.0, V_{0}=-5 $')
plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E[a.u]')
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

e_0 = -2
V_0 = -3
adbridge = [[0, 0], [1, 0]]
add_column = np.zeros((N * N, 1))
add_column[convert_site_to_m(adbridge[0])][0] = V_0 / np.sqrt(2)
add_column[convert_site_to_m(adbridge[1])][0] = V_0 / np.sqrt(2)
add_row = np.zeros((1, N * N + 1))
add_row[0][convert_site_to_m(adbridge[0])] = V_0 / np.sqrt(2)
add_row[0][convert_site_to_m(adbridge[1])] = V_0 / np.sqrt(2)
add_row[0][-1] = e_0
H_adbridge = np.c_[H(N), add_column]
H_adbridge_f = np.r_[H_adbridge, add_row]
print(H_adbridge_f)
E_lambda, psi_lambda = LA.eig(H_adbridge_f)


def LocalDensityOfState(E, Eigvec, gamma, I):
    summa = 0
    for p in range(len(Eigvec[0])):
        numerator = abs((Eigvec[I][p])) ** 2
        denominator = (E - E_lambda[p]) ** 2 + gamma ** 2  # Denna verkar bäst, på N = 3 gav den samma som samuel
        summa += numerator / denominator
    return summa * gamma / np.pi


plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([1, 1])), label=r'$1,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 0])), label=r'$2,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 1])), label=r'$2,1$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 2])), label=r'$2,2$')

plt.title(r'$\epsilon_0 = -1, V_0=-5$')
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

e_0 = -2
V_0 = -3
adbridge = [[0, 0], [1, 0]]
add_column = np.zeros((N * N, 1))
add_column[convert_site_to_m(adbridge[0])][0] = V_0 / np.sqrt(2)
add_column[convert_site_to_m(adbridge[1])][0] = V_0 / np.sqrt(2)
add_row = np.zeros((1, N * N + 1))
add_row[0][convert_site_to_m(adbridge[0])] = V_0 / np.sqrt(2)
add_row[0][convert_site_to_m(adbridge[1])] = V_0 / np.sqrt(2)
add_row[0][-1] = e_0
H_adbridge = np.c_[H(N), add_column]
H_adbridge_f = np.r_[H_adbridge, add_row]
print(H_adbridge_f)
E_lambda, psi_lambda = LA.eig(H_adbridge_f)


def LocalDensityOfState(E, Eigvec, gamma, I):
    summa = 0
    for p in range(len(Eigvec[0])):
        numerator = abs((Eigvec[I][p])) ** 2
        denominator = (E - E_lambda[p]) ** 2 + gamma ** 2  # Denna verkar bäst, på N = 3 gav den samma som samuel
        summa += numerator / denominator
    return summa * gamma / np.pi


plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([0, 0])), label=r'$0,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([0, 1])), label=r'$0,1$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([1, 1])), label=r'$1,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 0])), label=r'$2,0$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 1])), label=r'$2,1$')
plt.plot(E, LocalDensityOfState(E, psi_lambda, 0.05, convert_site_to_m([2, 2])), label=r'$2,2$')

plt.title(r'$\epsilon_0 = -1, V_0=-5$')
plt.ylabel(r'$g(E,\Gamma)$')
plt.xlabel('E')
plt.legend()
plt.show()