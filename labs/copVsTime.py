from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp
import pandas as pd

data = pd.read_csv("./files/Task_2.3.txt", "\t", header=0,
                   names=["Time", "Temperature_Hot", "Temperature_Cold", "Work"])

start_index = 0
end_index = 12

cop_ideal = zeros(10)
cop = zeros(10)
t = zeros(10)

for i in range(10):
    time = array(data["Time"][start_index: end_index])
    temp_hot = array(data["Temperature_Hot"][start_index: end_index])
    temp_cold = array(data["Temperature_Cold"][start_index: end_index])

    slope, y_inter, *a = sp.linregress(time, temp_hot)
    cop[i] = (slope * 1000 * 0.01 * 4190) / 422.68
    t[i] = (time[0] + time[time.size - 1]) / 2

    cop_ideal[i] = temp_hot[temp_hot.size - 1] / (temp_hot[temp_hot.size - 1] - temp_cold[temp_cold.size - 1])

    start_index = end_index + 1
    end_index += 12

grid()
xlabel("time, [s]")
ylabel("COP")
title("Graph of COP of heat pump vs time.")

plot(t, cop, "ro", label="data points")
plot(t, cop)
plot(t, cop_ideal, "b*", t, cop_ideal)
legend()
