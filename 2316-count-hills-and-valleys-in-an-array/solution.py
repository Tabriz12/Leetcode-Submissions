class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        left = nums[0]
        cnt = 0
        for n in range(1, len(nums[1:]), 1):


            if nums[n] != nums[n-1]:
                left = nums[n-1]
            
            if (nums[n] > left and nums[n] > nums[n+1]) or (nums[n] < left and nums[n] < nums[n+1]):
                cnt+=1
        
        return cnt





        
