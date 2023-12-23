class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start_i = -1
        cur_tot = 0
        grand_tot = 0
        for i in range(len(gas)):

            expense = gas[i] - cost[i]

            grand_tot += expense

            if expense >= 0:
                cur_tot += expense
                if start_i == -1:
                    start_i = i
            else:
                if cur_tot + expense < 0:
                    start_i = -1
                    cur_tot = 0 
                else: cur_tot += expense
        
        if grand_tot>=0: 
            return start_i
        else: return -1


        
