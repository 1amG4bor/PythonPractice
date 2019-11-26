# merge-sort

def __merge_sort(data):
    if len(data) > 1:
        m = int(len(data)/2)        
        low = __merge_sort(data[0:m])
        high = __merge_sort(data[m:])
    else: return data
    
    sorted = []
    while low != [] or high != []:
        if low == []: next = high.pop(0)
        elif high == []: next = low.pop(0)
        else: next = low.pop(0) if low[0] < high[0] else high.pop(0)
        sorted.append(next)
    return sorted

def sort(data):
    sorted = __merge_sort(data[:])
    print("Merge-sort: (sorted)\t", sorted)
