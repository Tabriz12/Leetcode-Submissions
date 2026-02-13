# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pre(self, root, lst):
        
        if root:

            lst.append(root.val)
            self.pre(root.left, lst)
            self.pre(root.right, lst)
        
        return lst


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        return self.pre(root, lst)




        
        
