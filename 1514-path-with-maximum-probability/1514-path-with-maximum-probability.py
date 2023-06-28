from heapq import heappop, heappush, heapify

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        dic = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]           
            dic[src].append((dst , succProb[i]))
            dic[dst].append((src , succProb[i]))
        
        pq = [(-1, start)] # 

        seen = set() # 0 , 1

        
        while pq:
            prob, node = heapq.heappop(pq) #( 0 ,1 ) ( 1 , -.5)
            seen.add(node)
            
            if node == end:
                return prob * -1
            
            for node , currProb  in dic[node]: # (1, .5) (2, 0.5)
                if node not in seen:
                    heapq.heappush(pq,( prob * currProb, node))# (1 , -.5) , (2, -.2)
        
        return 0.0