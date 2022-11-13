from matplotlib.pyplot import *
from numpy import *

data1 = loadtxt("./labs/ssp/XRD/unknown_0004.dat")
x1, y1 = data1[230:, 0], data1[230:, 1]
xlabel("2$\\theta$ [deg]")
ylabel("Intensity [$Wm^{-2}$]")
# text(20.7, 15.2, "(110)")
# text(28, 74, "artifact")
# text(29.2, 6.7, "(200)")
# text(35.8, 7.4, "(211)")
# plot(x1, y1)

data2 = loadtxt("./labs/ssp/XRD/unknown_0006.dat")
x2, y2 = data2[200:, 0], data2[200:, 1]
text(18, 42.8, "(111)")
text(20.7, 18.1, "(200)")
text(27.8, 59.4, "artifact")
text(29.25, 12.5, "(220)")
text(34.14, 13.2, "(311)")
text(35.78, 6.1, "(222)")
plot(x2, y2)
# savefig("./graphs/XRD/sample2.pdf")

