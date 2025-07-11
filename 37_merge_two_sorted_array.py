def merge(arr1,m,arr2,n):
    temp=arr1[:m]
    i,j,k=0,0,0
    while i<m and j<n:
        if temp[i]<arr2[j]:
            arr1[k]=temp[i]
            i+=1
        else:
            arr1[k]=arr2[j]
            j+=1
        k+=1
    while i<m:
        arr1[k]=temp[i]
        i+=1
        k+=1
    while j<n:
        arr1[k]=arr2[j]
        j+=1
        k+=1
    return arr1
# ### Example usage:
if __name__ == "__main__":
    arr1 = [1, 3, 5, 0, 0, 0]
    m = 3
    arr2 = [2, 4, 6]
    n = 3
    merged_array = merge(arr1, m, arr2, n)
    print("Merged array:", merged_array)