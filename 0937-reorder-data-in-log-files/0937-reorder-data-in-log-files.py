class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        numbers = []
        words = []
        
        for word in logs:
            if word.split()[1].isdigit():
                numbers.append(word)
            else:
                words.append(word)
        
        words.sort(key = lambda x: x.split()[0])          
        words.sort(key = lambda x: x.split()[1:])

        
        return words + numbers

        
        
        
        
        
        """
        
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        
        "let1 art can", "let3 art zero"
        
        
        """