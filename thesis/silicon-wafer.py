from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

t = array([374.75, 374.61, 375.93, 378.46, 381.96, 386.30, 391.19, 396.19, 401.01])
d = array([0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2])
m, y_inter, *a = linregress(d, t)

grid()
print(m, "nm/cm")
xlabel("distance [cm]")
ylabel("SiO$_2$ thickness [nm]")
plot(d, t, "ro")
plot(d, t)
# plot(d, m * d + y_inter)
