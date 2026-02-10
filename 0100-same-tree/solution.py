# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right
    
    def __bool__(self):
        return True




from collections import deque

class Solution:

    def xor(self, p, q):


        return (p and not q) or (q and not p)

    def dbfs(self, p, q):

        if not (p or q):
            return True
        if self.xor(p, q):
            return False
        
        pq = deque([p])
        qq = deque([q])

        while pq or qq:

            ppop = pq.popleft()
            qpop = qq.popleft()

            if ppop.val != qpop.val:
                return False
            
            if self.xor(ppop.left, qpop.left) or self.xor(ppop.right, qpop.right):

                return False

            else:

                if ppop.left:

                    pq.append(ppop.left)
                    qq.append(qpop.left)

                if ppop.right:

                    pq.append(ppop.right)
                    qq.append(qpop.right)
        
        return True





    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

       return self.dbfs(q, p)
        


