import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv('iris_data.csv')
SL=np.array(list((df['SepalLengthCm'])))
SW=np.array(list((df['SepalWidthCm'])))
PL=np.array(list(df['PetalLengthCm']))
PW=np.array(list(df['PetalWidthCm']))
n=len(SL)
fig, axs =plt.subplots(3,2,layout='constrained',figsize=(16,9))

ax1=axs[0,0]
ax1.scatter(SL, SW, marker='o')
ax1.set_ylabel('SepalWidthCm')
ax1.set_xlabel('SepalLengthCm')
k1, b1 = np.polyfit(SL, SW, deg=1)
xint1=SL
yint1=SL*k1+b1
ax1.plot(SL,yint1, 'r',label=f'k = {k1}; b = {b1}')
ax1.legend()
ax1.grid()

ax3 = axs[1, 0]
ax3.scatter(SL, PW, marker='o')
ax3.set_ylabel('PetalWidthCm')
ax3.set_xlabel('SepalLengthCm')
k3, b3 = np.polyfit(SL, PW, deg=1)
yint3=SL*k3+b3
ax3.plot(xint1,yint3, 'r',label=f'k = {k3}; b = {b3}')
ax3.legend()
ax3.grid()

ax2 = axs[0, 1]
ax2.scatter(SL, PL, marker='o')
ax2.set_ylabel('PetalLengthCm')
ax2.set_xlabel('SepalLengthCm')
k2, b2 = np.polyfit(SL, PL, deg=1)
yint2=SL*k2+b2
ax2.plot(xint1,yint2, 'r',label=f'k = {k2}; b = {b2}')
ax2.legend()
ax2.grid()

ax4 = axs[1, 1]
ax4.scatter(SW, PL, marker='o')
ax4.set_ylabel('PetalLengthCm')
ax4.set_xlabel('SepalWidthCm')
k4, b4 = np.polyfit(SW, PL, deg=1)
yint4=SW*k4+b4
xint4=SW
ax4.plot(SW,yint4, 'r',label=f'k = {k4}; b = {b4}')
ax4.legend()
ax4.grid()

ax5 = axs[2, 0]
ax5.scatter(SW, PW, marker='o')
ax5.set_ylabel('PetalWidthCm')
ax5.set_xlabel('SepalWidthCm')
k5, b5 = np.polyfit(SW, PW, deg=1)
yint5=SW*k5+b5
ax5.plot(xint4,yint5, 'r',label=f'k = {k5}; b = {b5}')
ax5.legend()
ax5.grid()

ax6 = axs[2, 1]
ax6.scatter(PL, PW, marker='o')
ax6.set_ylabel('PetalWidthCm')
ax6.set_xlabel('PetalLengthCm')
k6, b6 = np.polyfit(PL, PW, deg=1)
yint6=PL*k6+b6
ax6.plot(PL,yint6, 'r',label=f'k = {k6}; b = {b6}')
ax6.legend()
ax6.grid()

plt.show()



