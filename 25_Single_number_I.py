def single(arr):
    n=len(arr)
    if n==0:
        return None
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in count:
        if count[i]==1:
            return i
    return None
# ### Example usage:
if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    single_number = single(arr)
    print("The single number is:", single_number)