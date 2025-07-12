def union(arr1,arr2):
    i,j=0,0
    m,n=len(arr1),len(arr2)
    res=[]
    while i<m and j<n:
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i]==arr2[j]:
            res.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<m:
        if i==0 or arr1[i]!=arr1[i-1]:
            res.append(arr1[i])
        i+=1
    while j<n:
        if j==0 or arr2[j]!=arr2[j-1]:
            res.append(arr2[j])
        j+=1
    return res
# ### Example usage:
if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    result = union(arr1, arr2)
    print("Union of the two arrays:", result)
    arr1=[3,4,6,7,9,9]
    arr2=[1,5,7,8,8]
    result = union(arr1, arr2)
    print("Union of the two arrays:", result)