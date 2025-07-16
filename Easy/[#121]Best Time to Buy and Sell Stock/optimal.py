class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for i in prices:
            if min>i:
                min=i
            elif profit<(i-min):
                profit=(i-min)
        return profit