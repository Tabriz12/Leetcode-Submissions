class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) == 1: return min(citations[0],1)
        
        citations.sort(reverse=True)

        
        for idx, el in enumerate(citations,1):

            if idx >= el:
                return max(el, idx-1)
            
        
        return len(citations)




        
