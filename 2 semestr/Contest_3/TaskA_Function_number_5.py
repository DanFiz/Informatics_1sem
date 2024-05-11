#z-a
#переворот строки
#перебор индексов и 2*n - 1 - i

def Z_fun(s):
    ln = len(s)
    z = [0 for i in range(ln)]
    l = 0
    r = 0
    for i in range(1, len(s)):

        z[i] = max(0, min(r-i, z[i - l]))
        while i + z[i] < ln and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
        if 1 + z[i] > ln:
            r = ln
        
    return z

n = int(input())

s = input()
s0 = s[::-1]
S = s + s0
z = Z_fun(S)
ln = []
for i in range(n):
    ln.append(z[2*n - 1 - i])
print(*ln)