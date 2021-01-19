def countInversions(array):
    sortedArray, numInv = sortAndCount(array, 0)
    return numInv

def sortAndCount(array, numInv):
    if len(array) <= 1:
        return array, numInv
    else:
        mid = len(array) // 2
        firstHalf, leftInv = sortAndCount(array[:mid], numInv)
        secondHalf, rightInv = sortAndCount(array[mid:], numInv)
        sortedArray, splitInv = countSplitInv(firstHalf, secondHalf)

        totalInv = leftInv + rightInv + splitInv
        return sortedArray, totalInv

def countSplitInv(firstHalf, secondHalf):
    res = [None] * (len(firstHalf) + len(secondHalf))

    ptr1 = 0
    ptr2 = 0
    ptr3 = 0

    numInv = 0

    while ptr1 < len(firstHalf) and ptr2 < len(secondHalf):
        if firstHalf[ptr1] <= secondHalf[ptr2]:
            res[ptr3] = firstHalf[ptr1]
            ptr1 += 1
        else:
            res[ptr3] = secondHalf[ptr2]
            ptr2 += 1
            numInv += (len(firstHalf) - ptr1)
        
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
    
    return res, numInv


f = open('count_inversions_input.txt', 'r')
data = f.read().split()
data = list(map(int, data))

print(countInversions(data))