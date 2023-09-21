s=input().split()
G=int(s[0])
st=s[1]
L=len(st)
num=L//G
A=[]
for i in range(num):
    A.append(st[i*G:(i+1)*G])
B=[]
for i in range(len(A)):
    B.append(A[i][::-1])
res=' '.join(B)
print(A,B,res)