# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        #recursive apporch
        if head.next != None:
            head.val , head.next.val = head.next.val , head.val
            self.swapPairs(head.next.next)
        return head
        
        
        #itrative apporch
        # temp = head
        # while temp and temp.next != None:
        #     temp.val , temp.next.val = temp.next.val , temp.val
        #     temp = temp.next.next
        # return head
        