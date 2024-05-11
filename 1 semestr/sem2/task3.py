st=input()
L=len(st)
num_steps=L//2
flag1=True
for i in range(num_steps):
    if st[i]!=st[-(i+1)]:
        flag1=False
        break
res=f'{st} palindrome = {flag1}'
flag2=False
B=['A','H','I','M','O','T','U','V','W','W','X','Y','1','8','0']
C=['E','J','S','Z']
D=['3','L','2','5']
for i in range(L):
    if ((st[i] in B) == True):
        flag2=True
    elif ((st[i] in C) == True):
        x=C.index(st[i])
        if st[-(i+1)]!=D[x]:
            flag2=False
            break
    elif ((st[i] in D) == True):
        x=D.index(st[i])
        if st[-(i+1)]!=C[x]:
            flag2=False
            break
res2=f'{st} mirrors = {flag2}'
print(res,res2,sep='\n')
if flag1==True and flag2==True:
    print(f'{st} mirrored palindrome = {flag2}')
else: print(f'{st} mirrored palindrome = False')