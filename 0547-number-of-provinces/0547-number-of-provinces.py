class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        G = {}
        
        for node in range(len(isConnected)):
            level = node + 1
            for i,v in enumerate(isConnected[node]):
                if level not in G:
                    G[level] = []
                if v == 1:
                    G[level].append(i + 1)
                    
        stack = []
        seen = set()
        count = 0

        for i in range(len(isConnected[0])):
            stack.append(i + 1)
            if i + 1 not in seen:
                while stack:
                    node = stack.pop(0)
                    seen.add(node)
                    for nei in range(len(G[node])):
                        if (G[node])[nei] not in seen:
                            stack.append((G[node])[nei])
                count += 1
        

        return count