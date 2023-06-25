class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_list = sorted(nums)
        res = []
        count = 0
        B = 0
        for num in range(len(nums)):
            A = num
            B = num
            while A < len(nums):
                if nums[A] < nums[num]:
                    count += 1
                A += 1
            while B > -1:
                if nums[B] < nums[num]:
                    count += 1
                B -= 1
            res.append(count)
            count = 0
        return res