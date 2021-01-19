import random

def rselect(array, left, right, orderStat):
    if left >= right:
        return array[left]
    else:
        pivotIdx = partition(array, left, right)
        if pivotIdx == orderStat:
            return array[pivotIdx]
        elif orderStat < pivotIdx:
            return rselect(array, left, pivotIdx - 1, orderStat)
        else:
            return rselect(array, pivotIdx + 1, right, orderStat)
            
def partition(array, left, right):
    pivotIdx = random.randint(left, right)
    array[left], array[pivotIdx] = array[pivotIdx], array[left]
    pivotIdx = left

    while left <= right:
        while left <= right and array[left] <= array[pivotIdx]:
            left += 1
        
        while left <= right and array[right] > array[pivotIdx]:
            right -= 1
        
        if left <= right:
            array[left], array[right] = array[right], array[left]
    
    array[right], array[pivotIdx] = array[pivotIdx], array[right]

    pivotIdx = right
    return pivotIdx

def main(array, orderStat):
    return rselect(array, 0, len(array) - 1, orderStat)

print(main([2,5,1,3,6,9,4,7,0,8], 6))
