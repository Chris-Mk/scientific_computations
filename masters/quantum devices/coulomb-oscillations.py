import pandas as pd
from matplotlib.pyplot import *
import scipy.stats as sp

data = pd.read_csv('./masters/quantum devices/files/coulomb blockade/group4_log5.txt', '\t', header=1,
                   names=['Time(s):', 'Sweep V(V):', 'Ch1 I(A) 0.0181K'])
slope1, y_inter1, *a1 = sp.linregress(data['Sweep V(V):'][93:121], data['Ch1 I(A) 0.0181K'][93:121])
slope2, y_inter2, *a2 = sp.linregress(data['Sweep V(V):'][138:371], data['Ch1 I(A) 0.0181K'][138:371])
slope3, y_inter3, *a3 = sp.linregress(data['Sweep V(V):'][380:396], data['Ch1 I(A) 0.0181K'][380:396])
print(1 / slope1)
print(1 / slope2)
print(1 / slope3)

grid()
xlabel('$V_{sd}$ [mV]')
ylabel('$I_{sd}$ [pA]')
plot(data['Sweep V(V):'][85:400] / 1e-3, data['Ch1 I(A) 0.0181K'][85:400] / 1e-11)
# plot(data['Sweep V(V):'][93:121] / 1e-3, slope1 * data['Sweep V(V):'][93:121] / 1e-3 + y_inter1)
# plot(data['Sweep V(V):'][138:371] / 1e-3, slope2 * data['Sweep V(V):'][138:371] / 1e-3 + y_inter2)
# plot(data['Sweep V(V):'][380:396] / 1e-3, slope3 * data['Sweep V(V):'][380:396] / 1e-3 + y_inter3)
# plot(data['Sweep V(V):'], data['Ch1 I(A) 0.0181K'] / 1e-11)
# savefig('./masters/graphs/IV2.pdf')
