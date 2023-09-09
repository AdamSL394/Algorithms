class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        order = []
        for x, y in points:
            distance = (x - 0)**2 + (y - 0)**2
            order.append((distance,(x,y)))
        
        ordered_distance = sorted(order)
        
        total = k
        res = []
        for pairs in ordered_distance:
            if total == 0:
                return res
            
            paried_coordinates = list(pairs[1])
            res.append(paried_coordinates)
            total -= 1

        return res