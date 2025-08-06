def minimumRateToEatBananas(nums, h):
    def finish(k):
        total = 0
        for pile in nums:
            total += (pile + k - 1) // k
        return total <= h
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if finish(mid):
            right = mid
        else:
            left = mid + 1
    return left
# ### Example usage:
if __name__ == "__main__":
    nums = [3, 6, 7, 11]
    h = 8
    result = minimumRateToEatBananas(nums, h)
    print(f"The minimum eating speed to finish in {h} hours is: {result}")

    nums = [30, 11, 23, 4, 20]
    h = 5
    result = minimumRateToEatBananas(nums, h)
    print(f"The minimum eating speed to finish in {h} hours is: {result}")

    nums = [30, 11, 23, 4, 20]
    h = 6
    result = minimumRateToEatBananas(nums, h)
    print(f"The minimum eating speed to finish in {h} hours is: {result}")