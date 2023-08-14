from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num)
        heapify(heap)
        
        res = 0
        test = len(nums) - k
        for v in range(test + 1):
            res = heappop(heap)
        return (res)
