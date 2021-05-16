from numpy import *
from matplotlib.pyplot import *

n = linspace(1, 6, 6)
E_cal = array([0.30, 1.18, 2.67, 4.81, 7.39, 9.62])
E_og = array([0.30, 1.19, 2.67, 4.69, 7.19, 9.81])

grid()
xlabel("number of bound states, n")
ylabel("Energy levels, E [eV]")
title("Graph of energy levels vs no. of bound states.")

plot(n, E_cal, "ro", n, E_cal, label="Calculated energies.")
plot(n, E_og, "go", n, E_og, label="Observed energies.")
legend()

savefig("./graphs/nVsEnergyCal.pdf")
