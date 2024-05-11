import random
def Partition(A,m):
    L=[]
    R=[]
    for ai in A:
        if ai<=m:
            L.append(ai)
        elif ai>m:
            R.append(ai)
    A=L+R
    return A
def five_med(B):
    for j in B:
        count_less=0
        count_more=0
        count_eq=0
        for c in B:
            if c<j:
                count_less += 1
            elif c>j:
                count_more += 1
            else:
                count_eq += 1
        if count_less == count_more:
            b=j
            break
        elif (count_less==0 and count_eq==3) or (count_more == 0 and count_eq == 3) or (count_more == 1 and count_eq == 2) or (count_less == 1 and count_eq == 2) or (count_eq == 4):
            b=j
    return b
def find_kth(A,k):
    l=len(A)
    if l==1:
        return A[0]
    p=l//5
    rem=l%5
    B=[]
    for i in range(p):
        tmp = A[i*5:(i+1)*5]
        b=five_med(tmp)
        B.append(b)
    if rem != 0:
        tail = A[-rem:]
        if len(tail) == 1:
            B.append(tail[0])
        elif len(tail) == 2:
            B.append(tail[1])
        elif len(tail) == 3:
            B.append(five_med(tail))
        elif len(tail) == 4:
            tmp1=five_med(tail[:3])
            tmp2=five_med(tail[1:])
            if tmp1>tmp2:
                B.append(tmp1)
            else:
                B.append(tmp2)
    m=find_kth(B,(len(B)//2)+1)
    L,R=Partition(A,m)
    if len(L)>=k:
        return find_kth(L,k)
    elif len(l)==k-1:
        return m
    else:
        find_kth(R,k-len(l)-1)
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)
def det_qs():
    pass
