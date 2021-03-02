from numpy import *
from matplotlib.pyplot import *

d = linspace(0, 80, 17) / 1000
b = abs(array([-1.2038, -0.6674, -0.2178, -0.0974, -0.0506, -0.0292, -0.0178, -0.0114, -0.0060,
               -0.0044, -0.0026, -0.0010, 0.0000, 0.0010, 0.0018, 0.0026, 0.0030])) / 10000

xlabel("distance, d(m)")
ylabel("magnetic field, B(T)")
title("Graph of magnetic field,B vs distance,d.")
ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
grid()
plot(d, b, "o", label="data")
plot(d, b)
legend()
savefig("./graphs/B_vs_d.pdf")

