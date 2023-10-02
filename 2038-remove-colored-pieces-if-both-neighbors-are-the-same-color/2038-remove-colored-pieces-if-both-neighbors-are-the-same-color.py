class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        for letter in range(1, len(colors)): 
            if letter + 1 < len(colors):
                if colors[letter - 1] == colors[letter] ==  colors[letter + 1] :
                    if colors[letter] == "A":
                        a +=1
                    else:
                        b += 1
                

        if a > b:
            return True
        return False
