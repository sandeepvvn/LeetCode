from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right by k steps.
        
        Args:
            nums: Array to rotate (modified in-place)
            k: Number of steps to rotate
        """
        n = len(nums)
        k = k % n
        
        # Rotate: last k elements go to front, rest follow
        nums[:] = nums[-k:] + nums[:-k]
