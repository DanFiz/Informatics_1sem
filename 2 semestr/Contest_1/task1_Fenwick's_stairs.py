def Prefix_sum(i, Fenwick):
    result = 0
    while i >= 0:
        result += Fenwick[i]
        i = (i & (i + 1)) - 1
    return result

def Update(i, delta, max_value, Fenwick):
    while i < max_value:
        Fenwick[i] += delta
        i = i | (i + 1)

def task1_Fenwicks_stairs():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        value_list = list(map(int, input().split()))
        max_value = max(value_list) + 1
        Fenwick = [0] * max_value
        sum_result = 0
        for value in value_list:
            Update(value, value, max_value, Fenwick)
            sum_result += Prefix_sum(value-1, Fenwick)
        print(sum_result)
task1_Fenwicks_stairs()