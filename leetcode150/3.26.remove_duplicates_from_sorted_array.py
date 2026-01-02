from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.
        
        Args:
            nums: Sorted array of integers to modify in-place
        
        Returns:
            The number of unique elements (k)
        
        The first k elements of nums will contain unique numbers in sorted order.
        """
        
        # Get unique elements and sort them (maintains order since input is sorted)
        nums2 = list(set(nums))
        nums2 = sorted(nums2)
        nums2_len = len(nums2)
        
        # Update nums array with unique values
        for i in range(nums2_len):
            if nums[i] != nums2[i]:
                nums[i] = nums2[i]
        
        # Clean up remaining elements
        nums[nums2_len:] = [0]
        
        return nums2_len
