class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        loc = -1
        n= len(needle)
        if len(haystack) == n:
            if haystack != needle:
                return -1
            else:
                return 0
        else:
            for i in range(len(haystack) - n+1):

                if needle == haystack[i:i+n]:
                    return i
        
            return -1
        
