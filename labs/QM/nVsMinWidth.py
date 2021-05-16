from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

n = linspace(1, 8, 8)
d = array([.1, .3, .6, .9, 1.2, 1.4, 1.7, 2])
slope, y_inter, *a = sp.linregress(d, n)

grid()
xlabel("min width, d [nm]")
ylabel("number of bound states, n")
title("Graph of no. of bound states vs min width of well.")

plot(d, n, "ro",  label="data points")
plot(d, slope * d + y_inter, label="linear regression")
legend()

savefig("./graphs/nVsMinWidth.pdf")

