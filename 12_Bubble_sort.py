def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# ### Driver Code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = bubble(arr)
    print("Sorted array:", sorted_arr)