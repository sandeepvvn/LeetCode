from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element that appears more than n/2 times.
        
        Args:
            nums: Array of integers with a guaranteed majority element
        
        Returns:
            The majority element
        """
        count_dict = {}
        
        # Count occurrences of each element
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Return element with maximum count
        return max(count_dict, key=count_dict.get)
