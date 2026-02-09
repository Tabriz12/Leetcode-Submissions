class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        buy = True

        prof = 0

        if len(prices) < 2: return prof

        for i in range(len(prices)-1):

            if buy:

                if prices[i] < prices[i+1]:

                    prof-=prices[i]
                    buy = False
            
            else:

                if prices[i] >= prices[i+1]:

                    prof+=prices[i]
                    buy = True
        
        if buy == False:
            prof+=prices[-1]
        
        return prof

            
        
