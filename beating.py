from matplotlib.pyplot import *
from numpy import *

t = linspace(0, 100, 1000)
# phi1 = 0.05 * (cos(3.13 * t) + cos(3.44 * t))
# phi2 = 0.05 * (cos(3.13 * t) - cos(3.44 * t))

phi1 = 0.05 * (cos(3.29 * t) + cos(0.16 * t))
phi2 = 0.05 * (cos(3.29 * t) - cos(0.16 * t))

grid()
xlabel("t")
ylabel("phi(t)")
plot(t, phi1)
plot(t, phi2)
# plot(t, phi1 + phi2)
