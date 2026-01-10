class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Process from right to left
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If all digits were 9, add a leading 1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
