class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        
        majority = N / 3
        
        dic = {}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else: 
                dic[num] += 1
        res = []
        for k,v in dic.items():
            if float(v) > majority:
                res.append(k)
                
        return (res)
                