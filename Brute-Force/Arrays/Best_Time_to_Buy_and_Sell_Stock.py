class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit=prices[0]
        profit=0

        for i in range(1,len(prices)):
            current_profit=prices[i]-min_profit

            if current_profit>profit:
                profit=current_profit
            min_profit=min(min_profit,prices[i])

        return profit