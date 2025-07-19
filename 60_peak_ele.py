def peak(arr):
    n=len(arr)
    left,right=0,n-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]>arr[mid+1]:
            right=mid
        else:
            left=mid+1
    return left
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    peak_index = peak(arr)
    print(f"Peak index in the array: {peak_index}")

    arr = [1, 2, 1, 3, 5, 6, 4]
    peak_index = peak(arr)
    print(f"Peak index in the array: {peak_index}")
