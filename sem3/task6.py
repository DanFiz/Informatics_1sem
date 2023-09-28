import numpy as np
n=int(input())
x=[int(input()) for i in range(n)]
y=[int(input()) for i in range(n)]
def mnk(x,y):
    A = np.vstack([x, np.ones(len(x))]).T
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return k,b
B=mnk(x,y)
k=B[0]
b=B[1]
print(f'y={k}x+{b}')