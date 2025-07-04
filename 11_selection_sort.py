def selection(arr):
    n=len(arr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr
# ### Driver Code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection(arr)
    print("Sorted array:", sorted_arr)
