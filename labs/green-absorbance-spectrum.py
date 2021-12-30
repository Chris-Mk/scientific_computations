from matplotlib.pyplot import *
from numpy import *
import pandas as pd

data = pd.read_csv("./files/task1.2 green absorbance.csv", ";", header=0,
                   names=["Wavelength (nm)", "Absorbance Solution", "Transmittance Solution"])[400:800]

grid()
title("Graph of Absorbance vs Wavelength for green dots.")
xlabel("Wavelength [nm]")
ylabel("Absorbance")
# plot(data["Wavelength (nm)"], data["Transmittance Solution"])
plot(data["Wavelength (nm)"], data["Absorbance Solution"])
savefig("./graphs/absorbance-wavelength-green-dots.pdf")
