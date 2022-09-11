import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        # Sort by efficiency
        engineers = sorted(zip(speed, efficiency), key=lambda x: x[1], reverse=True)
        # Heap of speed
        heap = []
        speed_sum = 0
        res = 0
        for s, e in engineers:
            heapq.heappush(heap, s)
            speed_sum += s
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            res = max(res, speed_sum * e)
        return res % mod


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
    print(sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3))
    print(sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4))


# Complexity Analysis:
# Time complexity: O(nlogn) - Sort, O(nlogk) - Heap, O(nlogn) - Total
# Space complexity: O(n) - Heap
