g = input().split()
N=int(g[0])
b=g[1]
def tri(N, i,n):
    if N == 0:
        if n == 1:
            print(b*i)
        return
    print(b*i)
    tri(N-1,i+1,n)
    print(b*i)
n=N % 2
tri(N//2 , 1, n)