# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        # corner case
        if head == None or head.next == None:
            return head
        
        current = head
        while current != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head