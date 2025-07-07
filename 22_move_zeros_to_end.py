def move(arr):
    n=len(arr)
    if n<=1:
        return arr
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr
### Example usage:
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    move(arr)
    print("Array after moving zeros to the end:", arr)