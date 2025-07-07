def consecutive(nums):
    max_count=0
    res=0
    for i in nums:
        if i==1:
            res+=1
            max_count=max(max_count,res)
        else:
            res=0
    return max_count
# ### Example usage:
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    max_consecutive_ones = consecutive(nums)
    print("Maximum number of consecutive ones:", max_consecutive_ones)