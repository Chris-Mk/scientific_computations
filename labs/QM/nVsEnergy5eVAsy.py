from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 5, 5)
E = array([-3.78, -2.71, -1.83, -1.06, -0.38])

grid()
xlabel("number of bound states, n")
ylabel("Energy levels, E [eV]")
title("Graph of energy levels vs no. of bound states.")

plot(n, E, "ro", label="data points")
plot(n, E, label="Finite well, 5eV")
legend()

savefig("./graphs/nVsEnergy5eVAsy.pdf")
