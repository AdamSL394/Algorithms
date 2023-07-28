class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                mid_value = arr[mid]

                if mid_value == target:
                    return mid
                elif mid_value < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return mid + 1 if target > arr[mid] else mid

        return binary_search(nums, target)