class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        if len(s) % 2 != 0:
            return False

        
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")

     
        return len(s) == 0