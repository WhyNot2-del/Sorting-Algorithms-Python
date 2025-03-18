import random

# quicksort algorithm for sorting items
def quickSort(data, begin, end):
    # base case for recursion, if there is only one or zero items being sorted
    if begin < end:
        # breaks down data into two smaller parts
        partitionIndex =  partition(data, begin, end)

        # sorts the two broken down parts
        quickSort(data, begin, partitionIndex - 1)
        quickSort(data, partitionIndex + 1, end)

# breaks down the data into two smaller parts
def partition(data, begin, end):
    pivot = data[end]
    partitionIndex = begin - 1
    
    # checks every value in current part
    # if value is smaller or the same as pivot value, swap the two values and increase the partitionIndex
    for x in range(begin, end):
        if data[x] < pivot or data[x] == pivot:
            partitionIndex += 1
            temp = data[partitionIndex]
            data[partitionIndex] = data[x]
            data[x] = temp
    
    # after all values have been checked, swap pivot value to final position
    temp = data[partitionIndex + 1]
    data[partitionIndex + 1] = data[end]
    data[end] = temp

    # return index of the final position of the pivot value
    return partitionIndex + 1