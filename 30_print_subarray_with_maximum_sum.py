def print_sub(arr):
    res=arr[0]
    max_ending=arr[0]
    start=end=s=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i]+max_ending:
            max_ending=arr[i]
            s=i
        else:
            max_ending+=arr[i]
        if max_ending>res:
            res=max_ending
            start=s
            end=i
    return arr[start:end+1],res
# ### Example usage:
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    subarray, maximum_sum = print_sub(arr)
    print("Subarray with maximum sum is:", subarray)
    print("Maximum sum is:", maximum_sum)