import numpy as np
import matplotlib.pyplot as plt
#Hello
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(16, 9),dpi=100)

ax1.set_title('Момент инерции от квадрата смещения')
y_measured0 = [1.6, 1.8, 2.9, 4.5, 6.3,9.5,13.1,16.8,21.4]
x_measured0= [0,1.44,2.88, 4.32,5.76,7.2,8.64,10.08,11.52]
n=len(y_measured0)
y_measured=[i*10 for i in y_measured0]
x_measured=[i**2 for i in x_measured0]
y_measured1=[i**2 for i in y_measured]
x_measured1=[i**2 for i in x_measured]
x=np.array(x_measured)
y=np.array(y_measured)
k, b = np.polyfit(x, y, deg=1)
twonum=(y-k*x-b)**2
srkv=np.sum(twonum)
error=np.sqrt(srkv/len(x))
T=np.array([77.0,78.0,82.0,88.0,94.3,104.0,114.2,124.0,135.0])
xerror=0.2*np.sqrt(x)
yerror=((0.019+1/T+0.0006/2.5094)*(y+80)+2.27)
#x1=(y[0]-b)/k
#x2=(y[len(y)-1]+yerror[len(y)-1]-b)/k
#xint = [x1, x2]
#yint = np.interp(xint, x_measured, y_measured)
ax1.scatter(x_measured, y_measured, marker='x')
y_est = k * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))
ax1.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax1.errorbar(x, y, yerr=yerror, xerr = xerror, color = 'k', linestyle = 'None')
ax1.plot(x,y_est, 'r',label=f'I = {round(k,1)}*$h^2$ + {round(b,1)} кг$*$$см^2$')
ax1.set_ylabel('I, кг$*$$cм^2$',rotation=0, horizontalalignment='right')
errork0=np.sqrt(((np.mean(y_measured1)-np.mean(y_measured)**2)/(np.mean(x_measured1)-np.mean(x_measured)**2)-k**2)/len(x_measured))
errorb0=errork0*np.sqrt(np.mean(x_measured1)-np.mean(x_measured)**2)
y_measured0t=([1.2,1.4,2.3,3.9,6.0,8.7,12.0,15.8,20.3])
y_measuredt=[i*10 for i in y_measured0t]
yt=np.array(y_measuredt)
kt, bt = np.polyfit(x, yt, deg=1)
y_esteor=kt*x+bt
ax1.plot(x,y_esteor)
ax1.grid()
ax1.legend()
ek1=(y[n-1]+yerror[n-1]-(y[0]-yerror[0]))/(x[n-1]-x[0])
ek2=(y[n-1]-yerror[n-1]-(y[0]+yerror[0]))/(x[n-1]-x[0])
ek=(abs(ek1-k)+abs(k-ek2))/np.sqrt(n)+errork0
print(f'M = {round(k,1)}+-{round(ek,1)} кг')
print(f'I = {round(b,1)}+-{round(errorb0,1)} кг*см^2')




l_measured = [38.1, 39.1, 43.3, 49.8, 57.2,69.6,83.9,98.9,117.3]
g_measured0= [0,1.44,2.88, 4.32,5.76,7.2,8.64,10.08,11.52]
g_measured=[i**2 for i in g_measured0]
l_measured1=[i**2 for i in l_measured]
g_measured1=[i**2 for i in g_measured]
g=np.array(g_measured)
l=np.array(l_measured)
g_mean = np.mean(g)
l_mean = np.mean(l)
k2, b2 = np.polyfit(g, l, deg=1)
twonum=(l-k2*g-b2)**2
srkv=np.sum(twonum)
error=np.sqrt(srkv/len(g))
gerror=0.2*np.sqrt(g)
lerror=(0.019+1/T)*l
#g1=(l[0]-b2)/k2
#g2=(l[len(l)-1]+lerror[len(l)-1]-b2)/k2
#gint = [g1, g2]
#lint = np.interp(gint, g_measured, l_measured)
ax2.scatter(g_measured, l_measured, marker='x')
l_est = k2 * g + b2
l_err = g.std() * np.sqrt(1/len(g) +
                          (g - g.mean())**2 / np.sum((g - g.mean())**2))
ax2.fill_between(g, l_est - l_err, l_est + l_err, alpha=0.2)
ax2.errorbar(g, l, yerr=lerror, xerr = gerror, color = 'k', linestyle = 'None')
ax2.plot(g,l_est, 'r',label=f'k*$T^2$ = {round(k2,3)}*$h^2$ + {round(b2,1)} $см^2$')
ax2.set_xlabel('$h^2$, $см^2$')
ax2.set_ylabel('k*$T^2$, $cм^2$',rotation=0, horizontalalignment='right')
errork02=np.sqrt(((np.mean(l_measured1)-np.mean(l_measured)**2)/(np.mean(g_measured1)-np.mean(g_measured)**2)-k2**2)/n)
errorb02=errork02*np.sqrt(np.mean(g_measured1)-np.mean(g_measured)**2)
ek1h=(l[n-1]+lerror[n-1]-(l[0]-lerror[0]))/(x[n-1]-x[0])
ek2h=(l[n-1]-lerror[n-1]-(l[0]+lerror[0]))/(x[n-1]-x[0])
ekh=(abs(ek1h-k2)+abs(k2-ek2h))/np.sqrt(n)+errork02

m0=1.0668
I0=80
M2=k2*m0/(1-k2)
eM2=M2*(0.0005/1.0668+2*ekh/k2)
I=b2*(M2+m0)-I0
eI=((eM2+0.0005)/(M2+m0)+errorb02/b2)*b2*(M2+m0)+2.27
print(f'M2 = {round(M2,2)}+-{round(eM2,2)} кг')
print(f'I2 = {round(I,0)}+-{round(eI,0)} кг*см^2')
ax2.grid()
ax2.legend()
#plt.savefig('I(h^2).png', dpi=500)
plt.show()