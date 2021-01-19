import random
import heapq

def quicksort(array, start, end):
    if start >= end:
        return
    else:
        pivotIdx = partition(array, start, end)
        quicksort(array, start, pivotIdx - 1)
        quicksort(array, pivotIdx + 1, end)

def partition(array, left, right):
    pivotIdx = random.randint(left, right)
    array[left], array[pivotIdx] = array[pivotIdx], array[left]
    pivotIdx = left

    while left <= right:
        if left <= right and array[left] <= array[pivotIdx]:
            left += 1

        if left <= right and array[right] > array[pivotIdx]:
            right -= 1
        
        if left <= right:
            array[left], array[right] = array[right], array[left]
    
    array[pivotIdx], array[right] = array[right], array[pivotIdx]

    pivotIdx = right
    return pivotIdx

def driver(array):
    quicksort(array, 0, len(array) - 1)
    return array
    
# print(driver([4,2,6,87,3,912,3,7,1,233,1,18,90,6,77]))

def main(array):
    totalComparisons = mainQuicksort(array, 0, len(array) - 1, 0)
    return totalComparisons

def partitionFirstIdx(array, left, right):
    pivotIdx = left
    numComparisons = right - left + 1
    while left <= right:
        if left <= right and array[left] <= array[pivotIdx]:
            left += 1
        if left <= right and array[right] > array[pivotIdx]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
    
    array[pivotIdx], array[right] = array[right], array[pivotIdx]
    pivotIdx = right
    return pivotIdx, numComparisons

def partitionLastIdx(array, left, right):
    pivotIdx = right
    array[left], array[pivotIdx] = array[pivotIdx], array[left]
    pivotIdx = left

    numComparisons = right - left
    while left <= right:
        if left <= right and array[left] <= array[pivotIdx]:
            left += 1
        if left <= right and array[right] > array[pivotIdx]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
    
    array[pivotIdx], array[right] = array[right], array[pivotIdx]
    pivotIdx = right
    return pivotIdx, numComparisons

def partitionMedianThreeIdx(array, left, right):
    first = array[left]
    last = array[right]
    mid = array[(right - left) // 2 + left]
    potentialPivots = sorted([first, last, mid])
    median = potentialPivots[1]
    pivotIdx = None
    if median == first:
        pivotIdx = left
    elif median == last:
        pivotIdx = right
    else:
        pivotIdx = (right - left) // 2 + left

    numComparisons = right - left
    while left <= right:
        if left <= right and array[left] <= array[pivotIdx]:
            left += 1
        if left <= right and array[right] > array[pivotIdx]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
    
    array[pivotIdx], array[right] = array[right], array[pivotIdx]
    pivotIdx = right
    return pivotIdx, numComparisons

def mainPartitionFirstIdx(array, left, right):
    pivotIdx = left
    i = left
    j = i + 1
    numComparisons = right - left
    while j <= right:
        if array[j] <= array[pivotIdx]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[pivotIdx], array[i] = array[i], array[pivotIdx]
    pivotIdx = i
    return pivotIdx, numComparisons

def mainPartitionLastIdx(array, left, right):
    pivotIdx = right
    i = left
    j = i + 1
    numComparisons = right - left
    array[pivotIdx], array[left] = array[left], array[pivotIdx]
    pivotIdx = left
    while j <= right:
        if array[j] <= array[pivotIdx]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[pivotIdx], array[i] = array[i], array[pivotIdx]
    pivotIdx = i
    return pivotIdx, numComparisons

def mainPartitionMedianThreeIdx(array, left, right):
    first = array[left]
    last = array[right]
    mid = array[(right - left) // 2 + left]
    potentialPivots = sorted([first, last, mid])
    median = potentialPivots[1]

    pivotIdx = None
    if median == first:
        pivotIdx = left
    elif median == last:
        pivotIdx = right
    else:
        pivotIdx = (right - left) // 2 + left
    
    numComparisons = right - left

    i = left
    j = i + 1
    array[pivotIdx], array[left] = array[left], array[pivotIdx]
    pivotIdx = left
    while j <= right:
        if array[j] <= array[pivotIdx]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[pivotIdx], array[i] = array[i], array[pivotIdx]
    pivotIdx = i
    return pivotIdx, numComparisons

def mainQuicksort(array, start, end, numComparisons):
    if start >= end:
        return numComparisons
    else:
        pivotIdx, partitionComparisons = mainPartitionMedianThreeIdx(array, start, end)
        leftComparisons = mainQuicksort(array, start, pivotIdx - 1, 0)
        rightComparisons = mainQuicksort(array, pivotIdx + 1, end, 0)
        
        totalComparisons = partitionComparisons + leftComparisons + rightComparisons
        return totalComparisons

f = open('quicksort_input.txt', 'r')
array = f.read().split()
array = list(map(int, array))
# array = [1,2,3,4]
print(main(array))