class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        remainingColors = colors
#         colorsLeft = list(colors)
        
#         aliceCanPlay = True
#         bobCanPlay = True
            
#         turn = 'A'

#         def alice(remainingColors):
#             if len(remainingColors) < 3:
#                 return False
            
#             for letter in range(1, len(remainingColors)): 
#                 if letter + 1 < len(remainingColors):
#                     if remainingColors[letter - 1] == "A" and remainingColors[letter] == "A" and remainingColors[letter + 1] == "A":
#                         remainingColors[letter] = "_"
#                         return True
#             return False
            
            
#         def bob(remainingColors):
#             if len(remainingColors) < 3:
#                 return False
            
#             for letter in range(1, len(remainingColors)): 
#                 if letter + 1 < len(remainingColors):
#                     if remainingColors[letter - 1] == "B" and remainingColors[letter] == "B" and remainingColors[letter + 1] == "B":
#                         remainingColors[letter] = "_"
#                         return True
#             return False
            
#         while aliceCanPlay and bobCanPlay:
#             if turn == 'A':
#                 movedA= alice(colorsLeft)
#                 if not movedA:
#                     return False
#                 else:
#                     turn = 'B'
#             if turn == 'B':
#                 movedB = bob(colorsLeft)
#                 if not movedB:
#                     return True
#                 else:
#                     turn = 'A'
        a = 0
        b = 0
        for letter in range(1, len(remainingColors)): 
            if letter + 1 < len(remainingColors):
                if remainingColors[letter - 1] == "A" and remainingColors[letter] == "A" and remainingColors[letter + 1] == "A":
                    a += 1
                if remainingColors[letter - 1] == "B" and remainingColors[letter] == "B" and remainingColors[letter + 1] == "B":
                    b +=1
        print("A =",a,"B = ",b)
        if a > b:
            return True
        return False
        '''
        "ABBAAA"   
        
        '''