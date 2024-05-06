from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from numpy import tan
from numpy import sqrt
from numpy import linspace
from numpy import nan

def theta_func(x, theta):
    return sqrt((theta)/(x**2) - 1)

def tan_func(x):
    if 0 < tan(x) < 1000: t1 = tan(x)
    else: t1 = None
    if 0 < tan(x-0.5*3.141592653589793) < 1000: t2 = tan(x-0.5*3.141592653589793)
    else: t2 = None
    
    if t1==None and t2==None: return nan
    elif t1==None: return t2
    elif t2==None: return t1
    else: return t1+t2
    
def intersections(x_list, fun_list, tan_list):
    tvals = []
    yvals = []
    iola = 0
    for k, j in enumerate(fun_list):
        if k==0:
            tlist = []
            ylist = []
            difflist = []
        if k-iola > 5 and len(difflist)>0:
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

def Energies(meff=1, VeV=1, a=1e-9):
    m       = 9.1093837015e-31
    hbar    = 1.054571817e-34
    V       = VeV*1.602176634e-19
    theta   = (m*meff*V*(a**2)) / (2*(hbar**2))

    X = linspace(0, 20*3.141592653589793, 20000)
    Y1 = [theta_func(i, theta) for i in X]
    Y2 = [tan_func(i) for i in X]
    
    tvals, yvals = intersections(X, Y1, Y2)
    Elist = [(hbar**2/(2*m*meff)) * 4/a**2 * i**2 * 1/1.602176634e-19 for i in tvals]
    
    return Elist

def plot(line=None, canvas=None, plot1=None):
    m = float(e1.get())
    V = float(e2.get())
    a = float(e3.get())
    
    Elist = Energies(m, V, a*1e-9)
    
    x = [-a/2, 0, 0, a, a, a/2+a]
    w = [V, V, 0, 0, V, V]
    
    x2 = []
    e = []
    levelstring = f'{len(Elist)} energy levels at:'
    for j,i in enumerate(Elist):
        x2 = x2 + [0, a, None]
        e = e + [i, i, None]
        levelstring = levelstring + f'\nE{j+1} = {i:.5f} eV'
    
    if line==None:
        fig = Figure(figsize = (10, 10), dpi = 90)
        plot1 = fig.add_subplot(111)
        line, = plot1.plot(x, w, color='k')
        plot1.plot(x2, e, color='k', ls='--', label=levelstring)
        plot1.set_xlabel('Distance (nm)')
        plot1.set_ylabel('Energy (eV)')
        plot1.legend()
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True)
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas_widget.pack(expand=True)
    else:
        plot1.clear()
        plot1.plot(x, w, color='k')
        plot1.plot(x2, e, color='k', ls='--', label=levelstring)
        plot1.set_xlabel('Distance (nm)')
        plot1.set_ylabel('Energy (eV)')
        plot1.legend()
        
    canvas.draw()
    return line, canvas, plot1

def plotter():
    global line, canvas, plot1
    line, canvas, plot1 = plot(line, canvas, plot1)
    
def quit_me():
    window.quit()
    window.destroy()
    
window = Tk() 
window.title('Paul\'s Finite Square Quantum Well Simulator™') 
window.geometry("500x600") 

plot_button = Button(master = window, command = plotter, height = 2, width = 15, text = "Plot")

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.insert(0, "0.067")
e2.insert(0, "0.5")
e3.insert(0, "10")

Label(window, text="Effective mass:").pack()
e1.pack()
Label(window, text="Well Depth (eV):").pack()
e2.pack()
Label(window, text="Well Width (nm):").pack()
e3.pack()
plot_button.pack()

line, canvas, plot1 = plot()

window.protocol("WM_DELETE_WINDOW", quit_me)
window.mainloop()


