from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        stack = deque([[0, heights[0]]])

        maxs = 0

        for i, h in enumerate(heights[1:], 1):

            temp  = i

            while stack and h < stack[-1][-1]:

                top_i, top_h = stack.pop()
                temp = top_i
                
                maxs = max(maxs, (i-top_i)*top_h)
            

            stack.append([temp, h])
        

        tot = len(heights)
        
        if stack:

            while stack:

                top_i, top_h = stack.pop()
                maxs = max(maxs, (tot-top_i)*top_h)
        
        return max(maxs, heights[0])






                










        
