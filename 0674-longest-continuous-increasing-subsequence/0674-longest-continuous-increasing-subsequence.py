class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        N = len(nums)
        count = 1
        res = 1
        prev = nums[0]
        
        for i in range(1,N):
            if nums[i] > prev:
                count += 1
            else:
                count = 1
            prev = nums[i]
            res = max(res,count)
        return (res)
                
            