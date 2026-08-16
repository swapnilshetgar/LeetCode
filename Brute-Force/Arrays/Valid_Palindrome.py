class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
                
        
        ans=""
        boolean=True
        for i in s.lower():
            if i.isalnum():
                ans+=i

        if ans==ans[::-1]:
            return  boolean
            
        else:
            boolean=False
            return  boolean