# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0 

    def postOrd(self, root):

        if not root:
            return 0
        


        leftdepth = self.postOrd(root.left)
        rightdepth = self.postOrd(root.right)

        self.res = max(self.res, leftdepth+rightdepth)

        return 1 + max(leftdepth, rightdepth)





    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.postOrd(root)
        return self.res






        
