from collections import deque, defaultdict
class Solution:


    def topOrder(self, nc, prereq):

        order = deque([])

        queue = deque([])

        ins = [0] * nc
        graph = defaultdict(list)

        for post, pre in prereq:

            graph[pre].append(post)
            ins[post] +=1
        
        for idx, crs in enumerate(ins):

            if crs == 0:
                queue.append(idx)
        
        while queue:

            top = queue.popleft()
            order.append(top)

            for ne in graph[top]:

                ins[ne] -= 1
                if ins[ne] == 0: queue.append(ne)
        

        return list(order) if len(order) == nc else []

        



    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        return self.topOrder(numCourses, prerequisites)
        
