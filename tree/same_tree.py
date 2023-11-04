# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    # Base case: If both trees are empty, they are the same.
    if not p and not q:
        return True
    # If one tree is empty while the other is not, they are not the same.
    if not p or not q:
        return False
    # Check if the values of the current nodes are the same.
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees.
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Example usage:
# Construct the trees from the given input lists
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(4)

result = isSameTree(p, q)
print(result)  # Output: True
