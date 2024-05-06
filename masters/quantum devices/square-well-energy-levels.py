from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np


def theta_func(x, theta, mf):
    return np.sqrt(mf * (theta / (x ** 2) - 1))


def tan_func(x):
    if 0 < np.tan(x) < 1000:
        t1 = np.tan(x)
    else:
        t1 = None
    if 0 < np.tan(x - 0.5 * np.pi) < 1000:
        t2 = np.tan(x - 0.5 * np.pi)
    else:
        t2 = None

    if t1 is None and t2 is None:
        return np.nan
    elif t1 is None:
        return t2
    elif t2 is None:
        return t1
    else:
        return t1 + t2


def intersections(x_list, fun_list, tan_list):
    tvals = []
    yvals = []
    iola = 0
    tlist = []
    ylist = []
    difflist = []
    for k, j in enumerate(fun_list):
        if k - iola > 2 and len(difflist) > 0:
            index = difflist.index(min(difflist))
            tvals.append(tlist[index])
            yvals.append(ylist[index])

            tlist = []
            ylist = []
            difflist = []
        if abs(tan_list[k] - j) < 0.1:
            tlist.append(x_list[k])
            ylist.append(j)
            difflist.append(abs(tan_list[k] - j))
            iola = k
    return tvals, yvals


def Energies(meff=1, VeV=1, a=1e-9, mb=1):
    m = 9.1093837015e-31
    hbar = 1.054571817e-34
    V = VeV * 1.602176634e-19
    theta = (m * meff * V * (a ** 2)) / (2 * (hbar ** 2))
    mf = meff / mb

    X = np.arange(0.001, 15 * np.pi, step=(0.001))
    Y1 = np.array([theta_func(i, theta, mf) for i in X])
    Y2 = np.array([tan_func(i) for i in X])

    tvals, yvals = intersections(X, Y1, Y2)
    Elist = [(hbar ** 2 / (2 * m * meff)) * 4 / a ** 2 * i ** 2 * 1 / 1.602176634e-19 for i in tvals]

    return Elist


def plot(line=None, canvas=None, plot1=None, fig=None):
    m = float(e1.get())
    V = float(e2.get())
    a = float(e3.get())
    mb = float(e4.get())

    Elist = Energies(m, V, a * 1e-9, mb)

    x = [-0.7 * a, 0, 0, a, a, 1.7 * a]
    w = [V, V, 0, 0, V, V]

    x2 = []
    e = []
    Alist = []
    prevE = -1
    md = V * 0.022
    for j, i in enumerate(Elist):
        x2 = x2 + [0, a, None]
        e = e + [i, i, None]
        if i - prevE > md:
            Alist.append([f'E{j + 1} = {i:.5f} eV', (1.02 * a, min(0.97 * V, i))])
            prevE = i
        else:
            Alist.append([f'E{j + 1} = {i:.5f} eV', (1.02 * a, min(0.97 * V, prevE + md))])
            prevE += md

    if line is None:
        fig = Figure(figsize=(6, 8), dpi=90)
        plot1 = fig.add_subplot(111)
        line, = plot1.plot(x, w, color='k')
        plot1.plot(x2, e, color='k', ls='--')
        plot1.fill(x, w, color="k", alpha=0.15)
        for i in Alist: plot1.annotate(i[0], xy=i[1], verticalalignment='center')
        plot1.set_xlabel('Distance (nm)')
        plot1.set_ylabel('Energy (eV)')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=140, y=-80)
    else:
        plot1.clear()
        plot1.plot(x, w, color='k')
        plot1.plot(x2, e, color='k', ls='--')
        plot1.fill(x, w, color="k", alpha=0.15)
        for i in Alist: plot1.annotate(i[0], xy=i[1], verticalalignment='center')
        plot1.set_xlabel('Distance (nm)')
        plot1.set_ylabel('Energy (eV)')

    canvas.draw()
    return line, canvas, plot1, fig


def plot2(line=None, canvas=None, plot1=None, fig=None):
    meff = float(e1.get())
    VeV = float(e2.get())
    a = float(e3.get())
    mb = float(e4.get())

    m = 9.1093837015e-31
    hbar = 1.054571817e-34
    V = VeV * 1.602176634e-19
    theta = (m * meff * V * ((a * 1e-9) ** 2)) / (2 * (hbar ** 2))
    mf = meff / mb

    X = np.arange(0.001, 15 * np.pi, step=(0.001))
    Y1 = np.array([theta_func(i, theta, mf) for i in X])
    Y2 = np.array([tan_func(i) for i in X])

    tvals, yvals = intersections(X, Y1, Y2)

    plot1.clear()
    plot1.plot(X, Y1, color='k')
    plot1.plot(X, Y2, color='k', ls='--')
    for a, b, c in zip(tvals, yvals, range(len(yvals))):
        plot1.scatter(a, b, 40, marker='o', zorder=2, label=f'Intersection for n = {int(c + 1)} at θ = {a:.3f}')
    plot1.set_xlabel('θ = ka/2 (unitless)')
    plot1.set_ylabel('f(θ) (unitless)')
    plot1.set_xlim(0, (int(2 * max(tvals) / np.pi) + 1) * 0.5 * np.pi)
    plot1.set_ylim(0, max(yvals) * 2)
    plot1.legend()

    canvas.draw()
    return line, canvas, plot1, fig


def plotter():
    global line, canvas, plot1, fig
    line, canvas, plot1, fig = plot(line, canvas, plot1, fig)


def plotter2():
    global line, canvas, plot1, fig
    line, canvas, plot1, fig = plot2(line, canvas, plot1, fig)


def save():
    global line, canvas, plot1, fig, pltnr
    fig.savefig(f'qw_plot_{pltnr}.png', dpi=200)
    pltnr += 1


def quit_me():
    window.quit()
    window.destroy()


window = Tk()
window.title('Paul\'s Finite Square Quantum Well Simulator™')
window.geometry("640x640")

plot_button = Button(master=window, command=plotter, height=2, width=15, text="Plot Well")
plot_button2 = Button(master=window, command=plotter2, height=2, width=15, text="Plot Intersections")
plot_button3 = Button(master=window, command=save, height=2, width=15, text="Save Plot")

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e1.insert(0, "0.067")
e2.insert(0, "0.5")
e3.insert(0, "10")
e4.insert(0, "0.067")

Label(window, text="Well Effective Mass:").place(x=10, y=0)
e1.place(x=10, y=21)
Label(window, text="Barrier Effective Mass:").place(x=10, y=60)
e4.place(x=10, y=81)
Label(window, text="Well Depth (eV):").place(x=10, y=120)
e2.place(x=10, y=141)
Label(window, text="Well Width (nm):").place(x=10, y=180)
e3.place(x=10, y=201)
plot_button.place(x=10, y=240)
plot_button2.place(x=10, y=290)
plot_button3.place(x=10, y=340)

line, canvas, plot1, fig = plot()
pltnr = 1

window.protocol("WM_DELETE_WINDOW", quit_me)
window.mainloop()
