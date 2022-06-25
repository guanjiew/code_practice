from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getLen(self, head: ListNode):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        long = headA
        short = headB
        if lenA <= lenB:
            short = headA
            long = headB
        while short:
            node_set.add(short)
            short = short.next
        while long:
            if long in node_set:
                return long
            long = long.next
        return None
