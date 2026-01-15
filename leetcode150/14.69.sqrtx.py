class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        
        # Find the largest integer whose square is <= x
        while i * i <= x:
            i += 1
        
        return i - 1
