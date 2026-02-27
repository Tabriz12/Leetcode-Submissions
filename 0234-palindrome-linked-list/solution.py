# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        self.curr = head

        return self.walk(head)

    
    def walk(self, head)->bool:

        if not head:
            return True
        
        res = (self.walk(head.next) and self.curr.val == head.val)

        self.curr = self.curr.next

        return res


        
        

        
