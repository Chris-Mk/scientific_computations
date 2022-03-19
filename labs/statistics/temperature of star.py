from matplotlib.pyplot import *
from numpy import *
import pandas as pd
import scipy.constants as sp
from scipy.stats import linregress

data = pd.read_csv('./files/LineList.dat', '    ', header=0, names=['#lambda/Å', 'loggf', 'chi/eV'])
spectrum = pd.read_csv('./files/spectrum.dat', '\s', header=0, names=['# lambda/AA', 'F/Fc']).to_numpy()

wavelength = flip(array(spectrum[:, 0]))
flux = flip(array(spectrum[:, 1]))
const = log10(e) / (sp.k / sp.e)

grid()
# xlabel('wavelength [Å]')
# ylabel('flux')
# xlim(6392, 6402)
# plot(wavelength, flux)
# savefig('./graphs/iron_spectrum.pdf')

lhs = []
for i in range(len(data['#lambda/Å'])):
    lamb = data['#lambda/Å'][i]
    lower_index = searchsorted(wavelength, lamb - 0.3515)
    upper_index = searchsorted(wavelength, lamb + 0.3515)

    x = wavelength[lower_index: upper_index]
    fs = flux[lower_index: upper_index]

    width = trapz([1 - fs], x)[0]
    lhs.append(log10(width / lamb) - data['loggf'][i] - log10(lamb))

rhs = data['chi/eV']
slope, y_inter, *a = linregress(rhs, lhs)
print(slope)

xlabel('Constant K')
ylabel('$\chi$ [eV]')
plot(rhs, lhs, 'ro', label='Data points')
plot(rhs, slope * rhs + y_inter, label='Linear regression')
legend()
print('Temperature =', const / -slope)
# savefig('./graphs/stellar_temp.pdf')
