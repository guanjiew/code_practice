from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums: List[int], target: int) -> List[int]:
            idx = -1
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    idx = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return idx

        def binarySearchRight(nums: List[int], target: int) -> List[int]:
            idx = -1
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    idx = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx

        return [binarySearchLeft(nums, target), binarySearchRight(nums, target)]
