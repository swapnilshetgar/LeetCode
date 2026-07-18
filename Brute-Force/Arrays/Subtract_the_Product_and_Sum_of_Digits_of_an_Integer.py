class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        m=1
        for i in str(n):
            s=s+int(i)
            m=m*int(i)
        return m-s