class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        combos = [0 for _ in range(n + 1)]
        nums.insert(0,0)
        combos[1] = nums[1]
        
        for house in range(1,len(nums)):
            combos[house] = max(combos[house - 1] , nums[house] + combos[house - 2])
        return max(combos[-1],combos[-2])