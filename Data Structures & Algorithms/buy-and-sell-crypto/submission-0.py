class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        i = 0
        j = 1

        while j< len(prices):
            if prices[j] > prices[i]:
                # we are making some profit
                n = prices[j] - prices[i]
                if n > maxprofit:
                    maxprofit = n
            #otherwise price at j is new low point
            else :
                i = j
            j += 1


        return maxprofit