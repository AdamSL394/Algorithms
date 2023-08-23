class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # [0,0,0,1,0]
        houses = [0 for _ in range(N + 1)]
        houses[-2] = nums[-1]

        for cash in range(N - 2, -1, -1):
            houses[cash] = max(houses[cash + 1], nums[cash] + houses[cash + 2])
        
        return max(houses[0],houses[-1])