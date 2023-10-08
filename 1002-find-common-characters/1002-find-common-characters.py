class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        word_counter = []
        INF = 10**4
        for word in words:
            word_counter.append(Counter(word))
            
        char_list  = ''.join(words)
        freq_count = {}
        found_in_all = len(words)
        
        for c in char_list:
            for k, count in enumerate(word_counter):
                if c in count:
                    found_in_all -= 1
            if found_in_all == 0:
                freq_count[c] = INF
            found_in_all = len(words)
            
        for k,v in freq_count.items():
            for j, count in enumerate(word_counter):
                if k in count:
                    if count[k] < freq_count[k]:
                        freq_count[k] = count[k]
                        
        res = []
        
        for key,value in freq_count.items():
            char_count = value
            while char_count > 0:
                res.append(key)
                char_count -= 1
                
        return res
                
                