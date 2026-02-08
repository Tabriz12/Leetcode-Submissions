from collections import defaultdict, deque
class Solution:

    def dfsr(self, adj, st, visited = None, edges = None):

        if not visited:
            visited = set()
        
        print(st)
        
        visited.add(st)

        if not edges:
            edges = set()

        for n in adj[st]:

            if n in visited:

                edges.add(frozenset([st, n]))
            
            else:
                visited.add(n)
                edges.update(self.dfsr(adj, n, visited, edges))
        
        return edges
    
    










    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        adj = defaultdict(list)

        ins = [0] * (len(edges) + 1) # first 0 then rest

        for v1, v2 in edges:

            adj[v1].append(v2)
            adj[v2].append(v1)

            ins[v1] +=1
            ins[v2] += 1

        queue = deque([idx for idx, n in enumerate(ins) if n == 1 ])

        visited = set()
        while queue:


            top = queue.popleft()

            visited.add(top)

            for nei in adj[top]:

                if nei not in visited:

                    ins[nei] -= 1

                    if ins[nei] == 1:
                        queue.append(nei)
        
        
        unvisited = set(adj.keys()).difference(visited)


        for v1, v2 in edges[-1::-1]:

            if v1 in unvisited and v2 in unvisited:

                return [v1, v2]






        



    
        
