from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:


        if n == 1:
            return 1

        trusts = [0] * (n + 1)
        istrusted_by = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1
            istrusted_by[b] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and istrusted_by[i] == n - 1:
                return i
        return -1


        
