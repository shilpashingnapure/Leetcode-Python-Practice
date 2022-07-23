# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        print(slow , fast)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        
        
        if fast == None:
            slow = slow.next
            head = slow
            
        elif slow and slow.next:
            slow.next = slow.next.next
        else:
            head = None
        return head
  

        
            
            
       
   
    
    