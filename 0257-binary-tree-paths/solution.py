# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    roads = []

    def pre(self, root, road):

        if root.left:

            self.pre(root.left, road + f"{root.val}->")
        
        if root.right:
            self.pre(root.right, road + f"{root.val}->")
        
        if not root.right and not root.left:
            self.roads.append(road + f"{root.val}")

        



    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        road = f"{root.val}->"

        self.roads = []
        if root.left:
            self.pre(root.left, road)
        
        if root.right:
            self.pre(root.right, road)
        
        if not self.roads:
            return [str(root.val)]

        return self.roads





        
