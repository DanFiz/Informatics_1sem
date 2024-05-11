A=list(map(int,input().split()))
for i in range(len(A)//2):
    A[i*2],A[i*2+1]=A[i*2+1],A[i*2]
print(' '.join(list(map(str,A))))