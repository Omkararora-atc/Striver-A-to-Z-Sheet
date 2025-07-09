def rearrange(arr):
    n=len(arr)
    ans=[0]*n
    pos=0
    neg=1
    for i in range(n):
        if arr[i]>=0:
            ans[pos]=arr[i]
            pos+=2
        else:
            ans[neg]=arr[i]
            neg+=2
    return ans
# ### Example usage:
if __name__ == "__main__":
    arr = [-1, 2, -3, 4, -5, 6]
    rearranged_array = rearrange(arr)
    print("Array after rearranging positive and negative numbers:", rearranged_array)