
def findMissingRepeatingNumbers(nums):
        n = len(nums)
        nums.sort()
        missing = -1
        repeating = -1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                repeating = nums[i]
            elif nums[i] - nums[i - 1] > 1:
                missing = nums[i - 1] + 1
        if nums[0] != 1:
            missing = 1
        if nums[-1] != n:
            missing = n

        return [repeating, missing]
# ### Example usage:
if __name__ == "__main__":
    nums = [3, 1, 2, 5, 3]
    result = findMissingRepeatingNumbers(nums)
    print("Repeating number:", result[0])
    print("Missing number:", result[1])