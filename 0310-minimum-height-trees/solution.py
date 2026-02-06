from collections import deque, defaultdict
class Solution:


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n < 2:
            return [0]

        adj = defaultdict(list)

        ns = [0] * n

        for n1, n2 in edges:

            adj[n1].append(n2)
            adj[n2].append(n1)

            ns[n1] += 1
            ns[n2] += 1

        queue = deque([idx for idx, n in enumerate(ns) if n == 1])

        steps = n

        while steps > 2:

            ln = len(queue)

            steps-=ln

            for _ in range(ln):

                top = queue.popleft()

                for ne in adj[top]:

                    ns[ne] -= 1
                    if ns[ne] == 1: queue.append(ne)

                

        return list(queue)


            




        




        



        




