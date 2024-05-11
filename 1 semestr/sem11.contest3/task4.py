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

N,R=map(int,input().split())
klm=list(map(int,input().split()))
KLM=quicksort(klm)
count=0
end=float('-inf')
for coordinates in KLM:
    if coordinates-R > end:
        count += 1
        end = coordinates+R
print(count)

