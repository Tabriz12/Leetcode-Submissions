import heapq as hq
from enum import StrEnum

medals = {

    1 :'Gold Medal',
    2 : "Silver Medal",
    3 : "Bronze Medal",

}

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        heap = []

        for index, scr in enumerate(score):

            hq.heappush(heap, (-scr, index))
        
        ctr = 0
        while heap:

            (_, idx) =  hq.heappop(heap)
            ctr+=1

            score[idx] =  str(ctr) if ctr > 3 else medals[ctr]
        
        return score

            

        
        





        
