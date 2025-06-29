# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        summer = ListNode()

        cur = summer

        reminder = 0

        while l1 and l2:

            tot = (l1.val+l2.val) + reminder

            cur.next = ListNode(tot % 10)

            if tot > 9:
                reminder = 1
            else: reminder = 0

            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        

        if l1:
            cur = self.all_the_way(l1, cur, reminder)
        
        elif l2:
            cur = self.all_the_way(l2, cur, reminder)
        
        elif reminder:
            cur.next = ListNode(1)
        
        return summer.next
    
    def all_the_way(self, l, cur, reminder):

        print(l)

        while l and l.val + reminder == 10:
            cur.next = ListNode(0)
            cur = cur.next
            l = l.next

        if l:
            cur.next = ListNode(l.val + reminder)
            cur.next.next = l.next

        else:
            cur.next = ListNode(1)

        return cur       



        

        

        
