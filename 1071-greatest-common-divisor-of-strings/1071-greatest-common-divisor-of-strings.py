class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        res = ''
        def gcd(k):
            
            if (len(str2) % len(k) == 0 and len(str1) % len(k) == 0):
                print(str2[:len(k)] * (len(str2) // len(k)) == str2)
                if (str2[:len(k)] * (len(str1) // len(k))) == str1 and str2[:len(k)] * (len(str2) // len(k)) == str2:
                    print(str2[:len(k)])
                    return str2[:len(k)]
                else:
                    return ""
            else:
                return
            
            
        
        
        for k in range(len(str2)-1,-1,-1):
                if gcd(str2[k:]):
                    res = gcd(str2[k:])
        
        return res
            