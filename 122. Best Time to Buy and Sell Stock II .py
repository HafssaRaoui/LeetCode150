class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        lo = prices[0]
        hi = prices[0]
        profit = 0 
        n = len(prices)

        while i < n - 1:
            # Look for our buying point
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            lo = prices[i]

            # Look for selling point
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            hi = prices[i]

            profit += hi - lo

        return profit





        