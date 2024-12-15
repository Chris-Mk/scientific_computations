import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./masters/quantum devices/files/coulomb blockade/group4_log6.txt', sep='\t',
                   usecols=[i for i in range(2, 603)], skiprows=[1])

plt.imshow(data, cmap='bwr', extent=[-0.35, -0.05, -5, 5])
plt.gca().set_aspect('auto', adjustable='box')
plt.xlabel('$V_g$ [V]')
plt.ylabel('$V_{sd}$ [mV]')
plt.colorbar(orientation='vertical')
plt.show(block=True)
# plt.savefig('./masters/graphs/stability.pdf')
