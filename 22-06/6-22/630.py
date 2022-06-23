import heapq
from typing import List


def scheduleCourse(courses: List[List[int]]) -> int:
    courses.sort(key=lambda c: c[1])
    select = []

    def push(item):
        heapq.heappush(select, -1 * item)

    def pop():
        return -heapq.heappop(select)

    ft = 0
    for d, l in courses:
        push(d)
        ft += d
        if l < ft:
            ft -= pop()

    return len(select)
