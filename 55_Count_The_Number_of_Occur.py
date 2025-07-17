def count(arr, target):
    n = len(arr)
    first, last = -1, -1
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                first = mid
                break
            else:
                r = mid - 1
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            if mid == n - 1 or arr[mid + 1] != target:
                last = mid
                break
            else:
                l = mid + 1
    if first == -1:
        return 0
    return last - first + 1

# ### Example usage:
if __name__ == "__main__":
    arr = [5, 7, 7, 8, 8, 10]
    target = 8
    count_result = count(arr, target)
    print(f"Count of {target} in the array: {count_result}")
