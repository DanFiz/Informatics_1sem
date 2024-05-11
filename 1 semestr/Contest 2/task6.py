with open('input.txt') as f:
    a=1
    while a!=0:
        x=list(map(int,f.readline().split()))
        if x[0]==0:
            break
        d = list(f.readline())
        n=x[0]
        i=0
        p=x[1]
        while p>0 and i < n-p+1:
            if d[i] <= d[i + 1]:
                del d[i]
                p -= 1
                if i:
                    i -= 1

            else:
                i += 1
        print(''.join(d[:-1]))

