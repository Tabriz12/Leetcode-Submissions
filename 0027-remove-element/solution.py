class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        shift=0
        for i in range(len(nums)):
            if (nums[i-shift]==val):
                nums.pop(i-shift)
                shift+=1
        
