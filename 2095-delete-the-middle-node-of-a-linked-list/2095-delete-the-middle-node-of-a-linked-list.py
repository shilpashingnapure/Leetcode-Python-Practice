# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        prev = head
        while fast and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if fast == slow:
            head = None
            return head   
        prev.next = slow.next
        return head
    