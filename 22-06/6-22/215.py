import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    nums = [-1 * num for num in nums]
    heapq.heapify(nums)
    ans = 0
    for i in range(k):
        ans = heapq.heappop(nums)
    return ans * (-1)
