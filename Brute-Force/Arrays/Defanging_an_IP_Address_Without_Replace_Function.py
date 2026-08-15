class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=""
        for i in address:
            if i!='.':
                ans=ans+i
            else:
                ans=ans+"[.]"
        return ans