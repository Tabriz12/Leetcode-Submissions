# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postOrder(self, root, lst):

        if root:

            lst = self.postOrder(root.left, lst)
            lst = self.postOrder(root.right, lst)

            lst.append(root.val)
        
        return lst


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        lst = []

        return self.postOrder(root, lst)


        
