def two_sum(arr,target):
    n=len(arr)
    count={}
    for i,num in enumerate(arr):
        com=target-num
        if com in count:
            return [count[com],i]
        count[num]=i
    return []
# ### Example usage:
if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    result = two_sum(arr, target)
    if result:
        print("Indices of the two numbers that add up to", target, "are:", result)
    else:
        print("No two numbers add up to", target)