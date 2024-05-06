from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

time = array([0, 1, 4, 7])
milled_oxide = array([0, 8, 24, 46])
slope, y_inter, *a = linregress(time, milled_oxide)

grid()
xlabel("Time [min]")
ylabel("Oxide milled [nm]")
plot(time, milled_oxide, "ro", label="data point")
plot(time, slope * time + y_inter, label="linear regression")
errorbar(time[1:], milled_oxide[1:], xerr=0.167, yerr=5, ls="none", label="error bar")
legend()
# savefig("./thesis/images/time-dependence.pdf")
