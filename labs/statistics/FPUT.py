# ====MODULES====
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt


# ====FUNCTIONS====
def calcF(u, alpha):
    F = np.zeros([N - 1, 1])
    F[0] = u[1] - 2 * u[0] + alpha * (u[1] - u[0]) ** 2 - alpha * u[0] ** 2
    for x in range(1, N - 2):
        F[x] = u[x + 1] - 2 * u[x] + u[x - 1] + alpha * (u[x + 1] - u[x]) ** 2 - alpha * (u[x] - u[x - 1]) ** 2
    F[N - 2] = - 2 * u[N - 2] + u[N - 3] + alpha * u[N - 2] ** 2 - alpha * (u[N - 2] - u[N - 3]) ** 2
    return F


def calcE(u, v, eigenValues, eigenVectors):
    E = np.zeros([4, 1])
    for x in range(0, 4):
        E[x] = 0.5 * ((sum(np.array(eigenVectors[:, x]) * v)) ** 2 + eigenValues[x] ** 2 * (
            sum(np.array(eigenVectors[:, x]) * u)) ** 2)
    return E


# ====DEFINING MATRIX====
N = 32
dl = - np.ones(N - 1)
d0 = 2 * np.ones(N - 1)
d = np.vstack((dl, d0, dl))
A = sparse.spdiags(d, (-1, 0, 1), N - 1, N - 1).todense()

# ====CALCULATING EIGENVALUES/VECTORS====
eigenValues, eigenVectors = np.linalg.eig(A)

idx = eigenValues.argsort()
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:, idx]

# ====FREQUENCIES====
wNum = np.sqrt(eigenValues)
wAnalyt = 2 * np.sin(np.array(range(1, N)) * np.pi / (2 * N))

# print(wNum)
# print(wAnalyt)

# ====DYNAMICS====
# -PARAMETERS-
delta = np.sqrt(1 / 8)
alpha = 0.25
nt = 50000

# -INITIAL CONDITIONS-
u = 4 * np.array(eigenVectors[:, 0])
v = np.zeros([N - 1, 1])
F = calcF(u, alpha)
E = np.transpose(calcE(u, v, eigenValues, eigenVectors))

# -LOOP-
for x in range(0, nt):
    uNew = u + v * delta + 0.5 * F * delta ** 2
    FNew = calcF(uNew, alpha)
    vNew = v + 0.5 * delta * (FNew + F)
    ENew = np.transpose(calcE(u, v, eigenValues, eigenVectors))
    u = uNew
    F = FNew
    v = vNew
    E = np.vstack((E, ENew))

# ====PLOTS====
x = np.array(range(0, nt + 1)) * delta * wNum[0] / (2 * np.pi)
y1 = 100 * E[:, 0]
y2 = 100 * E[:, 1]
y3 = 100 * E[:, 2]
y4 = 100 * E[:, 3]

plt.plot(x, y1, label='1')
plt.plot(x, y2, label='2')
plt.plot(x, y3, label='3')
plt.plot(x, y4, label='4')
plt.xlim([0, 160])
plt.ylim([0, 8])
plt.ylabel("$E_n (x10^{-2})$")
plt.xlabel("$\omega_1t/2\pi$")
plt.legend()
plt.show()
# plt.savefig("./graphs/FPUT_1.pdf")
