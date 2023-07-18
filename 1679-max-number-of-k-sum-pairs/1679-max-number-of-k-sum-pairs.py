class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        inorder = sorted(nums)
        
        l = 0
        r = len(nums) - 1
        operations = 0
        
        while l < r:
            if inorder[l] + inorder[r] == k:
                operations += 1
                l += 1
                r -= 1
            if inorder[l] + inorder[r] >  k:
                r -= 1
            if inorder[l] + inorder[r] <  k:
                l += 1
        
        return operations