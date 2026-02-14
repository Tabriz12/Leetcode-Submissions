# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def walk(self, root, lefty: bool, summ:int):

        if not root:
            return 0

        if not root.left and not root.right:

            if lefty: summ+=root.val

        else:
        
            if root.left:

                summ = self.walk(root.left, True, summ)
            
            if root.right:
                summ = self.walk(root.right, False, summ)
            
        return summ

            

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:


        return self.walk(root.left, True, 0) + self.walk(root.right, False, 0)













        


