class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0
        sell = prices[-1]
        for prc in prices[::-1][1:]:
            max_prof = max(sell-prc, max_prof)
            sell = max(sell, prc)
            
        return max_prof
            

        
        
    


        


        
