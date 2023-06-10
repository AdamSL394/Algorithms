class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        fequencyCount = [0 for i in range(102)]
        totalCount = 0
        
        for num in nums:
            fequencyCount[num] += 1

        for count in fequencyCount:
            totalCount += ((count) * (count - 1))/2
        return(int(totalCount))
