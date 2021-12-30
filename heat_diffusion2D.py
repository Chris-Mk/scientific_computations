import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import *
from scipy.special import erf

N = 100
x_range = linspace(0, 50, N)
y_range = linspace(0, 50, N)
X, Y = meshgrid(x_range, y_range)
alpha, u0 = 2, 100
rx, ry, r_max = 17.5, 37.5, 2.5


def u(x, y, t):
    r = sqrt((x - rx) ** 2 + (y - ry) ** 2)
    z1 = (r_max - r) / sqrt(4 * alpha * t)
    z2 = (-r_max - r) / sqrt(4 * alpha * t)
    return 0.5 * u0 * (erf(z1) - erf(z2))


# def plot_fig(i, t):
#     plt.title(f"Temperature at t={t[i]:.3f} seconds")
#     cax.set_array(u_wave[:-1, :-1, i].flatten())


def animate(i):
    plt.clf()
    plt.title(f"Temperature at t={i:.3f} seconds")
    plt.imshow(u(X, Y, i), cmap="jet", vmin=0, vmax=100, extent=(0, 50, 0, 50), origin="lower")
    plt.colorbar()


# u_wave = u(X, Y, t_range)
# fig, ax = plt.subplots()
# cax = ax.pcolormesh(x_range, y_range, u_wave[:-1, :-1, 0], cmap="jet")
# fig.colorbar(cax)
# plt.imshow(u_wave, cmap="jet")

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=30, repeat=False)
# plt.xlabel("x")
# plt.ylabel("y")
