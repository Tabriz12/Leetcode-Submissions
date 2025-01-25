# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        lefty = root.left
        righty = root.right

        return self.checkmate(lefty, righty)

    
    def checkmate(self, p, q):
        
        if not (p or q):
            return True
        
        if bool(p) != bool(q):
            return False

        return (
            p.val == q.val and self.checkmate(p.left, q.right) 
            and self.checkmate(p.right, q.left)
            )
        




        
