# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.robbing(root, True)

    def robbing(self, root, canRob):
        if not root:
            return 0
        if canRob:
            robRoot = root.val + self.robbing(root.left, False) + self.robbing(root.right, False)
        else:
            robRoot = -1
        notRoot = self.robbing(root.left, True) + self.robbing(root.right, True)
        return max(robRoot, notRoot)


robber = {}


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.robbing(root, True)

    def robbing(self, root, canRob):
        if not root:
            return 0
        if (root, canRob) not in robber:
            if canRob:
                robRoot = root.val + self.robbing(root.left, False) + self.robbing(root.right, False)
            else:
                robRoot = -1
            notRoot = self.robbing(root.left, True) + self.robbing(root.right, True)
            robber[(root, canRob)] = max(robRoot, notRoot)
        return robber[(root, canRob)]
