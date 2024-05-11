with open('input.txt') as f:
    n=int(f.readline())
    X = []
    for i in range(n):
        p=f.readline()
        x, y = map(int, p.split())
        X.append(x)
a=True
x1=(X[0]+X[n-1])/2
for i in range(n//2):
    x0=(X[i]+X[n-i-1])/2
    if x0!=x1:
        a=False
        break
if a==True:
    print('Yes')
else:
    print('No')