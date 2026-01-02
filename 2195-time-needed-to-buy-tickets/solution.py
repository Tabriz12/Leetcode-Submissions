class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:


        minus = sum([min(0, el-tickets[k]+1) for el in tickets])


        
        for i in range(len(tickets)):

            if tickets[i] >= tickets[k]:
                minus += 1
            
            if i == k: break

        last_formula = (tickets[k]-1) * len(tickets) + minus

        return last_formula
















        
