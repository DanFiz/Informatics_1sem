from functools import lru_cache
@lru_cache( )
def Rec(N):
    if N==3:
        return (4,2,1)
    return (sum(Rec(N-1)), Rec(N-1)[0], Rec(N-1)[1])
with open('input.txt') as f:
    Z = 1
    while Z!=0:
        Z = int(f.readline())
        if Z == 0:
            continue
        elif Z < 3:
            print(0)
        elif Z==3:
            print(1)
        else:
            O=2**Z - sum(Rec(Z))
            print(O)

