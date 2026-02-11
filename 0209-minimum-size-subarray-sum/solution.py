import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        mix = 0

        leng = 0

        summ = 0

        res = sys.maxsize

        for el in nums:

            summ += el
            leng+=1

            if summ >= target:

                while summ - nums[mix] >= target:

                    summ -= nums[mix]

                    mix+=1
                    leng-=1
                
                res = min(res, leng)

            if res == 1:
                return res
        

        return 0 if res ==sys.maxsize else res

        
