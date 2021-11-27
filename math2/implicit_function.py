from numpy import *
import matplotlib.pyplot as mp
from scipy.optimize import fsolve

N = 1000
x1 = linspace(-1, 1, N)
y1 = linspace(-1, 1, N)
X, Y = meshgrid(x1, y1)


# Smoothness of z(x, y)
def f(x, y):
    return fsolve(lambda z: x + 2 * y + z + e ** (2 * z) - 1, array([1]))


Z = zeros((N, N))
for i in range(N):
    for j in range(N):
        Z[i, j] = f(X[i, j], Y[i, j])
#
ax = mp.axes(projection="3d")
ax.contour3D(X, Y, Z, 100)

# *****************************************
# # Coefficient of taylor polynomial P2(x, y)
h = 1e-6

A = (f(h, 0) - f(-h, 0)) / (2 * h)
B = (f(0, h) - f(0, -h)) / (2 * h)
C = (f(h, 0) - 2 * f(0, 0) + f(-h, 0)) / (2 * h ** 2)
D = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h ** 2)
E = (f(0, h) - 2 * f(0, 0) + f(0, -h)) / (2 * h ** 2)

print("A =", A, "\nB=", B, "\nC=", C, "\nD=", D, "\nE=", E)


#
#
# # *************************************
# Plot of P2(x, y)

def p2(x, y):
    return A * x + B * y + C * x ** 2 + D * x * y + E * y ** 2


ax.contour3D(X, Y, p2(X, Y), 100)
#
# # ****************************************
# Plot of absolute error e(x, y)
ax.contour3D(X, Y, abs(Z - p2(X, Y)), 100)
