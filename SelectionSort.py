#This is a selection sort. It is comprised of nested for loops that loop through the arrays and swaps values depending on if the values are greater or lesser.
def selection_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] > array[j]:
                tempCar = array[i]
                array[i] = array[j]
                array[j] = tempCar