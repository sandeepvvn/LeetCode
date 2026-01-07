class Solution:
    def reverseWords(self, s: str) -> str:
        # Split collapses multiple spaces and drops leading/trailing spaces
        words = s.split()
        # Reverse in place for clarity
        words.reverse()
        return " ".join(words)