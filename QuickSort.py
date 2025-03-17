import random


def quickSort(data, begin, end):
    if begin < end:
        partitionIndex =  partition(data, begin, end)

        quickSort(data, begin, partitionIndex - 1)
        quickSort(data, partitionIndex + 1, end)

def partition(data, begin, end):
    pivot = data[end]
    partitionIndex = begin - 1
    
    for x in range(begin, end):
        if data[x] < pivot or data[x] == pivot:
            partitionIndex += 1
            temp = data[partitionIndex]
            data[partitionIndex] = data[x]
            data[x] = temp
    
    temp = data[partitionIndex + 1]
    data[partitionIndex + 1] = data[end]
    data[end] = temp

    return partitionIndex + 1