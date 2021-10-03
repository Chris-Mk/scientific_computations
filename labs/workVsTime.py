from numpy import *
from matplotlib.pyplot import *
import pandas as pd
import scipy.stats as sp

data = pd.read_csv("./files/Task_2.3.txt", "\t", header=0,
                   names=["Time", "Temperature_Hot", "Temperature_Cold", "Work"])
x, y = data["Time"], data["Work"]

slope, y_inter, *a = sp.linregress(x, y)

grid()
xlabel("Time [s]")
ylabel("Work [J]")
title("Graph of work vs time")
ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

plot(x, y, "r.", label="data points")
plot(x, slope * x + y_inter, "b-", label="linear regression")
legend()

# savefig("./graphs/workVsTime.pdf")

print("Power input=", slope)
