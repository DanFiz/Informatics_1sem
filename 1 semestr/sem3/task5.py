import numpy as np
N=int(input())
M=int(input())
B=[]
for i in range(N):
    A=[ 0 for j in range(M)]
    B.append(A)
C=np.array(B)
i=0
j=0
k=1
while k!=N*M:
        while j <= M - 1 or C[i, j] != 0:
            C[i, j] = k
            j += 1
            k+=1
            if j > M - 1: break
        j -= 1
        while i <= N - 1 or C[i, j] != 0:
            C[i, j] = k
            i += 1
            k += 1
            if i > N - 1: break
        i -= 1
        while j >= 0 or C[i, j] != 0:
            C[i, j] = k
            j -= 1
            k += 1
            if j < 0: break
        j += 1
        while i >= 0 or C[i, j] != 0:
            C[i, j] = k
            i -= 1
            k += 1
            if i < 0: break
        i += 1
print(C)