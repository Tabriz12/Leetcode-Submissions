# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        toe = None

        while head:

            nex = head
            head = head.next
            
            nex.next = toe
            toe = nex
        
        return toe



        

        
