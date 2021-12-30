import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import *


def wave_maker(A, B, t, x, omega, k):
    x, t = np.meshgrid(x, t)
    return A * np.sin(k * x + omega * t) + B * np.cos(k * x + omega * t)


def plot_wave(xvals, wave, t, i):
    # Clear the current plot figure
    plt.clf()
    plt.title(f"Wave at t = {t[i]:.0f} seconds")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.ylim(-1.1, 1.1)
    # This is to plot u_k (u at time-step k)
    plt.plot(xvals, wave[i], color='yellow')
    return plt


def animate(i):
    plot = plot_wave(xrange, wave, times, i)


max_iterations = 60
# frame_scaling = 4
times = np.arange(0, max_iterations, 1)
xrange = np.linspace(0, 10, max_iterations)
omega = np.pi
k = 2.5
wave = wave_maker(A=0.9, B=0.5, t=times, x=xrange, omega=omega, k=k)
anim = animation.FuncAnimation(plt.figure(), animate, interval=1,
                               frames=max_iterations, repeat=False)
# anim.save("sinwave.gif", fps=10, writer='pillow')
# print('done')
