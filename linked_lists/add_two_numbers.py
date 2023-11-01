# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            val = sum % 10
            carry = sum // 10

            tail.next = ListNode(val)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            tail.next = ListNode(carry)

        return dummy.next
