class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        candidate = 0
        count = 0
        
        for i in range(N):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                
        
        return candidate