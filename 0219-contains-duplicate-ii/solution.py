class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        start = 0
        end = k+1

        if k >= len(nums):
            return len(set(nums)) != len(nums)

        for i in range(len(nums)-k):
            
            if len(set(nums[start+i:end+i]))<k+1:
                return True
        
        return False
        
