f = open('input.txt')
a=f.readline()
A=list(map(float,a.split()))
b=f.readline()
if b=='*\n':
    s=1
    for i in range(len(A)):
       s=s*A[i]
elif b=='+\n':
    s=0
    for i in range(len(A)):
        s = s + A[i]
elif b=='-\n':
    s=0
    for i in range(len(A)):
        s = s - A[i]
g=open('output.txt', 'w')
g.write(str(s))
g.close()