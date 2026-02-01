class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr)

        while left < right:

            mid = (right+left) // 2

            if arr[mid - 1] > arr[mid]:

                right = mid
            
            elif arr[mid+1 ] > arr[mid]:

                left = mid + 1
            
            else:
                return mid
        
        return -1


            
