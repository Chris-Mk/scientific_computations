from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 8, 8)
E = array([-4.92, -4.68, -4.29, -3.74, -3.04, -2.20, -1.24, -0.23])
E_idw = array([-4.91, -4.62, -4.15, -3.50, -2.65, -1.62, -0.39, 1.02])

grid()
xlabel("number of bound states, n")
ylabel("Energy levels, E [eV]")
title("Graph of energy levels vs no. of bound states.")

plot(n, E, "ro", n, E, label="Finite well, 5eV")
plot(n, E_idw, "go", n, E_idw, label="IDW")
legend()

savefig("./graphs/nVsEnergy5eV.pdf")
