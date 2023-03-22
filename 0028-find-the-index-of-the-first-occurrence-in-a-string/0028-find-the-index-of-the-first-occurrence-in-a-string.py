class Solution:
    # "aabaaabaaac"
    #       ^
    #      ^
    # "aabaaac
    #  ^ 


    # "aaaabbbababb"
    #        ^
    #      ^
    # "baa"
    #  ^
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1
                    
