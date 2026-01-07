class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing spaces
        s = s.strip()
        
        # Split by spaces and get the last word
        words = s.split(" ")
        
        return len(words[-1])
