from scipy.optimize import curve_fit
from matplotlib.pyplot import *
import pandas as pd
from numpy import *


def lor(f, R, L, C):
    return 1 / (sqrt(1 + (1 / (R ** 2)) * ((1 / (f * C)) - (L * f)) ** 2))


data = pd.read_csv("./files/LRC tracking generator.csv", sep="\\s", header=0,
                   names=["Frequency", "Magnitude"])[: 400]

freq, power = data["Frequency"], 10 ** (data["Magnitude"] / 10)
power = power / max(power)
popt, pcov = curve_fit(lor, freq, power, p0=[6, 1e-7, 2.91e-12])
print(popt)

grid()
xlabel("Frequency [Hz]")
ylabel("Power [W]")
title("Graph of Power Loss vs Frequency")
plot(freq, power, label="Data fit")
plot(freq, lor(freq, popt[0], popt[1], popt[2]), label="Lorentian curve")
legend()

# savefig("./graphs/lorentian-fit.pdf")

