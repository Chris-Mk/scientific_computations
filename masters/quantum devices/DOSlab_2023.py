# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:12:00 2023

@author: ftf-abk
"""

import numpy as np
from itertools import product
import matplotlib.pyplot as plt

"""Running this code will generate the Eigen-energies for a system, whose
    dimensions you control with the variables below as you work through the lab.
    
    Read through the lab material (and this code), modify the variables in the code and then
    run the code for each lab task.
    
    You can use the 'Variable explorer' to view the variables entered and calculated,
    e.g. the combinations in the N-matrix or the Eigen energies in the E-matrix. 
    
    Hint: if small enough, you can also type "print(N)" in the console to 
    display the values (this works well for lab task 1).
"""


def perm(v1, v2, v3):
    # Generate all possible combinations of values from v1, v2, and v3
    combinations = list(product(v1, v2, v3))

    # Create a matrix M with the generated combinations
    return np.array(combinations)


"""ENTER IN VALUES BELOW TO CHANGE THE MODEL FOR THE LAB"""
nx_max = 5
ny_max = 5
nz_max = 2

Lx = 100
Ly = 100
Lz = 100
"""#####################################################"""

# Build the arrays for nx, ny and nz from 1 to the max value in steps of 1.
nx = np.arange(1, nx_max + 1, 1)
ny = np.arange(1, ny_max + 1, 1)
nz = np.arange(1, nz_max + 1, 1)

# Clear no-longer-needed variables to keep things tidy
del nx_max, ny_max, nz_max

# Safety check if the dimensions are too large
if nz[-1] * ny[-1] * nx[-1] > 400 ** 3:
    # If too large, print an error and abort
    print('error: too large')
else:
    # Otherwise, calculate all combinations of nx, ny and nz
    N = perm(nx, ny, nz)
    # Calculate the energy values for each combination
    E = N[:, 0] ** 2 / Lx ** 2 + N[:, 1] ** 2 / Ly ** 2 + N[:, 2] ** 2 / Lz ** 2

"""Below is a function to plot the energy data:
    
    Once the code is run you can type "Hist_Plot()" into the terminal and run it.
        You will then be prompted to enter the number of bins.
    
    HINT: running "%matplotlib qt" in the terminal will generate plots in their own window,
    which you can then zoom in on, etc. Run "%matplotlib inline" to undo this.
"""


def Hist_Plot():
    # Prompt the user for the number of bins
    num_bins = int(input("Enter the number of bins: "))

    # Compute the histogram
    hist_values, bin_edges = np.histogram(E, bins=num_bins)

    # Plot the histogram
    plt.hist(E, bins=bin_edges, edgecolor='blue', align='mid')
    plt.title("Histogram of Data")
    plt.xlabel("Energy ($\\frac{2m}{\\hbar^2 \\pi^2}$) [eV]")
    plt.ylabel("Frequency")
    plt.show()


Hist_Plot()
