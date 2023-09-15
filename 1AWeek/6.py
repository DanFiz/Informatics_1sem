f = open('input.txt')
a=f.readline()
A=list(map(int,a.split()))
b=f.readline()
d=f.readline()
B=list(map(int,d.split()))
for i in range(len(A)):
    A[i]=int(str(A[i]),B[0])
if b=='*\n':
    j=1
    for i in range(len(A)):
       j=j*A[i]
elif b=='+\n':
    j=0
    for i in range(len(A)):
         j= j + A[i]
elif b=='-\n':
    j=0
    for i in range(len(A)):
        j = j - A[i]
g=open('output.txt', 'w')
if B[0]==10:
    g.write(str(j))
elif B[0]==8:
    if j < 0:
        g.write('-'+oct(j)[3:])
    else :
        g.write(oct(j)[2:])
elif B[0]==2:
    if j < 0:
        g.write('-'+bin(j)[3:])
    else:
        g.write(bin(j)[2:])
g.close()
