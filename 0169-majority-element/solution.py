from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        babies = Counter(nums)
        maximus = 0
        kill_count = 0
        for k, v in babies.items():

            if v > kill_count:
                kill_count=v
                maximus = k
        
        return maximus


        
