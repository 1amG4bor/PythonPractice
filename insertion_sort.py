# Insertion-sort

def __insertion_sort(data):
	if len(data) <= 1: return data
	for i in range(1, len(data)):
		n = data.pop(i)
		for j in range(i-1, -1, -1):
			if data[j] <= n: 
				data.insert(j+1, n)
				break
			if j == 0: data.insert(0, n)
	return data

def sort(data):
    sorted = __insertion_sort(data[:])
    print("Insertion-sort: (sorted)", sorted)
