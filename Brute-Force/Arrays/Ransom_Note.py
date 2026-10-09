class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, "", 1)

        return True