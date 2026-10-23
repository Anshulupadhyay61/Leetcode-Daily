# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
        curr1 = head1
        curr2 = head2
        ans = ListNode(-1)

        curr3 = ans
        c = 0

        while curr1 != None or curr2 != None:
            total = c
            c = 0

            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next

            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next
            
            if total > 9:
                c = 1
                total -= 10
            newnode = ListNode(total)
            curr3.next = newnode
            curr3 = curr3.next

        if c>0:
            newnode = ListNode(c)
            curr3.next = newnode
        return ans.next
