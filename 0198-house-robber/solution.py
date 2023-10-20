class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<3: return max(nums)
        profs = [nums[0], nums[1], nums[0]+nums[2]]
        if len(nums)==3: return(max(profs))
        for idx in range(3, len(nums)):
            profs.append(max(profs[idx-2], profs[idx-3])+nums[idx])
        
        return(max(profs[-1], profs[-2]))
        



        
        
        
        
