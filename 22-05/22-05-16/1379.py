class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original.left:
            ans = self.getTargetCopy(original.left, cloned.left, target)
            if ans:
                return ans
        if original.right:
            ans = self.getTargetCopy(original.right, cloned.right, target)
            if ans:
                return ans
        return None