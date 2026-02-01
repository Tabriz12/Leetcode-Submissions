from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        nummies  =  [-n for n in nums]

        heapify(nummies)


        for _ in range(k):

            val = heappop(nummies)
        
        return -val
        
