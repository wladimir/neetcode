# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow  # middle

    def rev(self, mid):
        prev, curr = None, mid

        while curr:
            tmp, curr.next, prev = curr.next, prev, curr
            curr = tmp

        return prev

    def reorderList2(self, head: Optional[ListNode]) -> None:
        mid = self.middle(head)
        right = self.rev(mid)

        left = head
        while left and right:
            tmp, left.next, right.next = left.next, right, left.next
            left, right = tmp, right.next

        while head:
            print(head.val)
            head = head.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)

        # Reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        while head:
            # print(head.val)
            head = head.next


# Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))  # 1->4->2->3
Solution().reorderList2(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))  # 1->4->2->3
