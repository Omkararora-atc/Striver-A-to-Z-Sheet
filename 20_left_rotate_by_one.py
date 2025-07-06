def left(arr):
    if len(arr) == 0:
        return arr
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first
    return arr
# ### Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    arr = left(arr)
    print("Array after left rotation by one:", arr)
    arr = [10, 20, 30, 40, 50]
    print("Original array:", arr)
    arr = left(arr)
    print("Array after left rotation by one:", arr)