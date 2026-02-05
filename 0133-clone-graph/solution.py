
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []




from typing import Optional
from collections import deque
class Solution:


    def bfs(self, node : Node):

        if not node: return node

        queue = deque([node])

        ref = {node.val: Node(node.val)}

        while queue:

            top = queue.popleft()


            for neigh in top.neighbors:

                if neigh.val not in ref:

                    ref[neigh.val] = Node(neigh.val)

                    queue.append(neigh)

                ref[top.val].neighbors.append(ref[neigh.val])
        
        return ref[node.val]


        



    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        return self.bfs(node)



        
