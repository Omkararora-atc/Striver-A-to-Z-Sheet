def lower_bound(arr,x):
    n=len(arr)
    if n==0:
        return -1
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left if left < n and arr[left] == x else -1
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4]
    x = 2
    index = lower_bound(arr, x)
    if index != -1:
        print(f"The lower bound of {x} is at index: {index}")
    else:
        print(f"{x} is not present in the array.")