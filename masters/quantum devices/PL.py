import pandas as pd
from matplotlib.pyplot import *
from numpy import linspace

# data = pd.read_csv('./masters/quantum devices/files/PLE lab/1. 532nmexSampleA.txt.txt', '\t', skiprows=13, header=None) #532nm sample A
# data = pd.read_csv('./masters/quantum devices/files/PLE lab/2. 532nmexSampleAmerge.txt.txt', '\t', skiprows=13, header=None) #532nm sample A merged

# data = pd.read_csv('./masters/quantum devices/files/PLE lab/3. 532nmexSampleBmerge.txt.txt', '\t', skiprows=19,header=None)  # 532nm sample B merged
# data = pd.read_csv('./masters/quantum devices/files/PLE lab/4. 720nmexSapmleB.txt.txt', '\t', skiprows=19, header=None) #720nm sample B

# data = pd.read_csv('./masters/quantum devices/files/PLE lab/5. PLESampleB.txt.txt', '\t', header=None)  # PLE sample B
data = pd.read_csv('./masters/quantum devices/files/PLE lab/6. RamanSampleB.txt.txt', '\t', skiprows=19, header=None) #Raman sample B

xlabel("frequency [cm$^{-1}$]")
ylabel("Intensity [counts]")
# ticklabel_format(axis='y', scilimits=[-3, 3])
plot(data[0], data[1])
# plot([1.57364 for i in range(100)], linspace(150, 480, 100), 'r-')  # lh
# plot([1.55669 for j in range(100)], linspace(150, 480, 100), 'g-')  # hh
# plot([1.7289 for k in range(100)], linspace(150, 550, 100), 'r-', label='lh')  # lh
# plot([1.66525 for l in range(100)], linspace(150, 480, 100), 'g-', label='hh')  # hh
# text(1.692, 10, 'artifact')
# plot([1.82819 for i in range(100)], linspace(150, 480, 100), label='hh') #hh
# legend()

# text(1.57364, 9700, "lh")
# text(1.55669, 1400, "hh")
# text(1.7289, 199800, "lh")
# text(1.66525, 1750, "hh")
# text(1.82819, 1750, "hh")

# plot(pd.concat([data[0], data[2][450:]]), pd.concat([data[1], data[3][450:]]))
# savefig('./masters/graphs/PLE-graph.pdf')
