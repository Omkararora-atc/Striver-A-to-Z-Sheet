def upper(arr,x):
    n = len(arr)
    if n == 0:
        return -1
    l, h = 0, n - 1
    while l < h:
        mid = (l + h) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            h = mid
    return l
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    x = 2
    index = upper(arr, x)
    print("Upper bound index of", x, "is:", index)
