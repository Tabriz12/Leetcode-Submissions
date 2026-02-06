from collections import defaultdict, deque
class Solution:

    def bfs(self, adj) -> set:

        start = list(adj.keys())[0]
        queue = deque([start])

        visited = set()

        while queue:

            top = queue.popleft()

            visited.add(top)

            for n in adj[top]:

                if n not in visited:
                    #visited.add(n)
                    queue.append(n)

        return visited


    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adj = defaultdict(list)

        for row in range(0, len(isConnected)):
            for col in range(row, len(isConnected)):
                if isConnected[row][col] == 1:
                    adj[row].append(col)
                    adj[col].append(row)
                
        prov = 0

        while len(adj) > 0:


            visited_set = self.bfs(adj)

            for k in visited_set:
                del adj[k]
            
            prov+=1
        
        return prov
            

        




        



        
