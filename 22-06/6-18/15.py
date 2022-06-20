from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeros = set()
        pos = set()
        neg = set()
        for num in nums:
            if num == 0:
                zeros.add(num)
            elif num > 0:
                pos.add(num)
            else:
                neg.add(num)
        solutions = []
        # (0, pos, neg)
        for num in pos:
            if -1 * num in neg:
                solutions.append([num, -1 * num, 0])
        # (0, 0, 0)
        if len(zeros) >= 3:
            solutions.append([0,0,0])
        # (pos, neg, neg)

        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                if -1 * (neg[i] + neg[j]) in pos:
                    solutions.append([neg[i], neg[j], -1 * (neg[i] + neg[j])])
        # (neg, pos, pos)
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                if -1 * (pos[i] + pos[j]) in neg:
                    solutions.append([pos[i], pos[j], -1 * (pos[i] + pos[j])])
        return solutions


