import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
plt.title('This is task 2 (striving for normality)!', fontdict={'fontname': 'sans-serif', 'fontsize': 18})
values1 = np.random.normal(0, 10, 10000)
values2 = np.random.normal(0, 10, 1000000)
values3 = np.random.normal(0, 10, 100000000)
ax1.hist(values1, 1000, )
ax1.set_title('The first graph')
'''ax1.xlabel('Scale')
ax1.ylabel('Size')'''
ax1.grid()
#(x, bins=None, range=None, density=False, weights=None, cumulative=False,
# bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None,
# log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)

ax2.hist(values2, 1000)
ax2.set_title('The second graph')
# ax2.xlabel('Scale')
# ax2.ylabel('Size')
ax2.grid()
ax3.hist(values3, 1000)
ax3.set_title('The third graph')
# ax3.xlabel('Scale')
# ax3.ylabel('Size')
ax3.grid()
plt.show()