# Authors: Christopher Waschke, Jackson Jenks, Brody Weinkauf
# Assignment: Week 11 - Sorting Algorithms
# Description: This file contains a Merge Sort Algorithm.

# Ah, python. Language of my life.
# Funny how the last bit of code I'm writing for my portion is Python. - Christopher.

# Function _merge (leading underscore for private method) -> None.  (uses references for modifications)
# Performs the comparison and merging of our two arrays.
# After the split performed in the mergeSort method, we then iterate over the values in each array
# Swapping their positions in the original array, depending upon which value is lesser.
# 
# Parameters:
#  left     (list), the split array on the left to compare.
#  right    (list), the split array on the right to compare.
#  original (list), the original array, in which our sorted values will go into.
def _merge(left: list, right: list, original: list) -> None:
    left_length = len(left)
    right_length = len(right)
    left_index = 0
    right_index = 0
    primary_index = 0
    while left_index < left_length and right_index < right_length:
        if left[left_index] < right[right_index]:
            original[primary_index] = left[left_index]
            left_index += 1
            primary_index += 1
        else:
            original[primary_index] = right[right_index]
            right_index += 1
            primary_index += 1
    while left_index < left_length:
        original[primary_index] = left[left_index]
        left_index += 1
        primary_index += 1
    while right_index < right_length:
            original[primary_index] = right[right_index]
            right_index += 1
            primary_index += 1
    
# Function mergeSort -> None (Modifies through reference)
# This method takes in the original array we wish to sort.
# The method will split our array down by recursively calling this method.
# Base case is when the array called upon has a length of 1, which means it can no longer split.
# Once the arrays have been fully split, we call the merge function, to sort each split array.
# It is the merge function that actually performs the sorting of the array, with the comparison.
#
# Parameters:
# sort_list (list) The list to be sorted.
def merge_sort(sort_list: list) -> None:
    if len(sort_list) == 1:
         return

    mid_point = len(sort_list) // 2 # Divide, rounded down, due to Python automatic float conversion

    left = sort_list[:mid_point] # left = everything until mid point
    right = sort_list[mid_point:] # right = everything after mid point

    merge_sort(left)
    merge_sort(right)

    _merge(left, right, sort_list)

if __name__ == "__main__":
    x = [2, 1, 5, 4, 9]
    merge_sort(x)
    print(x)