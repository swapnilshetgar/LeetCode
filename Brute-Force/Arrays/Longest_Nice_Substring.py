class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""

        for i in range(len(s)):
            ch = s[i]

            # If both lowercase and uppercase are not present,
            # this character cannot be part of a nice substring.
            if ch.lower() not in s or ch.upper() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        # Every character has both cases
        return s