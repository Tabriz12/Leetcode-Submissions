# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.mini = sys.maxsize
        self.prev = None

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev is not None:
            self.mini = min(self.mini, root.val - self.prev)

        self.prev = root.val

        self.inorder(root.right)

    def getMinimumDifference(self, root):
        self.inorder(root)
        return self.mini


        
