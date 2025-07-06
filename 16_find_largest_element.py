def largest(arr):
    if not arr:
        return None
    max_val=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            max_val=arr[i]
    return max_val
# ### Driver Code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11,-5, 100, 0]
    largest_element = largest(arr)
    print("Largest element in the array:", largest_element)
