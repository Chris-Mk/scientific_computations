from matplotlib.pyplot import *
from numpy import *

Z = 1
r = linspace(0, 20, 1000)

for l in range(4):
    v = (-Z / r) + ((l ** 2 + l) / (2 * r ** 2))
    plot(r, v, label=f'l={l}')

grid()
xlabel('r')
ylabel('V')
ylim(-0.5, 0.4)
legend()
# savefig("./graphs/effective_potential.pdf")
