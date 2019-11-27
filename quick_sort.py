# Quick-sort

__data = []

def __quick_sort(start, end):
    # choose pivot point
    mid = int((end-start) / 2) + start
    swap(mid, end)
    pivot = __data[end]
    
    # partitioning
    mark = None
    for i in range(0, end):
        if mark == None:
            if __data[i] > pivot: mark = i
        elif __data[i] <= pivot:
            swap(i, mark)
            mark += 1
    if mark != None: 
        swap(mark, end)
    else: mark = end

    # sort sub-sequences
    if mark > 1: 
        __quick_sort(0, mark - 1)
    if end-mark > 1: 
        __quick_sort(mark + 1, end)

def swap(i, j):
    t = __data[i]
    __data[i] = __data[j]
    __data[j] = t


def sort(list):
    global __data
    __data = list[:]
    last = len(__data)-1
    __quick_sort(0, last)
    print("Quick-sort: (sorted)\t", __data)
