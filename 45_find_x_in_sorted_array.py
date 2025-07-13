def find(arr,x):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 5
    index = find(arr, x)
    if index != -1:
        print(f"Element {x} found at index: {index}")
    else:
        print(f"Element {x} not found in the array.")