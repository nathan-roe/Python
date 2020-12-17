def selection_sort(arr):
    min = None
    idx = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if min == None:
                min = arr[j]
                idx = j
            elif arr[j] < min:
                min = arr[j]
                idx = j
        if arr[i] > arr[idx]:
            arr[idx], arr[i] = arr[i], arr[idx]
    print(arr)
    return arr
selection_sort([5,3,6,7,8,4,8,9,1,0])