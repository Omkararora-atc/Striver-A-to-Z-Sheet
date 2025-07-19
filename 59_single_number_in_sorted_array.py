def singleNonDuplicate(nums):
    n = len(nums)
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]
# ### Example usage:
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4]
    result = singleNonDuplicate(nums)
    print(f"The single non-duplicate element is: {result}")

    nums = [1, 2, 2, 3, 3]
    result = singleNonDuplicate(nums)
    print(f"The single non-duplicate element is: {result}")