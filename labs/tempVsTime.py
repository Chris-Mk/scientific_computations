from numpy import *
from matplotlib.pyplot import *

temp1 = linspace(90, 50, 9)
time1 = array([0, 51, 119, 196, 294, 410, 554, 725, 955])

temp2 = linspace(85, 50, 8)
time2 = array([0, 50, 102, 166, 247, 345, 462, 620])

grid()
xlabel("Time [s]")
ylabel("Temperature [$\degree$C]")
title("Graph of temperature vs time.")

plot(time1, temp1, label="2dl of water")
plot(time2, temp2, label="1dl of water")
legend()
