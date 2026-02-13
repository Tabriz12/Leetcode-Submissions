# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inOrder(self, root, target):

        if not root:
            return False

        if not root.left and not root.right:

        
            return target - root.val == 0
        
        target -= root.val
        


        return self.inOrder(root.left, target) or self.inOrder(root.right, target) 
        
        

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        
        
        
        return self.inOrder(root, targetSum)
        
