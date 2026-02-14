# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = []
        self.max_streak = 0
        self.prev = None
        self.cur_streak = 0

    def counter(self, root):
        if not root:
            return

        self.counter(root.left)

        if root.val == self.prev:
            self.cur_streak += 1
        else:
            self.cur_streak = 1
            self.prev = root.val

        if self.cur_streak == self.max_streak:
            self.res.append(root.val)
        elif self.cur_streak > self.max_streak:
            self.max_streak = self.cur_streak
            self.res = [root.val]

        self.counter(root.right)        


    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.counter(root)
        return self.res





        
