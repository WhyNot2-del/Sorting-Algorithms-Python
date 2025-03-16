# Authors: Christopher Waschke, Jackson Jenks, Brody Weinkauf
# Assignment: Week 11 - Sorting Algorithms
# Description: The Test/UI Class for our sorting Algorithms.

from typing import List
from MergeSort import merge_sort
from QuickSort import QuickSort

# Function menu -> string
# Shows our selection options, and prompts the user for a selection.
def menu() -> str:
    print("m.) Merge Sort")
    print("q.) Quick Sort")
    print("s.) Shell Sort")
    print("x.) Exit")
    return input("Please make a selection> ").lower()

# Function get_user_ints -> List[Integer]
# This method gets a line of integers from the command line as a string.
# It then loops over numbers separated by spaces converting them into actual ints
# If an invalid substring is found, we catch the ValueError, print our own error message, and bubble it.
# Finally, we return the list of ints from the converted strings.
def get_user_ints() -> List[int]:
    int_list = []
    print("Please input your integers to be sorted.")
    int_str = input("Integers> ")
    for numb in int_str.split(" "):
        try:
            int_list.append(int(numb))
        except ValueError:
            print("Please only insert numbers.")
            raise ValueError
    return int_list

# Function do_merge_sort -> None
# First we get a list of integers from the user.
# Then we perform the merge sort on the list.
# Then we print out the changed list.
def do_merge_sort() -> None:
    try:
        int_list = get_user_ints()
        merge_sort(int_list)
        print(int_list)
    except ValueError:
        pass

# Function do_quick_sort -> None
# First we get a list of integers from the user.
# Then we perform the quick sort on the list.
# Then we print out the changed list.
def do_quick_sort() -> None:
    try:
        int_list = get_user_ints()
        QuickSort.quickSort(int_list, 0, len(int_list)-1)
        print(int_list)
    except ValueError:
        pass

# Function do_shell_sort -> None
# First we get a list of integers from the user.
# Then we perform the shell sort on the list.
# Then we print out the changed list.
def do_shell_sort() -> None:
    print("Not implemented.")

# Function main -> None
# Not technically our Entry point due to Python, but first and only if the script is directly executed.
# Loops through a menu, asking a user for their choice of what sort they want to do, until the user requests to quit.
# The code branches into the function related to what sort is requested, or exits.
def main() -> None:
    running = True
    while(running):
        # Ah! I'll use a match here to mimic the others with Switch statements. Thanks Python 3.10!
        # I programmed Python before we had them.
        # Python matches don't require breaks after a statement.
        # In fact, I found out the hard way here that break statement in a match still break out of a loop.
        # As such, I've omitted them.
        match menu():
            case "m":
                do_merge_sort()
            case "q":
                do_quick_sort()
            case "s":
                do_shell_sort()
            case "x":
                running = False
            case _: # Same as default in other languages
                print("Please make a valid choice.")


# In Python, we don't have a main method by default. Instead we check if the module is running directly.
# When that's the case the variable __name__ will be set the "__main__"
# In this case, I'll just call my self defined main method.

if __name__ == "__main__":
    main()
