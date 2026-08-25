class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
            
    
        seen = {}       # stores last index of each character
        left = 0        # left boundary of window
        max_length = 0

        for right, char in enumerate(s):
            # if char already seen and inside current window
            if char in seen and seen[char] >= left:
                left = seen[char] + 1   # move left pointer
            seen[char] = right          # update last seen index
            max_length = max(max_length, right - left + 1)

        return max_length

