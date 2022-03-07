from matplotlib.pyplot import *
from numpy import *
import scipy.stats as sp

N = array([20, 40, 80, 160])
r_sq = array([66.7, 193, 549, 1555])

slope, y_intercept, *a = sp.linregress(log(N), log(r_sq))  # finds the slope and y-intercept from the given data
print(slope / 2)

xscale('log')
yscale('log')
xlabel('N')
ylabel('$r_{ee}^2$')
plot(N, r_sq, label='Ordinary Random Walk')
plot(N ** (slope / 2), r_sq, label='Self-avoiding Walk')
legend()
# savefig('./graphs/random_walks.pdf')
