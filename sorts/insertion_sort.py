def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while(j >= 0 and arr[j] > key): 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr 

arr = [5,4,3,2,1]
arr = insertion_sort(arr)
print(arr)