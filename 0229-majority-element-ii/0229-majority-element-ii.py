class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        base = int(len(nums)/3)
        res = []
        
        for k,v in freq.items():
            if v > base:
                res.append(k)
        return res