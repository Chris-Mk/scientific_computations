from numpy import *
from matplotlib.pyplot import *
import pandas as pd
import scipy.stats as sp

data = pd.read_csv("./files/Task_2.3.txt", "\t", header=0,
                   names=["Time", "Temperature_Hot", "Temperature_Cold", "Work"])

grid()
ylabel("Temperature [$\degree$C]")
xlabel("Time [s]")
title("Graph of temperature vs time.")

t_start, t_end = data["Time"][:40],  data["Time"][-40:]
T_start, T_end = data["Temperature_Hot"][:40], data["Temperature_Hot"][-40:]

slope_start, y_inter_start, *a = sp.linregress(t_start, T_start)
slope_end, y_inter_end, *b = sp.linregress(t_end, T_end)

plot(data["Time"], data["Temperature_Hot"], label="Hot Reservoir")
plot(data["Time"], data["Temperature_Cold"], label="Cold Reservoir")
plot(t_start, slope_start * t_start + y_inter_start, label="Start slope")
plot(t_end, slope_end * t_end + y_inter_end, label="End slope")
legend()

# savefig("./graphs/timeVsTemperature.pdf")

print(slope_start * 1000 * 0.01 * 4190)
print(slope_end * 1000 * 0.01 * 4190)
