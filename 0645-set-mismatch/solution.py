class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        expected_sum = len(nums) * (len(nums) + 1) // 2
        current_sum = sum(nums)

        missing = list(set([i for i in range(1, len(nums)+1)]).difference(set(nums)))[0]

        return [missing - (expected_sum - current_sum), missing]


            

                

        
