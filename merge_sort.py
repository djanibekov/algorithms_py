def merge(first, second):
    i = 0 
    j = 0
    len1 = len(first)
    len2 = len(second)
    merged = []
    #? combining two lists
    while (i+j < len1+len2):
        if(j>len2 or (i<len1 and first[i] < second[j])):
            merged.append(first[i])
            i = i + 1
        else:
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

    