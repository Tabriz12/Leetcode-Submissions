from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = deque()

        max_area = 0

        for idx, height in enumerate(heights):

            new_idx = idx

            while stack and height < stack[-1][1]:

                
                (top_idx, top_h) = stack.pop()

                new_idx = top_idx

                max_area = max(max_area, (idx-top_idx) * top_h)
            
            stack.append((new_idx, height))
            

        

        while stack:

            (top_idx, top_h)  = stack.pop()

            max_area = max(max_area, (len(heights)-top_idx) * top_h)
        

        return max_area





        



        
                




        
