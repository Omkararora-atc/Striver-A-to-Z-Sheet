def count_freq(nums):
    count={}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return [[key,value] for key, value in count.items()]
# ### Driver Code
if __name__ == "__main__":
    nums=[5,5,5,5]
    result = count_freq(nums)
    print("The frequency of each number is:",result)
    nums = [1, 2, 2, 3, 3, 3]
    result = count_freq(nums)
    print("The frequency of each number is:",result)