from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(list(set(nums)))

        counter = Counter(nums)

        final = {}

        greater = 0

        for el in sorted_nums:
            great  = greater
            final[el] = great
            greater += counter[el]
        
        return [final[n] for n in nums]


        


        
        
