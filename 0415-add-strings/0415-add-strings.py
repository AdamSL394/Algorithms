class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num = 0
        num_2 = 0
        sys.set_int_max_str_digits(10000)
        for i in num1:
            num = num * 10 + (ord(i) - ord('0'))
        
        for i in num2:
            num_2 = num_2 * 10 + (ord(i) - ord('0'))
        
        return str(((num + num_2) ))
        