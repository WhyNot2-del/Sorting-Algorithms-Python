import random

class QuickSort:
    def quickSort(data, begin, end):
        if begin < end:
            partitionIndex = QuickSort.partition(data, begin, end)

            QuickSort.quickSort(data, begin, partitionIndex - 1)
            QuickSort.quickSort(data, partitionIndex + 1, end)

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

data = [None] * 50

for x in range(50):
    data[x] = random.randint(1, 50)

print("Unsorted data")
for x in range(50):
    print(data[x], end=" ")

QuickSort.quickSort(data, 0, 49)

print("\nSorted data")
for x in range(50):
    print(data[x], end=" ")