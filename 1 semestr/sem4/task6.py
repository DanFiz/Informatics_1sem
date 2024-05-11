import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('BTC_data.csv')
time=list(df['time'])
price=list(df['close'])
data=[]
for i in time:
    data.append(i[:10])
days=[]
k=0
l=0
for i in data:
    data0= list(map(int,(i.split('-'))))
    days.append(data0[0]*365.25+data0[1]*29.3+data0[2])
y=price
x=days
fig=plt.figure(figsize=(16,9))
ax=fig.add_subplot(111)
d=[i for i in range(len(time))]
n=int(input())
z=np.polyfit(d,y,deg=n)
P=np.poly1d(z)
tickp=[]
ax.plot(d,P,'r')
ax.plot(data, y,'k')
for i in range(len(time)):
    if i%92==0:
        tickp.append(i)
plt.xlabel('Data')
plt.ylabel('Price')
plt.title('Исторический график зависимости цены биткоина от времени')
ax.set_xticks([tickp[i] for i in range(len(tickp))])
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.show()