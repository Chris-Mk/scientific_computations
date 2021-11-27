from matplotlib.pyplot import *
import pandas as pd

data = pd.read_csv("./files/antenna.csv", sep="\\s", header=0,
                   names=["Frequency", "Magnitude"])

freq, power = data["Frequency"], data["Magnitude"]

grid()
xlabel("Frequency [Hz]")
ylabel("Power Loss [dBm]")
title("Graph of Power Loss vs Frequency")
plot(freq, power, label="Measured data")
legend()
