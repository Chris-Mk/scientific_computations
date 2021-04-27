from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp
# from numpy.polynomial.polynomial import polyfit


p = array([105000, 86600, 20900])
t = array([367, 289, 77])
x = linspace(0, 77, 20)
slope, y_inter, *a = sp.linregress(t, p)

grid()
xlabel("Temperature,T [K]")
ylabel("Pressure,P [Pa]")
title("Graph of pressure vs temperature.")
ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

plot(t, p, "ro", label="data")
plot(t, slope * t + y_inter, "b-", x, slope * x + y_inter, "b--")
legend()
# savefig("./graphs/pressureVsTemp.pdf")

