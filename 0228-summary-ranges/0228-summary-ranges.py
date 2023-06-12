class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return 
        A = 0
        B = 1
        start = None 
        result = [] 
        begin = True
         
        while B <= len(nums) - 1:
            if nums[B] == (nums[A] + 1):
                if begin:
                    start = nums[A]
                    begin = False
            if nums[B] != (nums[A] + 1):
                if start != None:
                    result.append(str(start) + "->" + str(nums[A]))
                    begin = True
                    start = None
                else:
                    result.append(str(nums[A])) 
            B += 1
            A += 1
            
               
                
            
        if begin:
            result.append(str(nums[-1]))
        if begin == False:
            result.append(str(start) + "->" + str(nums[A]))
            
        return result 