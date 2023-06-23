class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        N = len(nums)
        
        res = 0
        
        while l != r:
            minHeight = min(nums[l], nums[r])
            N -= 1 
            
            if minHeight * N > res:
                res = minHeight * N
            
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return(res)
        