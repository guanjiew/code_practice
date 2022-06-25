from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] > nums[idx + 1]:
                if modified:
                    return False
                modified = True
                if idx == 0:
                    nums[idx] = nums[idx + 1]
                elif idx == len(nums) - 2:
                    nums[idx + 1] = nums[idx]
                elif idx >= 1 and nums[idx - 1] <= nums[idx + 1]:
                    nums[idx] = nums[idx - 1]
                elif idx + 2 < len(nums) and nums[idx] <= nums[idx + 2]:
                    nums[idx + 1] = nums[idx]
                else:
                    return False
            idx += 1
        return True


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        idx = 1
        while idx < len(nums):
            if nums[idx - 1] > nums[idx]:
                if modified:
                    return False
                modified = True
                if idx == 1 or nums[idx - 2] <= nums[idx]:
                    nums[idx - 1] = nums[idx]
                else:
                    nums[idx] = nums[idx - 1]
            idx += 1
        return True
