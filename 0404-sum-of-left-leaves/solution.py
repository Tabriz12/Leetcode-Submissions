# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Literal
class Solution:

    def __init__(self):

        self.tot = 0

    def preOrder(self, root, par: Literal['left', 'right'] | None):

        if root:

            if not root.left and not root.right:

                if par == 'left':

                    self.tot+=root.val
            
            else:

                self.preOrder(root.left, 'left')
                self.preOrder(root.right, 'right')





    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        self.preOrder(root, None)

        return self.tot


        
