# bubble-sort
def __bubble_sort(data):
    c = 1
    while c !=0:
        c = 0
        for i in range (0, len(data)-1):
            if data[i] > data[i+1]:
                t = data[i]
                data[i] = data[i+1]
                data[i+1] = t
                c +=1
    return data

def sort(data):
    sorted = __bubble_sort(data[:])
    print("Bubble-sort: (sorted)\t", sorted)
