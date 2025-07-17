def search(arr,target):
    n=len(arr)
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        if arr[l]<=arr[mid]:
            if arr[l]<=target<arr[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<target<=arr[r]:
                l=mid+1
            else:
                r=mid-1
    return -1
# ### Example usage:
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search(arr, target)
    print(f"Index of {target} in the rotated sorted array: {result}")