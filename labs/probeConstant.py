from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

K_h = array([82605.04, 83519.08, 82281.88, 82095.81])
I = array([2, 2.2, 2.5, 2.8])
U_h = array([0.983, 1.081, 1.226, 1.371])
B = array([2.38, 2.62, 2.98, 3.34]) / 1000

x = (U_h / B)
slope, *a = sp.linregress(U_h, B)

print(slope)
plot(x, K_h)

