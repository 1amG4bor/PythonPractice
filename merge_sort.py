# Merge-sort

def __merge_sort(data):
    # divide
    if len(data) < 2: return data
    else:
        mid = int(len(data)/2)        
        left = __merge_sort(data[:mid])
        right = __merge_sort(data[mid:]) 
    
    # merge
    sorted = []
    while left != [] or right != []:
        if left == []: next = right.pop(0)
        elif right == []: next = left.pop(0)
        else: next = left.pop(0) if left[0] < right[0] else right.pop(0)
        sorted.append(next)
    return sorted

def sort(data):
    sorted = __merge_sort(data[:])
    print("Merge-sort: (sorted)\t", sorted)
