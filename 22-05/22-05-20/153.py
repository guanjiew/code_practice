from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[r] > nums[0]:
            return nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1