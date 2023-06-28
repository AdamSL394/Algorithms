class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x > 2147483648 or x < -2147483648:
            return 0
        
        if x < 0:
            pos = x * -1
            corrected = self.checkPrependZero((str(pos)[::-1]))
            return (int(corrected) * - 1)
        if x > 0:
            checked = self.checkPrependZero((str(x)[::-1]))
            return (int(checked))
        
        
    def checkPrependZero(self, num):
        if int(num) > 2147483648 or int(num) < -2147483648:
            return 0
        else:
            return num