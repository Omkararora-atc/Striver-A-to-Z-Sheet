class Solution:
    def numberOfInversions(self, nums):
        self.count=0
        l,h=0,len(nums)-1
        self.merge_sort(nums,l,h)
        return self.count
    def merge_sort(self,nums,l,h):
        if l<h:
            mid=(l+h)//2
            self.merge_sort(nums,l,mid)
            self.merge_sort(nums,mid+1,h)
            self.merge(nums,l,mid,h)
    def merge(self,nums,l,mid,h):
        low=nums[l:mid+1]
        high=nums[mid+1:h+1]
        m=len(low)
        n=len(high)
        i,j,k=0,0,l
        while i<m and j<n:
            if low[i]<=high[j]:
                nums[k]=low[i]
                i+=1
            else:
                nums[k]=high[j]
                j+=1
                self.count+=len(low)-i
            k+=1
        while i < m:
            nums[k] = low[i]
            i += 1
            k += 1

        while j < n:
            nums[k] = high[j]
            j += 1
            k += 1
# ### Example usage:
if __name__ == "__main__":
    arr = [7, 5, 6, 4]
    solution = Solution()
    inversions = solution.numberOfInversions(arr)
    print("Number of inversions:", inversions)
    arr=[2, 3, 7, 1, 3, 5]
    inversions = solution.numberOfInversions(arr)
    print("Number of inversions:", inversions)
