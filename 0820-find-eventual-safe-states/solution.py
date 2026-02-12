from collections import deque, defaultdict
class Solution:


    def binaryInsert(self, arr, n):

        l, r = 0, len(arr)

        while l < r:

            mid = (l+r) // 2

            if arr[mid] == n:
                arr.insert(mid, n)
                return arr

            elif arr[mid] > n:

                r = mid
            
            else:
                l = mid + 1
        

        arr.insert(l, n)
        return arr
    
    def topo(self, graph):

        ins = defaultdict(list)
        cnts = [0] * len(graph)
        res = []

        for idx, dsts in enumerate(graph):

            cnts[idx] = len(dsts)

            if len(dsts) == 0:
                res.append(idx)

            for out in dsts:
                ins[out].append(idx)


        q = deque(list(res))

        while q:

            top = q.popleft()

            for income in ins[top]:

                cnts[income]-=1
                if cnts[income] == 0:
                    q.append(income)
                    res = self.binaryInsert(res, income)
        
        return res
        
                    



    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        return self.topo(graph)


        
        










        
