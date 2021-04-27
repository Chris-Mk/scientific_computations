from numpy import *
from matplotlib.pyplot import *
import pandas as pd

data1 = pd.read_csv("./files/measurement1.txt", "\t", header=0, names=["time", "temp"])
data2 = pd.read_csv("./files/measurement2.txt", "\t", header=0, names=["time", "temp"])
data3 = pd.read_csv("./files/measurement3.txt", "\t", header=0, names=["time", "temp"])

grid()
xlabel("Time, (s)")
ylabel("Temperature, ($\degree$C)")
title("Graph of temperature vs time.")

# plot(data1["time"], data1["temp"])
# plot(data2["time"], data2["temp"])
plot(data3["time"], data3["temp"])
# savefig("./graphs/heat3.pdf")

