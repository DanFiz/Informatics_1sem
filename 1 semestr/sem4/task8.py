A=set(list(map(float,input().split())))
B=set(list(map(float,input().split())))
A1=list(A.difference(B))
B1=list(B.difference(A))
C=list(A.union(B))
D=list(A.intersection(B))
print(' '.join(list(map(str,A1))))
print(' '.join(list(map(str,B1))))
print(' '.join(list(map(str,C))))
print(' '.join(list(map(str,D))))