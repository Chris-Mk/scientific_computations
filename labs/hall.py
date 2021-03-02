from numpy import *
from matplotlib.pyplot import *

d = linspace(0, 80, 17)
v = array([5.2895, 3.9485, 2.8245, 2.5235, 2.4065, 2.3530, 2.3245, 2.3085, 2.2950,
           2.2910, 2.2865, 2.2825, 2.2800, 2.2775, 2.2755, 2.2735, 2.2725])

xlabel("distance, d(mm)")
ylabel("voltage, V(Volts)")
title("Graph of voltage, V vs distance, d")
grid()
plot(d, v, "r*", d, v)
