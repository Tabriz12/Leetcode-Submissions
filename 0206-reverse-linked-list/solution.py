# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        toe = None
        
        # [1->2->3->4]

        if not head: return head

        while head:

            temp = head.next

            head.next = toe

            toe = head

            head = temp
        
        return toe


        

        
