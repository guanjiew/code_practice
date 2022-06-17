from typing import List


# Assume the index in the order of i, j, k and the requirement is nums[i] < nums[k] < nums[j]
# We will iterate index j in the array and
# Let i be the smallest item in nums[:j]
# Let k be the largest item in nums[j+1:] && nums[j] > nums[k]
# We can find such k by maintaining a decreasing monotonic stack for each j
# Then check if nums[i] < nums[k] for each j
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        smallest_to_j = [float("inf")] * n
        for i in range(1, n):
            smallest_to_j[i] = min(smallest_to_j[i - 1], nums[i - 1])
        stack = []
        for j in range(n - 1, 0, -1):
            while stack and nums[j] > stack[-1]:
                stack.pop()
            if stack:
                if stack[-1] > smallest_to_j[j]:
                    return True
            stack.append(nums[j])
        return False


s = Solution()
print(s.find132pattern([3, 5, 0, 3, 4]))
