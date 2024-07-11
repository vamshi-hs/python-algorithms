def merge(arr,low,mid,high):
    left = arr[low:mid]
    right = arr[mid:high]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
def merge_sort(arr,l,r):
    if l < r:
        mid = l + ((r - l) // 2)
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,10]
    merge_sort(arr,0,len(arr))
    print(arr)
