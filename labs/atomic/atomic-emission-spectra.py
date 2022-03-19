import pandas as pd
from matplotlib.pyplot import *

data = pd.read_csv('./files/hydrogen spectrum.txt', ';', header=0,
                   names=["Wave", "Sample", "Dark", "Reference"])

# xlim(430, 630)  #sodium saturated
# xlim(338, 362)  #cadmium
# print(data["Wave"])
# print(data["Sample"])
# title('Hydrogen')
# xlabel('Wavelength')
# ylabel('Counts')
# plot(data["Wave"], data["Sample"])
