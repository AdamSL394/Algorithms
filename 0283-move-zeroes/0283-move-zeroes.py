class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        l = 0
        r = 0
        
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
      
        return nums