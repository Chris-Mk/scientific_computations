import matplotlib.animation as animation
from matplotlib.pyplot import *
from numpy import *
from scipy.special import erf

N = 1000
lim = 7e6
x_range = y_range = linspace(0, lim, N)
X, Y = meshgrid(x_range, y_range)
rx = ry = (6.3e6 / sqrt(2)) - 6.9e4
r_max = 1e6
u0 = 10000

E = zeros((N, N))
A = zeros((N, N))

E[X ** 2 + Y ** 2 <= 6.3e6 ** 2] = 2000  # crust
E[X ** 2 + Y ** 2 <= 3.5e6 ** 2] = 4000  # mantle
E[X ** 2 + Y ** 2 <= 1.2e6 ** 2] = 7000  # core

A[X ** 2 + Y ** 2 > 6.3e6 ** 2] = 1e-50  # air
A[X ** 2 + Y ** 2 <= 6.3e6 ** 2] = 1e-5  # crust
A[X ** 2 + Y ** 2 <= 3.5e6 ** 2] = 1e-6  # mantle
A[X ** 2 + Y ** 2 <= 1.2e6 ** 2] = 1e-7  # core


def u(x, y, t, alpha):
    r = sqrt((x - rx) ** 2 + (y - ry) ** 2)
    z1 = (r_max - r) / sqrt(4 * alpha * t)
    z2 = (-r_max - r) / sqrt(4 * alpha * t)
    return 0.5 * u0 * (erf(z1) - erf(z2))


def animate(t):
    t = t * 1e15
    clf()
    title(f"Temperature at t={t:.3f} time (yr)")
    xlabel("x in m")
    ylabel("y in m")
    imshow(E + u(X, Y, t, A), interpolation="bilinear", cmap="jet", vmin=0, vmax=u0,
           extent=(0, lim, 0, lim), origin="lower")
    colorbar()


anim = animation.FuncAnimation(figure(), animate, interval=0.01, frames=N, repeat=False)
