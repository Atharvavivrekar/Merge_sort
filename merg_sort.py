import random
list = [random.randint(1,20) for i in range(8)]

print(list)

def merge (low,mid,high):
    pass

def merge_sort (low,high):
    if low < high:
        mid = (high + low) //2 
        merge_sort(low,mid)
        merge_sort(mid + 1,high)
        merge(low,mid,high) 