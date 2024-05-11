A=list(map(int,input().split()))
max=0
for i in range(len(A)):
    if A.count(A[i])>=max:
        max=A.count(A[i])
        x=A[i]
print(x)