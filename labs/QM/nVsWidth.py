from numpy import *
from matplotlib.pyplot import *

n = array([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8])
d = linspace(0.1, 2, 20)

grid()
xlabel("width, d [nm]")
ylabel("number of bound states, n")
title("Graph of no. of bound states vs width of well.")

plot(d, n)
savefig("./graphs/nVsWidth.pdf")
