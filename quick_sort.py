from math import ceil

count = 0
def find_median(array, length:int):
    mid = ceil(length/2)
    miniset = sorted([array[0], array[mid], array[-1]])
    return miniset[1]


def partition(array, l:int, r:int):
    pivot = array[l]
    i = l + 1
    for j in range(l+1, r):
        if(array[j] < pivot):
            array[j], array[i] = array[i], array[j]
            i = i + 1
    array[l], array[i-1] = array[i-1], array[l]
    return i-1


def quick_sort(array):
    length = len(array)
    if(length<=1):
        return array
    
    global count 

    pivot_index = partition(array, 0, length)
    array[:pivot_index] = quick_sort(array[:pivot_index])
    count += len(array[:pivot_index])-1
    
    array[pivot_index+1:] = quick_sort(array[pivot_index+1:])
    count += len(array[pivot_index+1:])-1

    return array


with open('quick_sort.txt') as f:
    array = [int(x) for x in f]



print(quick_sort(array))
print(count)