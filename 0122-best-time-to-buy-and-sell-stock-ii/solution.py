class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prof = 0

        buy = prices[0]

        for idx in range(1, len(prices)):
            
            if prices[idx] > buy:
                prof += (prices[idx] - buy)
                
            buy = prices[idx]

        return prof
