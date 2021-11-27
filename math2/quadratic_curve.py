from numpy import *
import matplotlib.pyplot as plt
from sympy import symbols, solveset, lambdify

ax = plt.axes(projection='3d')

x1 = linspace(-1, 1, 100)
x2 = linspace(-1, 1, 100)
X, Y = meshgrid(x1, x2)

x, y, z = symbols('x y z')
result = solveset(2 * z ** 2 - (4 * x - 10 * y) * z + 2 * x ** 2 - 10 * x * y - y ** 2 - 1, z)
f1 = lambdify((x, y), result.args[0], "numpy")
f2 = lambdify((x, y), result.args[1], "numpy")

ax.contour3D(X, Y, f1(X, Y), 150)
ax.contour3D(X, Y, f2(X, Y), 150)

# ax.set_zlim(-12, 12)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Graph")
