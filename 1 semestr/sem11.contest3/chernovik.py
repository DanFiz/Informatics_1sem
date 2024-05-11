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


def h_index(citations):
    for i, cited in enumerate(citations):
        result = len(citations) - i
        if result <= cited:
            return result
    return 0
def H_index(sort_list):
    if len(sort_list)==0:
        return 0
    n=len(sort_list)
    for h in range(1,n+1):
        for i in range(h):
            if sort_list[i]<h:
                return h-1
            elif i>=n-1:
                break
    return n

n, l = map(int, input().split())
list0=list(map(int, input().split()))
sort_list=quicksort(list0)
stack=sort_list
h=h_index(sort_list)
'''for i in sort_list:
    if l==0:
        h_max=h_index(sort_list)
        break
    elif l == n:
        new_list=[]
        for j in range(n):
            new_list.append(sort_list[i]+1)
        h_max = h_index(new_list)
        break
    if len(stack) == l:
        break
    for j in stack:
        if abs(irange(l):
        ind = sort_list-j) == 1:
            mn = min([i,j])
            stack.pop(stack.index(mn))
            break
if l!=n and l!=0:
    new_list_sort=quicksort(stack)
    for i in .index(new_list_sort[i])
        sort_list[ind]=new_list_sort[i]+1
    h_max = h_index(sort_list)
print(h_max)'''