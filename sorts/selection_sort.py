def selection_sort(arr):
    for i in range(0,len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[min] > arr[j]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr

arr = [5,4,3,2,1]
arr = selection_sort(arr)
print(arr)