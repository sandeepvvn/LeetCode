from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array in-place.
        
        Args:
            nums1: Array with length m+n, first m elements are valid, rest are 0
            m: Number of valid elements in nums1
            nums2: Sorted array with n elements
            n: Number of elements in nums2
        
        The function modifies nums1 in-place and does not return anything.
        """
        
        # Process each element from nums2 that needs to be merged
        for i in range(n):
            # Find the correct position in nums1 to insert the current nums2 element
            for j in range(len(nums1)):
                # Insert if nums2[0] is <= nums1[j] (found correct position)
                # OR if we've reached beyond the valid merged elements (j >= i+m)
                # where i+m represents the end of merged elements so far
                if nums2[0] <= nums1[j] or j >= i+m:
                    # Insert the element from nums2 at position j
                    nums1.insert(j, nums2[0])
                    # Remove the element from nums2 since it's been merged
                    nums2.pop(0)
                    break
            
            # Remove the last element (which was a placeholder 0) to maintain
            # the correct length of m+n after insertion
            nums1.pop()


