class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        tempo = nums[len(nums)-k:]

        nums[k:] = nums[:len(nums)-k]

        nums[:k] = tempo
        
        return nums
        
