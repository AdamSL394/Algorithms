class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        111] Two bit
        110] One bit
        100
        
        """
        if len(bits) == 1:
            return True
        
        
        if bits[-1] == 0 and bits [-2] == 0:
            return True
        
        if len(bits) == 2 and bits [-2] == 1:
            return False
        
        if bits[-3] == 0:
            return False
        
    
        if len(bits) == 3:
            if bits[-1] == 1 and bits [-2] == 1:
                return False
            else:
                return True
            
        N = len(bits)
        zero_count = 0 # 1
        ones_count = 0 # 1
        flag = False # True, False
        for v in range(N):
            if bits[v] == 1:
                ones_count += 1
                
            if bits[v] == 0:
                zero_count += 1
                
            if zero_count == 2:
                flag = True
                zero_count = 0
                
            if ones_count == 2:
                flag = False
                zero_count = 0
                ones_count = 0
                
            if ones_count == 1 and zero_count == 1:
                flag = False
                zero_count = 0
                ones_count = 0
            if zero_count == 1 and ones_count == 0:
                flag = True
                zero_count = 0
                ones_count = 0
                
            
        return flag