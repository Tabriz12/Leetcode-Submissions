from collections import defaultdict, deque
class Solution:


    def bfslike(self, adj, src, dst, k):

        stop = -1

        q = deque([[src, 0, stop]])

        visited = defaultdict(list) # {price, stop}

        while q and stop <=k:

            it = len(q)

            for _ in range(it):
                
                src, pr, stop = q.popleft()

                if src not in visited or pr < visited[src][-1][0]:
                    
                    if src not in visited or visited[src][-1][1] < stop:

                        visited[src].append([pr, stop])
                    
                    else: # if stops are same and price is lower, just replace it
                        visited[src][-1] = [pr, stop]
                
                else:
                    continue
                
                for nei in adj[src]:

                    q.append([nei[0], pr + nei[1], stop+1])
            
            stop+=1
        

        if dst in visited:
            return visited[dst][-1][0]
        
        return -1

                





    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for sr, ds, p in flights:

            adj[sr].append([ds, p])
        

        return self.bfslike(adj, src, dst, k)
        








    
        
