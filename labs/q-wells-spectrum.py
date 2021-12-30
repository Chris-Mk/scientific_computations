from matplotlib.pyplot import *
import pandas as pd

data = pd.read_csv("./files/task2_1.csv", ";", header=0,
                   names=["Wavelength (nm)", "Intensity Source"])
# [400:800]

grid()
title("Graph of Intensity vs Wavelength for quantum wells.")
xlabel("Wavelength [nm]")
ylabel("Intensity")
plot(data["Wavelength (nm)"], data["Intensity Source"])
savefig("./graphs/q-wells-spectrum.pdf")
