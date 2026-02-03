from collections import deque
class Solution:


    def bfs(self, adj, src, dst):


        visited = set()

        queue = deque([src])


        while queue:

            top = queue.popleft()

            if dst == top:
                return True

            if top not in visited:

                queue.extend(adj[top])

                visited.add(top)
        
        return False




    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        if n <=1 :
            return True
        
        adjm = [[] for _ in range(n)]

        for a, b in edges:

            adjm[a].append(b)
            adjm[b].append(a)
        

        return self.bfs(adjm, source, destination)
        


                        





        
        
