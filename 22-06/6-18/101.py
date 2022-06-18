# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isMirroring(self, L, R):
        if L and R and L.val == R.val:
            return self.isMirroring(L.right, R.left) and self.isMirroring(L.left, R.right)
        return L == R

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirroring(root.left, root.right)


s = Solution()

print(s.isSymmetric(TreeNode(0, TreeNode(1), TreeNode(1))))
