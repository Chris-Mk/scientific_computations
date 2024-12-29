import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

filepath = './masters/spectroscopy/files/ABS/100avg140cm.txt'

# Importing the data
Abs = np.loadtxt(filepath, delimiter='\t', skiprows=26)
Abs_data = Abs[:, 0]

# Creating the x-axis samples
x = np.arange(1500, 8001)

# Performing the fit and correcting the data (essentially taking away the slope)
exclude1 = np.logical_and(x > 2500, x < 6600)
exclude2 = x < 1500
exclude3 = x > 6800
exclude = exclude1 | exclude2 | exclude3


# Define a polynomial function for fitting
def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c


# Fit the data
popt, _ = curve_fit(poly2, x[~exclude], Abs_data[x[~exclude]])

# Correct the data
Abs_corr = Abs_data[x] / poly2(x, *popt)

# Plotting the results
plt.figure(1)
plt.plot(Abs_data[x], linewidth=2)
plt.plot(poly2(x, *popt), 'r', linewidth=2)
plt.show(block=True)

# Plotting the corrected data
plt.figure(3)
plt.plot(Abs_corr)
plt.show(block=True)

y = np.min(Abs_corr)
imin = np.argmin(Abs_corr) + 9

# plt.axhline(y=1, linewidth=2, color=[.8, .8, .8])
# plt.axhline(y=np.mean(Abs_corr[(imin - 10):(imin + 10)]), linewidth=2, color=[.8, .8, .8])
# plt.show(block=True)

# Display the mean value
print(np.mean(Abs_corr[(imin - 10):(imin + 10)]))
