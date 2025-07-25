class Solution:
    def nextPermutation(self, nums):
        n=len(nums)
        ind=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            return nums.reverse()
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        nums[ind+1:]=reversed(nums[ind+1:])
        return nums
# ### Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.nextPermutation(nums)
    print(f"Next permutation of {nums} is: {result}")

    nums = [3, 2, 1]
    result = solution.nextPermutation(nums)
    print(f"Next permutation of {nums} is: {result}")

    nums = [1, 1, 5]
    result = solution.nextPermutation(nums)
    print(f"Next permutation of {nums} is: {result}")