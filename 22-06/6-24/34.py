from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_search(nums, target, 0, len(nums) - 1), self.right_search(nums, target, 0, len(nums) - 1)]

    def left_search(self, nums, target, left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target and ((mid > left and nums[mid - 1] < target) or mid == left):
            return mid
        elif nums[mid] >= target:
            return self.left_search(nums, target, left, mid - 1)
        else:
            return self.left_search(nums, target, mid + 1, right)

    def right_search(self, nums, target, left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target and ((mid < right and nums[mid + 1] > target) or mid == right):
            return mid
        elif nums[mid] > target:
            return self.right_search(nums, target, left, mid - 1)
        else:
            return self.right_search(nums, target, mid + 1, right)
