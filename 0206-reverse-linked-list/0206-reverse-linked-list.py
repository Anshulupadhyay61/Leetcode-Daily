# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        nxt = None
        current = head

        while current != None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev