# Class to run&test different sorting algorithms
import random
import bubble_sort
import merge_sort
import insertion_sort

def main():
    unsorted = [random.randint(-100, 1000) for i in range(0, 30)]
    print("unsorted list:", unsorted)
    bubble_sort.sort(unsorted)
    merge_sort.sort(unsorted)
    insertion_sort.sort(unsorted)

if __name__ == "__main__":
    main()