def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        d, x, y = gcd_extended(b % a, a)
    return (d, y - (b // a) * x, x)
A=input().split()
a=int(A[0])
b=int(A[1])
c=gcd_extended(a, b)
print(f'{c[0]} {c[1]} {c[2]}')
