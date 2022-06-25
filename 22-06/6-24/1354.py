import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-x for x in filter(lambda x: x != 1, target)]
        heapq.heapify(target)
        while target:
            curMax = -heapq.heappop(target)
            rest = total - curMax
            if curMax - rest < 1 or rest == 0:
                return False
            prevMax = curMax % rest
            if prevMax == 0 and rest != 1:
                heapq.heappush(target, -rest)
            elif prevMax > 1:
                heapq.heappush(target, -prevMax)
            total -= (curMax - prevMax)
        return True
