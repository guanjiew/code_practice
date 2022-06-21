import heapq
from typing import List

"""
If using greedy strategy
"""


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    climb = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(climb, -1 * diff)
            if bricks >= diff:
                bricks -= diff
            elif ladders > 0:
                bricks += heapq.heappop(climb) * -1
                ladders -= 1
                bricks -= diff
            else:
                return i
    return len(heights) - 1






print(furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
