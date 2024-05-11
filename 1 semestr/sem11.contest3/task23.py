import random
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
N=int(input())
length={}
for i in range(N):
    l,r=map(int,input().split())
    length[r]=l

R=quicksort(list(length.keys()))

count = 0
end = float('-inf')
for r in R:
    l = length.get(r)
    if l > end:
        count += 1
        end = r
print(count)
