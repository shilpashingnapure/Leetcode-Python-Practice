# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        prevs = []
        nextt = []
        while fast and fast.next:
            prevs.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            nextt.append(slow.val)
            slow = slow.next
        
        i = 0
        temp = head
        while temp:
            if i % 2 == 0 and prevs:
                temp.val = prevs.pop(0)
            else:
                temp.val = nextt.pop()
            i += 1
            temp = temp.next
        