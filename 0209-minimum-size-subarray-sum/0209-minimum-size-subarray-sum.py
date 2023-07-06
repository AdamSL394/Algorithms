class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Inf = 10**20
        N = len(nums)
        best = Inf
        l = 0
        total = 0
        
        for r in range(N):
            total += nums[r]
            
            while total >= target:
                best = min(best, (r - l) + 1)
                total -= nums[l]
                l += 1
            
            
            
        if best >= Inf:
            return 0
        return best