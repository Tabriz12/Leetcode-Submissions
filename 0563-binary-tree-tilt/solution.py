# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def __init__(self):

        self.res = 0
    
    def pos(self, root, tot):

        if not root:

            return 0


        left = self.pos(root.left, tot) 
        right = self.pos(root.right, tot)

        self.res += abs(left-right)


        tot = left + right + root.val

        return tot


    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.pos(root, 0)

        return self.res




        
