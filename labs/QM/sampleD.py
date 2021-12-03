from scipy.stats import linregress
from matplotlib.pyplot import *
import pandas as pd
from numpy import *

data = pd.read_csv("./files/Sample_D.txt", "\t", header=None)
T = 2 * sqrt((2 * 0.067 * 9.1e-31) / 1.055e-34 ** 2) * sqrt(200e-3 * 1.6e-19 - (0.3 * 1.6e-19 * data[0]) / 2)
I = log(data[1])
slope, inter, *a = linregress(T, I)
print("Width, a =", abs(slope))

grid()
# title("Graph of Current Vs Tunnelling probability")
xlabel("X [1/m]")
ylabel("Logarithmic Current ln(I)")
plot(T, I, "r.", label="Sample points (D)")
plot(T, slope * T + inter, label=f"Fit (y={slope:.3e}x+{round(inter, 4)})")
legend()

# savefig("./graphs/sample-d.pdf")
