# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):

        self.waitin  = deque()

        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.BFS_moving(root)

    
    def BFS_moving(self, root):

        if not root:
            return 0
        
        self.waitin.append(root)

        while self.waitin:

            self.depth+=1

            for _ in range(len(self.waitin)):

                node = self.waitin.popleft()
                if node.left:
                    self.waitin.append(node.left)
                if node.right:
                    self.waitin.append(node.right)
        
        return self.depth





        
