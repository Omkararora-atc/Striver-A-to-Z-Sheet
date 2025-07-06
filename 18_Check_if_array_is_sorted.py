def check(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True
# ### Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    if check(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")
    arr = [5, 3, 2, 4, 1]
    if check(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")
