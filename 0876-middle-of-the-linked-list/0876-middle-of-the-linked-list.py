# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current = head
        l = 0
        while current != None:
            current = current.next
            l += 1
        current = head
        for i in range(l//2):
            current = current.next

        return current

        