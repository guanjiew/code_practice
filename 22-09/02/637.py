from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    queue = [root]
    res = []
    while queue:
        sum = 0
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        avg = sum / n
        res.append(avg)
    return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(averageOfLevels(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(averageOfLevels(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    root.right.right.right.left = TreeNode(8)
    root.right.right.right.left.left = TreeNode(9)
    root.right.right.right.left.right = TreeNode(10)
    root.right.right.right.left.right.left = TreeNode(11)
    root.right.right.right.left.right.right = TreeNode(12)
    root.right.right.right.left.right.right.left = TreeNode(13)
    root.right.right.right.left.right.right.right = TreeNode(14)
    root.right.right.right.left.right.right.right = TreeNode(14)
    print(averageOfLevels(root))
