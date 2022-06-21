import heapq
from typing import List


def furthestBuilding2(heights: List[int], bricks: int, ladders: int) -> int:
    climb = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(climb, diff)
        if len(climb) > ladders:
            bricks -= heapq.heappop(climb)
        if bricks < 0:
            return i

    return len(heights) - 1
