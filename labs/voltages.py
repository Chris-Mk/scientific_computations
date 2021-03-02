from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

v_in = linspace(1, 15, 6, dtype=int)
v_out = linspace(1, 15, 6, dtype=int)
slope, y_intercept, *a = sp.linregress(v_in, v_out)

grid()
xlabel("Input voltage[V]")
ylabel("Measured output voltage[V]")
title("Graph of output voltage vs input voltage")

plot(v_in, v_out, "ro", label="measured data")
plot(v_in, v_in* slope + y_intercept, label="linear regression")
legend()
savefig("./files/voltages.pdf")

