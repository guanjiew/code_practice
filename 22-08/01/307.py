from typing import List


# Recursive Segment Tree

class TreeNode:
    def __init__(self, start, end, total):
        self.start = start
        self.end = end
        self.sum = total
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        def build_segment_tree(start, end):
            if start == end:
                return TreeNode(start, end, nums[start])
            mid = (start + end) // 2
            left = build_segment_tree(start, mid)
            right = build_segment_tree(mid + 1, end)
            root = TreeNode(start, end, left.sum + right.sum)
            root.left = left
            root.right = right
            return root

        self.root = build_segment_tree(0, len(nums) - 1)
        # Runtime: O(n) T(n) = 2T(n/2) + O(1)

    def update(self, index: int, val: int) -> None:
        self.update_segment_tree(self.root, index, val)

    def update_segment_tree(self, root, index, val):
        if index > root.end or index < root.start:
            return
        if root.start == index and root.end == index:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update_segment_tree(root.left, index, val)
        else:
            self.update_segment_tree(root.right, index, val)
        root.sum = root.left.sum + root.right.sum
        return
        # Runtime O(log(n))

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_segment_tree(self.root, left, right)

    def sum_segment_tree(self, root, i, j):
        if j > root.end or i < root.start:
            return 0
        if root.start == i and root.end == j:
            return root.sum
        mid = (root.start + root.end) // 2
        if j <= mid:
            return self.sum_segment_tree(root.left, i, j)
        elif i >= mid + 1:
            return self.sum_segment_tree(root.right, i, j)
        else:
            return self.sum_segment_tree(root.left, i, mid) + self.sum_segment_tree(root.right, mid + 1, j)
        # Runtime: O(log(n))
