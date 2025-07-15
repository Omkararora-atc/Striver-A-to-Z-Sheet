def floor_celling(arr,x):
    low,high = 0,len(arr)-1
    floor, ceiling = -1,-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            ceiling = arr[mid]
            high = mid - 1
    return floor, ceiling
# ### Example usage:
if __name__ == "__main__":
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    floor, ceiling = floor_celling(arr, x)
    print("Floor:", floor)
    print("Ceiling:", ceiling)