class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1

        max_val = 0
        
        while left<right:

            area = (right-left) * min(height[right], height[left])

            max_val = max(max_val, area)

            if height[right] < height[left]: right-=1
            else: left+=1
        
        return max_val

            

            



        
