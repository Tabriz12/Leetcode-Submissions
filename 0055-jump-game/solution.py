class Solution:
    def canJump(self, nums: List[int]) -> bool:

        tot = len(nums)-1

        max_covered = nums[0]

        for dist, el in enumerate(nums, 0):

            if dist > max_covered: return False

            if dist+el >= tot: return True
            
            else: max_covered = max(max_covered, dist+el)


            
        



        
