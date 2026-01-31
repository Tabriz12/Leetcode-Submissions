import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        nums.sort()

        min_val = sys.maxsize

        res = 0


        for i in range(len(nums)):


            anchor = nums[i]

            l = i+1
            r = len(nums) - 1


            while l < r:

                tot = nums[l] + nums[r] + anchor

                if tot == target:
                    return tot
                
                elif tot > target:
                    
                    r-=1

                
                else:
                    l+=1
                    
                
                if min_val > abs(tot-target):
                    min_val = abs(tot-target)
                    res = tot
        
        return res
        

        
