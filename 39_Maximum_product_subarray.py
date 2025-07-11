def maximum_prod(arr):
    max_curr = min_curr = max_prod = arr[0]
    for i in range(1,len(arr)):
        temp=max_curr
        max_curr=max(arr[i],arr[i]*max_curr,arr[i]*min_curr)
        min_curr=min(arr[i],arr[i]*temp,arr[i]*min_curr)
        max_prod=max(max_prod,max_curr)
    return max_prod
# ### Example usage:
if __name__ == "__main__":
    arr = [2, 3, -2, 4]
    maximum_product = maximum_prod(arr)
    print("Maximum product subarray is:", maximum_product)
    arr2 = [-2, -3, -4]
    maximum_product2 = maximum_prod(arr2)
    print("Maximum product subarray for negative numbers is:", maximum_product2)
