with open('input1.txt','r') as f:
    L=f.read()
A=[]
for i in range(len(L)):
    A.append(L[i])
c=A.count('!')
s1=0
if c!=0:
    for i in range(c):
        x=A.index('!')
        if (A[x+1]==' ') or (A[x+1]=='\n'):
            s1=s1+1
        else: A[x]='0'
c=A.count('.')
s2=0
if c!=0:
    for i in range(c):
        x=A.index('.')
        if (A[x+1]==' ') or (A[x+1]=='\n'):
            s2=s2+1
        else: A[x]='0'
c=A.count('?')
s3=0
if c!=0:
    for i in range(c):
        x=A.index('?')
        if (A[x+1]==' ') or (A[x+1]=='\n'):
            s3=s3+1
        else: A[x]='0'
print(s1+s2+s3)