from matplotlib.pyplot import *
from numpy import *
from scipy.stats import *

I = array([34.7, 30.2, 25.3, 20.9, 16.34, 11.67, 7.86, 2.82, 0.05, 0.002, 0.001, 0, 0, 0]) * 10 ** -3
V_drop = array([2.93, 2.91, 2.88, 2.85, 2.81, 2.77, 2.73, 2.65, 2.51, 1.99, 1.53, 1.02, 0.44, 0])
intensity = array([.91, .89, .82, .79, .67, .4, .2, .05, 0, 0, 0, 0, 0, 0])
V_source = flip(linspace(0, 6.5, 14))
# vdrop_slope, y_inter_vdrop, *a = linregress(V_drop[0:8], I[0:8])
# vdrop_slope2, y_inter_vdrop2, *a2 = linregress(V_drop[8:], I[8:])
# vsource_slope, y_inter_vsource, *b = linregress(V_source, intensity)
intensity_slope, y_inter_intensity, *c = linregress(I, intensity)

# grid()
# xlabel("Voltage, V [volt]")
# ylabel("Current, I [mA]")
# plot(V_drop, I, "ro", label="data points")
# plot(V_drop, I)

subplot(2, 1, 1)
grid()
xlabel("Supply Voltage, V [volt]")
ylabel("Intensity [counts]")
plot(V_source, intensity, "ro", label="data points")
plot(V_source, intensity)
legend()

subplot(2, 1, 2)
grid()
xlabel("Current, I [mA]")
ylabel("Intensity [counts]")
plot(I, intensity)
plot(I, intensity, "ro", label="data points")
plot(I, intensity_slope * I + y_inter_intensity, label="linear regression")
tight_layout()
legend()
savefig("./graphs/intensities.pdf")
