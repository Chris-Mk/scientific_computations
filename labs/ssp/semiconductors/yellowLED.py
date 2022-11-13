from matplotlib.pyplot import *
from numpy import *

I = array([32.5, 28.1, 24.9, 21.1, 17.3, 13.3, 9.5, 6.3, 2.8, 0.15, 0.0001, 0, 0, 0]) * 10 ** -3
V_drop = array([2.09, 2.08, 2.07, 2.05, 2.03, 2.01, 1.98, 1.95, 1.9, 1.71, 1.34, 1.01, 0.56, 0.15])
V_source = flip(linspace(0.2, 5.4, 14))
intensity = array([0.83, 0.81, 0.8, 0.78, 0.7, 0.52, 0.33, 0.19, 0.06, 0, 0, 0, 0, 0])

grid()
# xlabel("Voltage, V [volt]")
# ylabel("Current, I [mA]")
# plot(V_drop, I, "ro", label="data points")
# plot(V_drop, I)

xlabel("Supply Voltage, V [volt]")
ylabel("Intensity [counts]")
plot(I, intensity, "ro", label="data points")
plot(I, intensity)
# savefig("./graphs/yellow_intensity_before.pdf")
legend()
