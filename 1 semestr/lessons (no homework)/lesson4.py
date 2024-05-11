import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) # допустим, больше 1 графика нам не надо

values = np.random.normal(pos, scale, size)

# строим гистограмму с 100 блоков
plt.hist(values, 100)

plt.show()