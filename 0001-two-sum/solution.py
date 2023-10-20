class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = []

        for idx, el in enumerate(nums):
            if el in needed: return [idx, needed.index(el)]
            else: needed.append(target-el)


        
