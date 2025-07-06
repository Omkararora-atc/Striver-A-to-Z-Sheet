def rem(arr):
    i=0
    n=len(arr)
    for j in range(n):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1
### Driver Code
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 5]
    new_length = rem(arr)
    print("Array after removing duplicates:", arr[:new_length])
    arr = [10, 20, 20, 30, 30, 40]
    new_length = rem(arr)
    print("Array after removing duplicates:", arr[:new_length])