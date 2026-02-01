class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:

            mid = (right + left) // 2

            if nums[mid] == target:

                return mid
            
            elif nums[mid] > target:


                if nums[min(right, len(nums)-1)] < nums[mid] and nums[min(right, len(nums)-1)] >= target:

                    left = mid + 1

                else:

                    right =  mid
            
            else:

                if  nums[left] <= target and nums[mid] < nums[left]:

                    right = mid 

                else:

                    left = mid + 1
        return -1




        
