class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        for letter in range(1, len(colors)): 
            if letter + 1 < len(colors):
                if colors[letter - 1] == "A" and colors[letter] == "A" and colors[letter + 1] == "A":
                    a += 1
                if colors[letter - 1] == "B" and colors[letter] == "B" and colors[letter + 1] == "B":
                    b +=1

        if a > b:
            return True
        return False
