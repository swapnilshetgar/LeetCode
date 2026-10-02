class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find a character whose frequency is less than k
        for ch in freq:
            if freq[ch] < k:
                # Split around that character
                parts = s.split(ch)

                # Find the maximum valid substring
                return max(
                    self.longestSubstring(part, k)
                    for part in parts
                )

        # Every character appears at least k times
        return len(s)