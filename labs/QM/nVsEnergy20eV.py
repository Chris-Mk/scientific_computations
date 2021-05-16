from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 15, 15)
E = array([-4.91, -4.66, -4.23, -3.62, -2.85, -1.91, -0.80,
           0.49, 1.93, 3.54, 5.32, 7.24, 9.32, 11.52, 13.79])
E_idw = array([-4.91, -4.62, -4.15, -3.50, -2.65, -1.62, -0.39,
               1.02, 2.61, 4.40, 6.37, 8.54, 10.89, 13.42, 16.15])

grid()
xlabel("number of bound states, n")
ylabel("Energy levels, E [eV]")
title("Graph of energy levels vs no. of bound states.")

plot(n, E, "ro",  n, E, label="Finite well, 20eV")
plot(n, E_idw, "go", n, E_idw, label="IDW")
legend()

savefig("./graphs/nVsEnergy20eV.pdf")
