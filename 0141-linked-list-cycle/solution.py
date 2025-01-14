# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        achilles = head
        tortoise = head

        while achilles and achilles.next:
            tortoise = tortoise.next
            achilles = achilles.next.next

            if achilles == tortoise:
                return True
        
        return False


        
        
