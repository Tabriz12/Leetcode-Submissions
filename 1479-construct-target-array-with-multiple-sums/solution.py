from heapq import heappop, heappush, heapify
class Solution:

    def isPossible(self, target: List[int]) -> bool:
        

        heap = [-n for n in target]
        total = sum(target)
        heapify(heap)


        while heap:

            top =  -heappop(heap)

            if top == 1: 
                return True
            
            if top < 1 or total == top:
                return False
            
            multip = max(top // (total-top) - 1, 1)
            new_val = top - (multip*(total - top))

            if top < 1 or new_val < 1:
                return False

            heappush(heap, -new_val)

            total -= multip*(total - top)

        

        








        
