class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums: return nums

        if len(nums) == 1: return [str(nums[0])]


        leng = 0

        res = []

        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]-1:
                leng += 1
            else:
                if leng: res.append("{}->{}".format(nums[idx-leng], nums[idx]))
                else: res.append(str(nums[idx]))
                leng = 0
        
        if leng: res.append("{}->{}".format(nums[idx+1-leng], nums[idx+1]))
        else: res.append(str(nums[idx+1]))
        return res




        

            
        
