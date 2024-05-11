N=input()
b=int(input())
c=input()
if int(c)==10:
    print(int(N,b))
elif int(c)==2:
    if int(N)<0:
        print('-'+bin(int(N,b))[3:])
    else:
        print(bin(int(N,b))[2:])
elif int(c)==8:
    if int(N) < 0:
        print('-' + oct(int(N, b))[3:])
    else:
        print(oct(int(N, b))[2:])
elif int(c)==16:
    if int(N) < 0:
        print('-' + hex(int(N, b))[3:])
    else:
        print(hex(int(N, b))[2:])