import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        
        preSum = 1

        for v in range(len(nums)):
            res[v] = preSum
            preSum *= nums[v]
        
        postSum = 1 
        
        for v in range(len(nums) - 1, -1, -1):
            res[v] = postSum * res[v] 
            postSum *= nums[v]
        
        return res
        
        