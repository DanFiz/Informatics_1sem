import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv('iris_data.csv')
A=list(df['Species'])
x=A.count('Iris-setosa')
y=A.count('Iris-versicolor')
z=len(A)-x-y
ln=len(A)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('The share of iris species in the dataset')
ax1.pie([x/ln, y/ln, z/ln], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
B=list(df['PetalLengthCm'])
a=0
b=0
c=0
for i in range(ln):
    if B[i]<1.2:
        a+=1
    elif B[i]>1.5:
        c+=1
b=ln-a-c
ax2.set_title('The proportion of irises along the length of the petal')
ax2.pie([a/ln, b/ln, c/ln], labels = ['<1.2','1,2<= <=1.5','>1.5'])
plt.show()