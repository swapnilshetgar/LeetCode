class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # If the difference exceeds 1, shrink the window from the left
            while nums[right] - nums[left] > 1:
                left += 1

            # Only update the max length if the difference is exactly 1
            if nums[right] - nums[left] == 1:
                max_length = max(max_length, right - left + 1)
                
        return max_length