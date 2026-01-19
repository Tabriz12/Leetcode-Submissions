from heapq import heapify, heappop
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        heapify(nums)

        
        while nums and nums[0] < 1:
            
            heappop(nums)
        
        if not nums: return 1

        cnt = 0
        while nums:

            pop = heappop(nums)
            if cnt == pop or pop == cnt+1:
                cnt = pop
            
            else: return cnt+1
        
        return cnt + 1
        

