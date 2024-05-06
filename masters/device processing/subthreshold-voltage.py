from matplotlib.pyplot import *
from numpy import *
import pandas as pd
import scipy.stats as sp

data_dark = pd.read_excel('./masters/device processing/files/Transfer_dark.xls')
gateV_dark = data_dark['GateV'][134: 141]
slope, y_inter, *a = sp.linregress(gateV_dark, log10(abs(data_dark['DrainI'][134: 141])))
print("Inverse subthreshold slope in dark = ", 1 / slope)

subplot(121)
grid()
title('Subthreshold Properties in Dark')
ylabel('log(|I$_d$|) [A]')
xlabel('V$_g$ [V]')
plot(data_dark['GateV'][90:], log10(abs(data_dark['DrainI'][90:])))
plot(gateV_dark, slope * gateV_dark + y_inter, 'r--', label='subthreshold slope')
legend()

data_light = pd.read_excel('./masters/device processing/files/Transfer_light.xls')
gateV_light = data_light['GateV'][90: 94]
slope2, y_inter2, *a2 = sp.linregress(gateV_light, log10(abs(data_light['DrainI'][90: 94])))
print("Inverse subthreshold slope in light = ", 1 / slope2)

subplot(122)
grid()
title('Subthreshold Properties in Light')
# ylabel('log(|I$_d$|) [A]')
xlabel('V$_g$ [V]')
plot(data_light['GateV'][90:], log10(abs(data_light['DrainI'][90:])))
plot(gateV_light, slope2 * gateV_light + y_inter2, 'r--', label='subthreshold slope')
legend()
