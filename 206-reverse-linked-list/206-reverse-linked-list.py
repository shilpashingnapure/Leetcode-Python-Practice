# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextt = None
        prev = None
        curr = head
        while curr:
            
            #storing current value in nextt variable
            nextt = curr.next
            
            #put new next value
            curr.next = prev
            
            #forwding our prev value
            prev = curr
            
            curr = nextt
        head = prev
        return head
            
        