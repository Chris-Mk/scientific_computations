from matplotlib.pyplot import *
from numpy import *

H = linspace(-0.3, 0.3, 13)
m_up = array([0.9845, 0.9859, 0.9867, 0.9878, 0.9885, 0.9892, 0.9897, 0.9902, 0.9907, 0.9910, 0.9914, 0.9916, 0.9919])
m_down = array([0.9919, 0.9821, 0.9849, 0.9862, 0.9868, 0.9870, 0.9870, 0.9869, 0.9863, 0.9855, 0.9846, 0.9832, 0.9760]) * -1

f, (ax, ax2) = subplots(2, 1, sharex=True)
ax.plot(H, m_up)
ax2.plot(H, m_down)

ax.set_ylim(.9800, .9999)
ax2.set_ylim(-0.9999, -0.9700)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

d = .010  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# plot(H, m_up)
# plot(H, m_down)
# ylim(-0.96, 0.90)
show(block=True)
