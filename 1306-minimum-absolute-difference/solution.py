from heapq import heapify, heappop, heappush
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        heapify(arr)

        prev = heappop(arr)

        diff = sys.maxsize

        while arr:

            top = heappop(arr)

            if top - prev < diff:
                out = [[prev, top]]

                diff = top - prev
            
            elif top - prev == diff:

                out.append([prev, top])
            
            prev = top
        
        return out

        
