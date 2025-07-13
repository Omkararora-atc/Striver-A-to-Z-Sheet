def merge(arr):
    if not arr:
        return []
    arr.sort(key=lambda x: x[0])
    temp=[]
    res=0
    for i in range(1,len(arr)):
        if arr[res][1]>=arr[i][0]:
            arr[res][1]=max(arr[res][1],arr[i][1])
        else:
            res+=1
            arr[res]=arr[i]
    return arr[:res+1]
# ### Example usage:
if __name__ == "__main__":
    intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
    merged_intervals = merge(intervals)
    print("Merged intervals are:", merged_intervals)