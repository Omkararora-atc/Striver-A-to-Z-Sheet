def maxLen(arr):
    prefix = 0
    max_len = 0
    hash_map = {}
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == 0:
            max_len = i + 1
        if prefix - 0 in hash_map:
            max_len = max(max_len, i - hash_map[prefix - 0])
        if prefix not in hash_map:
            hash_map[prefix] = i
    return max_len
# ### Example usage:
if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    largest_subarray_length = maxLen(arr)
    print("Length of the largest subarray with sum 0 is:", largest_subarray_length)