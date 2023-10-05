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
                
        count = 0  
        print(candidate)
        for j in range(N):
            if nums[j] == candidate:
                count += 1
                
        if count > N / 2:
            return candidate