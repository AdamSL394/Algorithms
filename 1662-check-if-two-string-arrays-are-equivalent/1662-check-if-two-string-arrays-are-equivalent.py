class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        concat1 = (''.join(str(x) for x in word1))
        concat2 = (''.join(str(x) for x in word2))
        
        return concat1 == concat2