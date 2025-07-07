def maxi_sum(arr):
    res=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        max_sum=max(arr[i],max_sum+arr[i])
        res=max(res,max_sum)
    return res
# ### Example usage:
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    maximum_sub_array_sum = maxi_sum(arr)
    print("Maximum subarray sum is:", maximum_sub_array_sum)