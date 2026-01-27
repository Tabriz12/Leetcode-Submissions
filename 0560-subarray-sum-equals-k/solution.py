class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        summy = 0
        dic = {summy: 1}

        res = 0


        for i, n in enumerate(nums):

            summy += n
            if summy - k in dic:
                res+=dic[summy-k]

            
            if summy in dic:
                dic[summy] += 1
            
            else: dic[summy] = 1
        
        return res
        


        


        
