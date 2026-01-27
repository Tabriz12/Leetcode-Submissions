from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:


        dic = Counter(nums)

        ops =0

        sorted_keys = sorted(list(dic.keys()))

        for i, n in enumerate(sorted_keys):

            ops+= i * dic[n]
        
        return ops







        
