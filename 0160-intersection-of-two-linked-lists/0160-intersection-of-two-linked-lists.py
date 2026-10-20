# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        count = 0

        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

            if p2 == None:
                count += 1
                p2 = headA
            if p1 == None:
                p1 = headB
            if count > 1:
                return None
                
