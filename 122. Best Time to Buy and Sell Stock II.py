class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只要后面比前面大，就在前一天买入，第二天卖出
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = profit + prices[right] - prices[left]
            left = left + 1
            right = right + 1
        return profit
