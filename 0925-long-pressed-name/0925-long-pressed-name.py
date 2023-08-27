class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        """
        "alex"
            ^  
        
        "aaleelx"
             ^
              
      "zlexya"
        ^
      "aazlllllllllllllleexxxxxxxxxxxxxxxya"
       ^
        """
        n = 0
        t = 0
        
        if typed[0] != name[0]:
            return False
     
        while t < len(typed) and n < len(name):
            if name[n] == typed[t]:
                n += 1
                t += 1
            
            while t < len(typed) and n < len(name) and name[n] != typed[t]:
                if typed[t] != name[n -1]:
                    return False
                t += 1
                
        while t < len(typed):
            if typed[t] != name[len(name) - 1]:
                return False
            t += 1
        
        if t < len(typed) or n < len(name):
            return False
        
        return True
        
    
    
 