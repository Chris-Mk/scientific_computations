import pandas as pd
from matplotlib.pyplot import *

data = pd.read_csv("./files/Sample_A.txt", "\t", header=None)

grid()
title("Graph of Current Vs Voltage")
xlabel("Voltage [V]")
ylabel("Current [A]")
plot(data[0], data[1], "r.", label="Measured data")
legend()
