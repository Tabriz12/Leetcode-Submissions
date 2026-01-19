"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashy = {}

        curr = head

        while curr:
            
            hashy[curr] = Node(curr.val)
            curr = curr.next
          
        curr = head
        
        while curr:
            copy_node = hashy[curr]
            copy_node.next = hashy.get(curr.next)
            copy_node.random = hashy.get(curr.random)
            curr = curr.next

        return hashy.get(head)

    
        

        


