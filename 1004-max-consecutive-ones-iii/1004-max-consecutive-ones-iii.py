class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        
        k = 3
        count = 5
       
        
        [1,1,1,1,0,0,0,1,1,1,1,0,1,1]
                   l
                                   r  
         
        [1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
         l
         r
        """
        nums.insert(0,1)
        nums.append(1)
        l = 0
        N = len(nums)
        res = 0
        
        for r in range(N):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                res = max(res, len(nums[l+1:r]))
            while k < 0:
                l += 1
                if nums[l] == 0:
                    k +=  1
                    
        if k > -1:
            res = max(res, len(nums[l+1:r]))
        return res
                
                