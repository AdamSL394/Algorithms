class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        numbers = []
        words = []
        
        for word in logs:
            if word.split()[1].isdigit():
                numbers.append(word)
            else:
                words.append(word.split())
        
        words.sort(key = lambda x: x[0])          
        words.sort(key = lambda x: x[1:])


        res = []
        
        for word in words:
            res.append(' '.join(word))
        
        return res + numbers

        
        
        
        
        
        """
        
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        
        "let1 art can", "let3 art zero"
        
        
        """