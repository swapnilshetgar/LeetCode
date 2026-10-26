class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step 1: Find the first decreasing element from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If found, find the next greater element
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the remaining elements
        nums[i + 1:] = reversed(nums[i + 1:])