import numpy as np
N = int(input())
sqr = np.sqrt(N)
dividers = []
i = 2
n=N
while i < (int(sqr)+1):
    if N % i == 0:
        N = N // i
        dividers.append(i)
    if N % (n-i) == 0:
        dividers.append(n-i)
        N = N // (n-i)
    if (N % i != 0) and (N % (n-i) != 0):
        i+=1
print(dividers)

