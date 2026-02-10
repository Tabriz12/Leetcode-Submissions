class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        h = 0
        
        for idx, n in enumerate(citations, 1):

            if idx > n:

                return h
            
            h = idx

        return h 

             


        
