class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        Inf = -10**5
        l = 0
        count = Inf
        total = Inf

        if N == 1:
            return float(nums[0])
        
        
        count = float(sum(nums[l: k]) / k)
        if count > total:
                total = count
                
        for r in range(k ,N):
            add =  nums[r] / k
            count += add
            remove = nums[l] / k
            count -= remove
            l += 1
            if count > total:
                total = count

        return total