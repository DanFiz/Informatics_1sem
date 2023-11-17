print('Введите выражение в инфиксной записи, отделяя все символы пробелом')
f=input()
#f='(2-3)*(12-10)+4/2'
answer=eval(f)
F=f.split()
obrpol=[]
stack=[]
flag=False
i=-1
for token in f:
    if token.isdigit():
        if flag:
            obrpol[i]=obrpol[i]+token
        else:
            obrpol.append(token)
            i += 1
        flag=True
    elif token in ["+", "-", "*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            obrpol.append(stack.pop())
            i+=1
        flag = False
        stack.append(token)
    elif token == "(":
        stack.append(token)
    elif token == ")":
        while stack and stack[-1] != "(":
            obrpol.append(stack.pop())
            flag=False
            i+=1
        stack.pop()

while stack:
    obrpol.append(stack.pop())
print('Обратная польская нотация:')
print(' '.join(obrpol))
obrpol=[]
pryampol=[]
stack1=[]
stack=[]
flag=False
i=-1

for token in f[::-1]:
    if token.isdigit():
        obrpol.append(token)
    elif token in ["+", "-", "*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            obrpol.append(stack.pop())
        stack.append(token)
    elif token == ")":
        stack.append(token)
    elif token == "(":
        while stack and stack[-1] != ")":
            obrpol.append(stack.pop())
        stack.pop()

while stack:
    obrpol.append(stack.pop())
print('Прямая польская нотация:')
print(' '.join(obrpol[::-1]))