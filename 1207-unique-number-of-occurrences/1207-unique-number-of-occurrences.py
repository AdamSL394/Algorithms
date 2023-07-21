class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = {}
        uniqueCount = set()
        
        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for k,v in count.items():
            if v in uniqueCount:
                return False
            uniqueCount.add(v)
        
        return True