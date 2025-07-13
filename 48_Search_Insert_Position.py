def insert(arr,target):
    n=len(arr)
    if n==0:
        return 0
    low, high = 0,n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    target = 5
    position = insert(arr, target)
    print("Insert position for", target, "is:", position)

    target = 2
    position = insert(arr, target)
    print("Insert position for", target, "is:", position)

    target = 7
    position = insert(arr, target)
    print("Insert position for", target, "is:", position)

    target = 0
    position = insert(arr, target)
    print("Insert position for", target, "is:", position)