from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

# Samples used: 1A, 2A, 4, and 9
ion_energy = array([1250, 1000, 750, 500])
milling_rate = array([42, 62, 19, 6.50])
milling_time = array([30, 30, 60, 240])
slope, y_inter, *a = linregress(ion_energy, milling_rate)

# subplot(121)
grid()
# title("Acceleration voltage")
xlabel("Ion energy [V]")
ylabel("Milling rate [nm/min]")
# plot(ion_energy, milling_rate)
plot(ion_energy, milling_rate, "ro", label="data point")
plot(ion_energy, slope * ion_energy + y_inter, label="linear regression")
errorbar(ion_energy, milling_rate, xerr=50, yerr=milling_rate * (10 / milling_time), ls="none",
         label="error bar")
legend(loc='upper left')
# savefig("./thesis/images/ion-energy-dependence.pdf")


# time = array([0, 1, 4, 7])
# milled_oxide = array([0, 8, 24, 46])
# slope, y_inter, *a = linregress(time, milled_oxide)
#
# subplot(122)
# grid()
# xlabel("Time [min]")
# ylabel("Oxide milled [nm]")
# plot(time, milled_oxide, "ro", label="data point")
# plot(time, slope * time + y_inter, label="linear regression")
# errorbar(time[1:], milled_oxide[1:], xerr=0.17, yerr=5, ls="none")
# legend()
