s='37593759375937593759375937593759'
x=[32,16]
for j in range(x[1]):
    i = 0
    if s[i] < s[i + 1]:
        s = s[:i] + s[i + 1:]
        continue
    while (s[i] > s[i + 1]) and i<len(s)-x[1]:
        i += 1
        s = s[:i] + s[i + 1:]
        if len(s)==2:
            break
print(s)