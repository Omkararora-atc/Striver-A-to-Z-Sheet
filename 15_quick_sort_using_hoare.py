def hoare(arr,l,h):
    pivot=arr[l]
    i=l-1
    j=h+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
def quick(arr,l,h):
    if l<h:
        p=hoare(arr,l,h)
        quick(arr,l,p)
        quick(arr,p+1,h)
# ### Driver Code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick(arr, 0, n - 1)
    print("Sorted array:", arr)