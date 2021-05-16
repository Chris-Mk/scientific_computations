from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 6, 6)
t = array([13.73, 3.50, 1.55, 0.86, 0.56, 0.43])

grid()
xlabel("number of bound states, n")
ylabel("period, T [fs]")
title("Graph of no. of bound state vs period.")

plot(n, t, "ro", label="data points")
plot(n, t)
legend()

savefig("./graphs/nVsPeriod.pdf")

