# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def bfs(self, root):

        lev = 0

        q = deque([root])

        while q:

            l = len(q)

            if l < 2**lev:

                return 2**(lev) - 1 + l

            for _ in range(l):

                top = q.popleft()

                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            
            lev+=1
        
        return 2**(lev) - 1



    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return self.bfs(root)



        
