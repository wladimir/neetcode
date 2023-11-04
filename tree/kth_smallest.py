# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        level = []
        curr = root

        while level or curr:
            while curr:
                level.append(curr)
                curr = curr.left
            curr = level.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

    def kthSmallestInOrder(self, root: Optional[TreeNode], k: int) -> int:
        # Base case: If the tree is empty, return None.
        if not root:
            return -1

        # Traverse the tree in-order and store the values in a list.
        values = []

        def traverse(node: TreeNode):
            if node:
                traverse(node.left)
                values.append(node.val)
                traverse(node.right)

        traverse(root)

        # Return the kth smallest value.
        return values[k - 1]


print(Solution().kthSmallest(TreeNode(1, None, TreeNode(2)), 2))
