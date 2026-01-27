class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        find = sum(nums)%p

        if not find: return find

        rolsum = 0

        dic = {0:-1}

        minlen = len(nums)

        for i, n in enumerate(nums):

            rolsum = (rolsum + n) % p

            dic[rolsum] = i


            remaining = (rolsum - find + p) % p

            if remaining in dic:

                minlen = min(minlen, i-dic[remaining])
        
        return minlen if minlen<len(nums) else -1
            
            
            







