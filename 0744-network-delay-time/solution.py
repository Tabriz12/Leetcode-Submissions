import sys
from heapq import heapify, heappop, heappush
class Solution:


    def djikstra(self, adj, st, n):

        heap = []
        heapify(heap)
        min_dis = n * [sys.maxsize]

        min_dis[st] = 0

        heappush(heap, (0, st))
        while heap:

            time, edge_id = heappop(heap)

            if time > min_dis[edge_id]:
                continue


            for neig in adj[edge_id]:
                
                n_time,  n_id = neig
                if min_dis[edge_id] + n_time < min_dis[n_id]:

                    min_dis[n_id] = min_dis[edge_id] + n_time
                
                    heappush(heap, (min_dis[edge_id] + n_time, n_id))
                
        
        return -1 if max(min_dis) == sys.maxsize else max(min_dis)










    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        wb = [[] for _ in range(n)]


        for src, dst, time in times:

            wb[src-1].append([time, dst-1])
        

        return self.djikstra(wb, k-1, n)
        


        

        


        
