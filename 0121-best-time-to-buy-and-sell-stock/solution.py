import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        anchor = sys.maxsize
        max_profit = 0

        for i in prices:

            if i < anchor:

                anchor = i
            
            else:

                max_profit = max(max_profit, i - anchor)

        return max_profit
        



        
            

        
