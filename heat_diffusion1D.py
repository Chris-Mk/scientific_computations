import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import *
from scipy.special import erf

alpha = 1
N = 100
x_range = linspace(-3, 3, N)
t_range = linspace(0, 3, N)
X, T = meshgrid(x_range, t_range)
y_lim = 0.5


def u(x, t):
    z1 = (y_lim - x) / sqrt(4 * alpha * t)
    z2 = (-y_lim - x) / sqrt(4 * alpha * t)
    return 0.5 * (erf(z1) - erf(z2))


def plot_wave(x, t, wave, i):
    plt.clf()
    plt.grid()
    plt.ylim(0, 1)
    plt.title(f"Temperature at t={t[i]:.3f} seconds")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.plot(x, wave[i])


u_wave = u(X, T)
anim = animation.FuncAnimation(plt.figure(), lambda i: plot_wave(x_range, t_range, u_wave, i),
                               interval=0.005, frames=N, repeat=False)
