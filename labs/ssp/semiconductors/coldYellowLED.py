from matplotlib.pyplot import *
from numpy import *

I = array([24.55, 20.09, 16.58, 12.93, 9.42, 5.54, 2.81, 0.91, 0.035, 0.0002, 0, 0, 0, 0]) * 10 ** -3
V_drop = array([2.94, 2.92, 2.91, 2.89, 2.85, 2.79, 2.69, 2.52, 2.22, 1.82, 1.38, 0.96, 0.55, 0.15])
V_source = flip(linspace(0.2, 5.4, 14))
intensity = array([0.89, 0.88, 0.88, 0.88, 0.87, 0.85, 0.79, 0.33, 0.01, 0, 0, 0, 0, 0])

grid()
# xlabel("Voltage, V [volt]")
# ylabel("Current, I [mA]")
# plot(V_drop, I, "ro", label="data points")
# plot(V_drop, I)

xlabel("Supply Voltage, V [volt]")
ylabel("Intensity [counts]")
plot(I, intensity, "ro", label="data points")
plot(I, intensity)
legend()
# savefig("./graphs/cold_yellow_intensity.pdf")
