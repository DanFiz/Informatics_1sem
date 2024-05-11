A=list(map(int,input().split()))
S=1
for i in range(len(A)):
    S=S*A[i]
print(S**0.5)
