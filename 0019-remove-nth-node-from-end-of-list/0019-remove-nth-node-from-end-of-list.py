# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        anshul = head
        samriddhi = head

        for i in range(n):
            samriddhi = samriddhi.next
        if samriddhi == None:
            head = head.next
            return head
                
        while samriddhi.next != None:
            samriddhi = samriddhi.next
            anshul = anshul.next
        anshul.next = anshul.next.next

        return head 
    


        
        