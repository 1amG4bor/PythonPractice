# Class to run&test different sorting algorithms
import random
import bubble_sort, merge_sort, insertion_sort, quick_sort

def main():
    unsorted = [random.randint(-999, 9999) for i in range(0, 25)]
    print("unsorted list:", unsorted)
    bubble_sort.sort(unsorted)
    merge_sort.sort(unsorted)
    insertion_sort.sort(unsorted)
    quick_sort.sort(unsorted)

if __name__ == "__main__":
    main()
