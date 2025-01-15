# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        right = headB
        left_set = set()
        right_set = set()

        while left or right:

            if left:
                if left in right_set:
                    return left
                    
                left_set.add(left)
                left = left.next
                
            if right:
                if right in left_set:
                    return right
                
                right_set.add(right)
                right = right.next
        
        return None
            

        
