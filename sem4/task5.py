import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('iris_data.csv')
time=list(df['time'])
price=list(df['close'])
fig=plt.figure(figsize=(16,9))
ax=fig.add_subplot(111)
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02,fontsize='medium')
x=matplotlib.dates.date2num(date)
y=price

for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
    plt.plot(x, y)
plt.show()