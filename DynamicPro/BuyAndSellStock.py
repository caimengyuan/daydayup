'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        sold = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        rest = [0 for _ in range(n)]
        hold[0] = -prices[0]
        for i in range(1, n):
            sold[i] = max(hold[i-1] + prices[i], sold[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            rest[i] = max(sold[i-1], rest[i-1])
        return sold[-1]