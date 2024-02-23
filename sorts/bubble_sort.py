def bubble_sort(arr):
    i = 0
    j = 0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
    
arr = [5,4,3,2,1]
bubble_sort(arr)
print(arr)