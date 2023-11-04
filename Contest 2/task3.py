b=1
A=[]
with open('input.txt') as f:
    while b!=0:
        b=int(f.readline())
        if b!=0:
            A.append(b)
for i in range(len(A)):
    n=A[i]
    if n<3:
        print(0)
    else:
        N=int((n-2)*(n-1)/2)
        print(N)