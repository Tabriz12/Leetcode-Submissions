class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic_dic = {}

        
        for i, el in enumerate(nums):

            diff = target - el

            if el in dic_dic.keys():
                return [dic_dic[el], i]
            
            else:
                dic_dic[diff] = i
            
            
