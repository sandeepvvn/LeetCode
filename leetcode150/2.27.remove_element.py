from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place.
        
        Args:
            nums: Array of integers to modify in-place
            val: Value to remove from the array
        
        Returns:
            The number of elements in nums which are not equal to val (k)
        
        The function modifies nums such that the first k elements contain
        all elements not equal to val. The remaining elements are not important.
        """
        
        # Start from the beginning of the array
        i = 0
        
        # Iterate through the array
        while i < len(nums):
            # If current element equals val, remove it
            # Note: pop(i) shifts all elements after i to the left,
            # so we don't increment i in this case
            if nums[i] == val:
                nums.pop(i)
            else:
                # Only increment i if we didn't remove an element
                # This ensures we check the new element at position i
                i += 1
        
        # Return the length of the modified array (number of elements != val)
        return len(nums)