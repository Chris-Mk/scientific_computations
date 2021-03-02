from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

x = linspace(5, 75, 8) / 1000
I = array([0.240, 0.415, 0.600, 0.780, 0.965, 1.150, 1.330, 1.500])

slope, y_intercept, r, p, s = sp.linregress(I, x)
print("Slope is", slope)
print("Std error", s)

xlabel("current, I(A)")
ylabel("distance, x(m)")
title("Graph of distance,x vs current,I")
grid()

plot(I, x, "ro", label="data")
plot(I, slope * I + y_intercept, label="linear regression")
legend()
# savefig("./graphs/d_vs_I.pdf")
