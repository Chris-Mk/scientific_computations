from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import fmin

#
x_axis = linspace(-2, 4, 100)
y_axis = linspace(-2, 6, 100)
X, Y = meshgrid(x_axis, y_axis)
Z = 8 * X * Y - 4 * X ** 2 * Y - 2 * X * Y ** 2 + X ** 2 * Y ** 2
contours = contour(X, Y, Z, 50, cmap="RdGy")
clabel(contours, inline=True, fontsize=8)
colorbar()


def f(xy):
    x, y = xy
    return -(8 * x * y - 4 * x ** 2 * y - 2 * x * y ** 2 + x ** 2 * y ** 2)


m = fmin(f, (-1, 2), retall=True)
print(m[0])

xq = list()
yq = list()
for j in m[1]:
    xq.append(j[0])
    yq.append(j[1])

plot(xq, yq)
