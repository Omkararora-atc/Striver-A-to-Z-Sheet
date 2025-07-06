def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    i,j,k=0,0,low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
def merge_sort(arr,low,high):
    mid = (low + high) // 2
    if low<high:
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
# ### Driver Code
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    n = len(arr)
    merge_sort(arr, 0, n - 1)
    print("Sorted array:", arr)