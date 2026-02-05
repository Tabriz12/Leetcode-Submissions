from collections import defaultdict, deque


class Graph:

    def __init__(self, nc: int) -> None:


        self.graph = defaultdict(list)

        self.ins = [0] * nc
    

    def add_edge(self, pre: int, post: int) -> None:

        self.graph[pre].append(post)
        self.ins[post] +=1






class Solution:


    def tosort(self, nc, prereqs):

        order = [ ]

        graph = Graph(nc)

        queue = deque([])

        for post, pre in prereqs:

            graph.add_edge(pre, post)
        
        for idx, course in enumerate(graph.ins):

            if course == 0:
                queue.append(idx)
        
        while queue:
            
            top = queue.popleft()

            order.append(top)

            for neigh in graph.graph[top]:

                graph.ins[neigh] -= 1

                if graph.ins[neigh] == 0:

                    queue.append(neigh)
        

        return len(order) == nc







    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        return self.tosort(numCourses, prerequisites)
       

