def findKRotation(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return low
# ### Example usage:
if __name__ == "__main__":
    nums = [15, 18, 2, 3, 6, 12]
    k_rotation = findKRotation(nums)
    print(f"The array is rotated {k_rotation} times.")

    nums = [4, 5, 6, 7, 0, 1, 2]
    k_rotation = findKRotation(nums)
    print(f"The array is rotated {k_rotation} times.")

    nums = [1, 2, 3, 4, 5]
    k_rotation = findKRotation(nums)
    print(f"The array is rotated {k_rotation} times.")
