def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        firstHalf = array[:mid]
        secondHalf = array[mid:]
        return merge(mergesort(firstHalf), mergesort(secondHalf))



def merge(firstHalf, secondHalf):
    res = [None] * (len(firstHalf) + len(secondHalf))
    ptr1 = 0
    ptr2 = 0
    ptr3 = 0

    while ptr1 < len(firstHalf) and ptr2 < len(secondHalf):
        if firstHalf[ptr1] <= secondHalf[ptr2]:
            res[ptr3] = firstHalf[ptr1]
            ptr1 += 1
        else:
            res[ptr3] = secondHalf[ptr2]
            ptr2 += 1
        
        ptr3 += 1
    
    if ptr1 >= len(firstHalf):
        while ptr2 < len(secondHalf):
            res[ptr3] = secondHalf[ptr2]
            ptr2 += 1
            ptr3 += 1

    if ptr2 >= len(secondHalf):
        while ptr1 < len(firstHalf):
            res[ptr3] = firstHalf[ptr1]
            ptr1 += 1
            ptr3 += 1

    return res

print(mergesort([2, 8, 1, 8, 6, 8, 2, 4]))