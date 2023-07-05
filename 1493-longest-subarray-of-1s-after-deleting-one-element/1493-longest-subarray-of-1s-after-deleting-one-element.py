class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        a = 0
        b = 0
        
        res = 0
        zeros = 1
        count = 0
        
        while  a < N - 1 and nums[a] == 0:
                a += 1
        b = a
        
        if a == N - 1:
            return 0

        while b < N:
            while nums[a] < b and zeros <= -1:
                if nums[a] == 0:
                    zeros += 1
                if nums[a] == 1:
                    count -= 1
                a += 1
            while zeros >= 0 and b < N:
                if nums[b] == 0:
                    zeros -= 1
                if nums[b] == 1:
                    count += 1
                b += 1
            res = max(res, count)
            
        if res == N:
            return N - 1
        
        return res
            