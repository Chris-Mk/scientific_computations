from matplotlib.pyplot import *
from numpy import *
import pandas as pd

data = pd.read_csv("./files/orange-dots-emission-spectrum.csv", ";", header=0,
                   names=["Wavelength (nm)", "Intensity Source"])[500:900]

grid()
title("Graph of Intensity vs Wavelength for orange dots.")
xlabel("Wavelength [nm]")
ylabel("Intensity")
plot(data["Wavelength (nm)"], data["Intensity Source"])
savefig("./graphs/intensity-wavelength-orange-dots.pdf")
