class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dirty_deeds = {}

        for idx, num in enumerate(nums):

            if target - num in dirty_deeds:

                return [dirty_deeds[target-num], idx]
            
            else:

                dirty_deeds[num] = idx


