#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        len_p = len(prices)

        l = prices[0]
        for i in range(1, len_p): # O(n)
            r = prices[i]
            profit = max(profit, r - l)
            if r < l:
                l = r
        return profit

# @lc code=end

