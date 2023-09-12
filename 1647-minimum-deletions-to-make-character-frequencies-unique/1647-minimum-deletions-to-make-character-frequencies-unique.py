class Solution:
    def minDeletions(self, s: str) -> int:

        seen_nums = set()  
        number_values = Counter(s) #
        count = 0  

        for k,v in number_values.items():
            if v not in seen_nums:
                seen_nums.add(v)
            else:
                dec_num_value = v 
                while dec_num_value in seen_nums:
                    dec_num_value -= 1
                    count += 1
                    if dec_num_value == 0:
                        break
                seen_nums.add(dec_num_value)
                    
                    
        return count