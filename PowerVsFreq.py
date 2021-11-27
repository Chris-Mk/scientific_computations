from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

f = linspace(1.5, 3, 4)
p = [-11.77, -9.48, -7.62, -2.27]
slope, y_inter, *a = linregress(f, p)

grid()
title("Graph of Power Loss Vs Frequency")
xlabel("Frequency [GHz]")
ylabel("Power Loss [dBm]")
plot(f, p, "ro", label="Measured data")
plot(f, slope * f + y_inter, label="Linear regression")
legend()

# savefig("./graphs/powerVsFreq.pdf")
