class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r = 0, 0

        jump = 0

        while r < len(nums)-1:

            furt = 0

            for i in range(l, r+1):

                furt = max(furt, nums[i] + i)

            l = r+1    
            r = furt
            jump+=1
        
        return jump




        
