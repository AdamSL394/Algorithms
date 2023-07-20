class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        N = len(asteroids)
        stack = []
        
        for stone in asteroids:
            
            stack.append(stone)
            
            if stone > 0:
                continue
            
            while len(stack) >= 2:
                current = stack[-1]
                previous = stack[-2]

                if previous < 0:
                    break
                    
                if previous > 0 and current > 0:
                    break
                    
                if abs(current) == abs(previous):
                    stack.pop()
                    stack.pop()
                    continue
 
                if abs(previous) > abs(current):
                    stack.pop()

            
               
                    
                if abs(previous) < abs(current):
                    stack.pop(-2)
                
        return stack
    
