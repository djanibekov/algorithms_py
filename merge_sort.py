def merge(first, second):
    i = 0 
    j = 0
    merged = []
    #? combining two lists
    while i < len(first) and j < len(second):
        if(first[i] < second[j]):
            merged.append(first[i])
            i = i + 1
        else:
            merged.append(second[j])
            j = j + 1

    #! extra check whether element is left
    while i < len(first):
        merged.append(first[i])
        i = i + 1
    while j < len(second):
        merged.append(second[j])
        j = j + 1

    return merged

def merge_sort(array):
    length = len(array)
    if(length == 1):
        return array
    mid = length // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


print(merge_sort([1, 3, 5, 2, 4, 6]))

    