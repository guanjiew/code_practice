# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    solution = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.nodePair(root, p, q)
        return self.solution

    def nodePair(self, root, p, q):
        left, mid, right = 0, 0, 0
        if not root:
            return 0, 0, 0
        if root.val == p.val or root.val == q.val:
            mid = 1
        if True in self.nodePair(root.left, p, q):
            left = 1
        if True in self.nodePair(root.right, p, q):
            right = 1
        if left + mid + right >= 2:
            self.solution = root
        return left, mid, right
