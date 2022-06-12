from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        if not p1 and not p2:
            return None
        if p1:
            p2 = headB
        else:
            p1 = headA
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1