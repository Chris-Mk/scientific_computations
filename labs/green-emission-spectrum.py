from matplotlib.pyplot import *
from numpy import *
import pandas as pd

data = pd.read_csv("./files/green-dots-emission-spectrum.csv", ";", header=0,
                   names=["Wavelength (nm)", "Intensity Source"])[300:800]

grid()
title("Graph of Intensity vs Wavelength for green dots.")
xlabel("Wavelength [nm]")
ylabel("Intensity")
plot(data["Wavelength (nm)"], data["Intensity Source"])

savefig("./graphs/intensity-wavelength-green-dots.pdf")
