def longest(arr):
    if not arr:
        return 0
    arr.sort()
    curr=1
    res=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            continue
        elif arr[i]==arr[i-1]+1:
            curr+=1
            res=max(res,curr)
        else:
            curr=1
    return res
# ### Example usage:
if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    longest_sequence_length = longest(arr)
    print("Length of the longest consecutive sequence is:", longest_sequence_length)

