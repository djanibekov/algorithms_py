inversion_count = 0

def inversion_counter_conquer(first, second):
    i = 0 
    j = 0
    length_of_first = len(first)
    length_of_second = len(second)
    inversion_count = 0
    merged = []
    #? looking for number of particular inversion
    while (i < length_of_first) and (j < length_of_second):
        if (first[i] > second[j]):
            inversion_count += length_of_first - i
            merged.append(second[j])
            j = j + 1
        else:
            merged.append(first[i])
            i = i + 1

    #! extra check whether element is left
    while i < len(first):
        merged.append(first[i])
        i = i + 1
    while j < len(second):
        merged.append(second[j])
        j = j + 1
    return merged, inversion_count

def list_divider_divide(array):
    """[This function divides the input list/array in to two parts recursively
        by divide and conquer method till the base case.]

    Args:
        array ([list]): [given input]

    Returns:
        [int]: [final answer of the question "How many inversions did list hold?"]
        [list]: [the sorted array/list of two derived lists "left" and "right"]
    """
    length = len(array)
    if(length == 1):
        return array, 0
    mid = length // 2
    left = list_divider_divide(array[:mid])
    right = list_divider_divide(array[mid:])
    
    #? inversion_count holds the sum of all particular #inversion
    merged, particular_inversions = inversion_counter_conquer(left[0], right[0])
    inversion_count = particular_inversions + left[1] + right[1]

    return merged, inversion_count

f_name = open("IntegerArray.txt")
integers = []
for integer in f_name:
    integers.append(int(integer))

print(list_divider_divide(integers)[1])
