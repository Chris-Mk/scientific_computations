from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 10, 10)
E = array([-1.81, 0.91, 3.14, 5.10, 6.90, 8.57, 10.14, 11.63, 13.05, 14.38])

grid()
xlabel("number of bound states, n")
ylabel("Energy levels, E [eV]")
title("Graph of energy levels vs no. of bound states.")

plot(n, E, "ro", label="data points")
plot(n, E, label="Finite well, 20eV")
legend()

savefig("./graphs/nVsEnergy20eVAsy.pdf")
