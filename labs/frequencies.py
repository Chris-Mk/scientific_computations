from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

f_in = array([40, 1200, 4500, 15000])
f_out = array([40, 1204, 4347, 14285])
slope, y_intercept, *a = sp.linregress(f_in, f_out)

grid()
xlabel("Input frequency[Hz]")
ylabel("Measured output frequency[Hz]")
title("Graph of output frequency vs input frequency")

plot(f_in, f_out, "ro", label="measured data")
plot(f_in, f_in * slope + y_intercept, label="linear regression")
legend()
savefig("./files/frequencies.pdf")

