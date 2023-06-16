class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 2 or  len(nums) == 3 :
        #     return nums.index(max(nums))
        
        def binarySearch(arr, l , r):
            
            while l <= r:
                
                mid = l + ((r - l) // 2)
            
                if mid > 0 and arr[mid] < arr[mid - 1] :
                    r = mid - 1
                
                elif mid < len(arr)- 1 and arr[mid] < arr[mid + 1] : 
                    l = mid + 1
                else:
                    return mid
                    
                
                     
            
        return binarySearch(nums, 0, len(nums) -1)