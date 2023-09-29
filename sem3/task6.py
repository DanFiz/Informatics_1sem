import numpy as np
ln=int(input())
k=1
x1=[]
y1=[]
while k<=ln:
    x1.append(float(input()))
    y1.append(float(input()))
    k+=1
x=np.array(x1)
y=np.array(y1)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = (x - x_mean)*y
denominator = (x - x_mean)**2
k = np.sum(numerator)/np.sum(denominator)
b = y_mean - k*x_mean
twonum=(y-k*x-b)**2
srkv=np.sum(twonum)
error=np.sqrt(srkv/len(x))
print(f'(y = {k}*x + {b})+-{error}')