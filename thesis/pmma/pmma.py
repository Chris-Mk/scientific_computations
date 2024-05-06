from matplotlib.pyplot import *
from numpy import *

data = loadtxt("./thesis/data/0min-thickness.txt")
# data0 = loadtxt("./thesis/data/4min-thickness.txt")
data1 = loadtxt("./thesis/data/1min-thickness.txt")
x, y0, y1 = data[0:, 0], data[0:, 1], data1[0:, 1]
y = y0 - y1

# subplot(121)
# grid()
# xlabel("X [cm]")
# ylabel("Thickness [nm]")
# plot(x, data[0:, 1], "ro", label="Data points")
# plot(x, data[0:, 1], label="Before milling")
# plot(x, y1, "ro")
# plot(x, y1, label="1 min milling")
# errorbar(x, y1, yerr=5, ls="none", label="error bar")
# errorbar(x, data[0:, 1], yerr=5, ls="none")
# tight_layout(pad=2)
# legend()

# subplot(122)
grid()
xlabel("X [cm]")
ylabel("Milling rate [nm/min]")
plot(x, y, "ro", label="Data points")
plot(x, y, label="Milling rate")
# plot(arange(-1.4, -1.4), range(72, 80))
errorbar(x, y, yerr=5, ls="none", label="error bar")
legend()
# savefig("./thesis/images/4min-pmma-milling.pdf")
