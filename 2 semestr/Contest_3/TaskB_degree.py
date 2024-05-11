def prefix_fun(s):
    l = len(s)
    P = [0 for i in range(l)]
    for i in range(1, len(s)):
        sup = P[i-1]
        while sup > 0 and s[sup] != s[i]:
            sup = P[sup - 1]
        if s[sup] == s[i]:
            sup += 1
        P[i] = sup
    return P

def main_task():
    s = input()
    p = prefix_fun(s)
    m = len(s)
    k = m - p[m-1]
    if (m % k) == 0:
        n = m // k
    else:
        n = 1
    return n

t = int(input())
for _ in range(t):
    print(main_task())