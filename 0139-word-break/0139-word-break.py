class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache 
        def recursion(s):
            if len(s) == 0:
                return True
            for word in wordDict:
                if s.find(word) > -1:
                    if s.index(word) == 0:
                        newWord = s[len(word):]
                        if recursion(s[len(word):]):
                            return True
                else:
                    continue
                    
            return False
        
        return recursion(s)
        