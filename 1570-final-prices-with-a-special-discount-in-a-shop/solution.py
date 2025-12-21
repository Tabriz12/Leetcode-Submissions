from collections import deque

class Solution:

    


    def finalPrices(self, prices: List[int]) -> List[int]:

        res = [el for el in prices]

        stack = deque()

        stack.appendleft(prices[-1])

        for i in range(len(prices)-2, -1, -1):
            
            while stack:
                
                stack_top  = stack.popleft()

                if prices[i] >= stack_top:

                    stack.appendleft(stack_top)
                    stack.appendleft(prices[i])
                    res[i] -= stack_top
                    break
                    
            if not stack: stack.appendleft(prices[i])


        return res

