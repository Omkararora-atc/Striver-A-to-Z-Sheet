def subarraySum(nums, k):
    prefix = 0
    count = 0
    hash_map = {0: 1}
    for i in nums:
        prefix += i
        if prefix - k in hash_map:
            count += hash_map[prefix - k]
        if prefix in hash_map:
            hash_map[prefix] += 1
        else:
            hash_map[prefix] = 1
    return count
# ### Example usage:
if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    result = subarraySum(nums, k)
    print("Number of subarrays with sum equal to", k, ":", result)

    nums = [1, 2, 3]
    k = 3
    result = subarraySum(nums, k)
    print("Number of subarrays with sum equal to", k, ":", result)