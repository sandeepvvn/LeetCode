class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert to string and compare with reverse
        str_x = str(x)
        reverse_x = "".join(reversed(str_x))
        x_rev = int(reverse_x)
        
        return x == x_rev
