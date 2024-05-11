def heapify(i,list):
    n = len(list)
    while True:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and list[i] < list[l]:
            largest = l
        if r < n and list[largest] < list[r]:
            largest = r
        if largest==i:
            break
        temp,list[i]=list[i],list[largest]
        list[largest]=temp
        i=largest

def heapSort(list):
    n=len(list)
    i=n//2
    while i>=0:
        heapify(i,list)
        i-=1

inp=list(map(int,input().split()))
heap_list=inp
heapSort(heap_list)
print(' '.join(list(map(str,heap_list))))