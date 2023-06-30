class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitsum = 0
        stringOfNums = (''.join(str(x) for x in nums))
        elementSum = sum(nums)
        
        print(elementSum,stringOfNums)
        
        for number in stringOfNums:
            digitsum += int(number)
            
        return (elementSum - digitsum)