# Bubble-sort
def __bubble_sort(data):
    counter = None
    while counter !=0:
        counter = 0
        for i in range (0, len(data)-1):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                counter +=1
    return data

def sort(data):
    sorted = __bubble_sort(data[:])
    print("Bubble-sort: (sorted)\t", sorted)
