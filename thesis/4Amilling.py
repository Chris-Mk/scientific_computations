from matplotlib.pyplot import *
from numpy import *
from scipy.interpolate import interp2d

data = loadtxt("./thesis/data/750kV_1min.txt")
x, y = data[0:, 0], data[0:, 1]
z = data[0:, 2]

f = interp2d(x, y, z, kind="linear")
x_coord = arange(min(x), max(x) + 1)
y_coord = arange(min(y), max(y) + 1)
z_coord = f(x_coord, y_coord)

xlabel("x [cm]")
ylabel("y [cm]")
imshow(z_coord, extent=[min(x), max(x), min(y), max(y)], origin="lower")
cbar = colorbar()
cbar.set_label("Thickness")
