from matplotlib.pyplot import *
from numpy import *

data1 = loadtxt("./thesis/data/pmma-no-milling.txt")
data2 = loadtxt("./thesis/data/pmma-plasma-only.txt")
data3 = loadtxt("./thesis/data/pmma-1min-milling.txt")

x, y1, y2, y3 = data1[0:, 0], data1[0:, 1], data2[0:, 1], data3[0:, 1]
y_plasma = (y1 - y2) / 5  # Plasma only for 5 minutes
y_milling = y1 - y3  # Thickness difference after 1 min of milling/etching

# subplot(1, 2, 1)
grid()
xlabel("X [cm]")
ylabel("Milling rate [nm/min]")
plot(x, y_plasma, "ro")
plot(x, y_plasma, label="Photon milling")
legend()

# subplot(1, 2, 2)
# grid()
# xlabel("X [cm]")
# ylabel("Milling rate [nm/min]")
# plot(x, y_milling, "ro")
# plot(x, y_milling, label="Argon Milling")
# legend()

# savefig("./thesis/images/pmma-double-fig.pdf")
