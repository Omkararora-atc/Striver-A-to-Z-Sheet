def longestSubarray( nums, k):
    prefix = 0
    max_len = 0
    hash_map = {}
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix == k:
            max_len = i + 1
        if prefix - k in hash_map:
            max_len = max(max_len, i - hash_map[prefix - k])
        if prefix not in hash_map:
            hash_map[prefix] = i
    return max_len
## Driver Code
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 9
    result = longestSubarray(nums, k)
    print("Length of the longest subarray with sum", k, "is:", result)