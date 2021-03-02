from numpy import *
from matplotlib.pyplot import *

d = linspace(0, 80, 17)
v = array([0.0180, 0.9080, 1.7770, 2.0460, 2.1480, 2.1940, 2.2190, 2.2330, 2.2410,
           2.2460, 2.2490, 2.2510, 2.2530, 2.2540, 2.2550, 2.2560, 2.2570])

xlabel("distance, d(mm)")
ylabel("voltage, V(Volts)")
title("graph of voltage, V vs distance, d")
grid()
plot(d, v, "g^", d, v)
