# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visit = set()
        while headA:
            visit.add(headA)
            headA=headA.next
        while headB:
            if  headB in visit:
                return headB
            else:
                headB = headB.next
        return None