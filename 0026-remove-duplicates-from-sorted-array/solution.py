class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        shift = 0
        for i in range(1, len(nums)):
            if nums[i-shift] == nums[i-shift-1]:
                nums.pop(i-shift)
                shift+=1


        
