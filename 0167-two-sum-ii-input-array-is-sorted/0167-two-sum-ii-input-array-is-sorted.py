class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        a = 0
        b = len(numbers) - 1
        result = []
            
        while a < b:
            print(numbers[a] + numbers[b])
            if numbers[a] + numbers[b] == target:
                result.append(a + 1)
                result.append(b + 1)
                return result
            if target < (numbers[a] + numbers[b]):
                b -= 1
            if target > (numbers[a] + numbers[b]):
                a += 1
        return result
                    
                    