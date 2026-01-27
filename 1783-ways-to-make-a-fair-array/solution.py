class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        odd_m = 0
        even_m = 0

        odd_sum = sum([n for i,n in enumerate(nums) if i%2 == 1])
        even_sum = sum(nums) - odd_sum

        res = 0

        for i, n in enumerate(nums):

            
            if (i % 2 == 0 and
                even_sum - even_m - n + odd_m== odd_sum - odd_m + even_m):
                res+=1


            elif (i % 2 == 1 and
                even_sum - even_m + odd_m == odd_sum - odd_m - n + even_m ):
                res+=1

            if i % 2 == 0:

                even_m +=n
            
            else:
                odd_m +=n
        
        return res

                

