from matplotlib.pyplot import *
from numpy import *
from scipy.interpolate import interp2d

initial_thickness = loadtxt("./thesis/data/SiNx-wiped2.txt")
final_thickness = loadtxt("./thesis/data/SiNx-wipedAndmilled.txt")
x, y = initial_thickness[0:, 0], initial_thickness[0:, 1]
z1, z2 = initial_thickness[0:, 2], final_thickness[0:, 2]
z = (z1 - z2) / 2.67

f = interp2d(x, y, z, kind="linear")
x_coord = arange(min(x), max(x) + 1)
y_coord = arange(min(y), max(y) + 1)
# z_coord = (f(x_coord, y_coord) / max(z)) * 100
z_coord = f(x_coord, y_coord)

xlabel("x [cm]")
ylabel("y [cm]")
imshow(z_coord, extent=[min(x), max(x), min(y), max(y)], origin="lower")
cbar = colorbar()
cbar.set_label("Milling rate [nm/min]")
# savefig("./thesis/images/nitride.pdf")

