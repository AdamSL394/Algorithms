class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        
        result = 0
        key = None
        
        if ruleKey == "type":
            key = 0
        if ruleKey == "color":
            key = 1
        if ruleKey == "name":
            key = 2
        
        for item in items:
            if item[key] == ruleValue:
                result += 1
        
        
        
        return result 