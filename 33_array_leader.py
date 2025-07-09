def array_leader(arr):
    n=len(arr)
    leaders=[]
    max_right=arr[-1]
    leaders.append(max_right)
    for i in range(n-2,-1,-1):
        if arr[i]>max_right:
            max_right=arr[i]
            leaders.append(max_right)
    return leaders[::-1]
# ### Example usage:
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    leaders = array_leader(arr)
    print("Leaders in the array are:", leaders)