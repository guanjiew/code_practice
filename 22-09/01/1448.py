# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, maxSoFar=float('-inf')) -> int:
        if not root:
            return 0
        return (1 if root.val >= maxSoFar else 0) + self.goodNodes(root.left, max(maxSoFar, root.val)) + self.goodNodes(
            root.right, max(maxSoFar, root.val))
