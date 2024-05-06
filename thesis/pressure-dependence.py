from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

# pressure = array([0, 0.00004, 0.00005, 0.00007])
# milling_rate = array([0, 4, 5.25, 6.75])
pressure = array([0, 0.00004, 0.00005, 0.00007, 0.0001, 0.0002])
milling_rate = array([0, 4, 5.25, 6.75, 6.5, 7])
slope, y_inter, *a = linregress(pressure[0:4], milling_rate[0:4])

grid()
xlabel("Pressure [Torr]")
ylabel("Milling rate [nm/min]")
ticklabel_format(axis="x", style="sci", scilimits=(-4, -4))
# plot(pressure, milling_rate)
plot(pressure, milling_rate, "ro", label="data point")
# plot(pressure[0:4], slope * pressure[0:4] + y_inter, label="linear regression")
errorbar(pressure, milling_rate, xerr=pressure * 0.15, yerr=milling_rate * .10, ls="none", label="error bar")
legend()
# savefig("./thesis/images/pressure-dependence.pdf")
