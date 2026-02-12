from collections import deque
class Solution:


    def dfsr(self, graph, src=0):

        dst = len(graph)-1

        stack = deque([[0, [0]]])

        paths = []

        while stack:

            cur =  stack.pop()
            pos, road = cur

            if pos == dst:
                paths.append(road)
            
            for nei in graph[pos]:
                stack.append([nei, road + [nei]])
            
        return paths
            








    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        return self.dfsr(graph)



        


