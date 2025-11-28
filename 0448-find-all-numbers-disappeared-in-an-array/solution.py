class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ints = [i for i in range(1, len(nums) + 1)]
        
        for el in nums:
            ints[el-1] = 0
        
        return [i for i in ints if i != 0]
            
