# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:


    def inOrder(self, root):

        if root:

            self.dfs(root.left)
            print(root.val)
            self.dfs(root.right)


    def recurse(self, root):

        if not root:
            return 0
        

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
    
    def bfs(self, root):

        if not root: return 0

        queue = deque([root])

        d4c = 0

        while queue:

            for _ in range(len(queue)):

                top = queue.popleft()

                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)
            
            d4c+=1
        
        return d4c





    def maxDepth(self, root: Optional[TreeNode]) -> int:



        return self.bfs(root)





        
