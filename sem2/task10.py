with open('input2.txt', encoding='utf-8', mode='r') as f:
    L=f.readlines()
A=(' '.join(L)).split()
B=['а','о','у','ы','и','э','я','ю','ё','е']
for i in range(len(A)):
    st=A[i]
    C=[]
    for g in range(len(st)):
        C.append(st[g])
    j=1
    while j <= len(st)-1 :
        if ((st[j] in B) == True) and ((st[j-1] in B) == False):
            a='c'+st[j]
            C[j]=C[j]+a
        j = j + 1
    print(''.join(C),end=' ')