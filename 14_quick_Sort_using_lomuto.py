def lomuto(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
def quick(arr,l,h):
    if l<h:
        p=lomuto(arr,l,h)
        quick(arr,l,p-1)
        quick(arr,p+1,h)
# ### Driver Code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick(arr, 0, n - 1)
    print("Sorted array:", arr)