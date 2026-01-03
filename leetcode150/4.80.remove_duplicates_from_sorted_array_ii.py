from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place, allowing at most 2 occurrences.
        
        Args:
            nums: Sorted array of integers to modify in-place
        
        Returns:
            The number of elements after removing duplicates (k)
        """
        k = 0  # Counter for consecutive duplicates
        i = 1  # Current index
        m = len(nums)  # Array length
        
        while i < m:
            if nums[i-1] == nums[i]:
                if k == 0:
                    # First duplicate, allow it
                    k = 1
                    i += 1
                else:
                    # More than 2 occurrences, remove it
                    nums.pop(i)
                    m -= 1
            else:
                # Different element, reset counter
                k = 0
                i += 1
           
        return m
