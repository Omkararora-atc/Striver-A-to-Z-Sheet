def search(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        if arr[low]==arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        elif arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False
# ### Example usage:
if __name__ == "__main__":
    arr = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    result = search(arr, target)
    print(f"Is {target} present in the rotated sorted array? {result}")

    target = 3
    result = search(arr, target)
    print(f"Is {target} present in the rotated sorted array? {result}")