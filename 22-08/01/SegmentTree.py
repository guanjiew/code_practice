# Recursive Segment Tree Solution
from typing import List


class SegmentTree:
    def __init__(self, A: List[int], op: callable, e: int):
        self.n = len(A)
        self.op = op
        self.e = e
        self.data = [e] * (4 * self.n)
        self.build(1, 0, self.n - 1, A)

    def build(self, i: int, l: int, r: int, A: List[int]):
        if l == r:
            self.data[i] = A[l]
            return
        m = (l + r) // 2
        self.build(i * 2, l, m, A)
        self.build(i * 2 + 1, m + 1, r, A)
        self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

    def query(self, l: int, r: int) -> int:
        return self.query_rec(1, 0, self.n - 1, l, r)

    def query_rec(self, i: int, l: int, r: int, s: int, e: int) -> int:
        if s <= l and r <= e:
            return self.data[i]
        if e < l or r < s:
            return self.e
        m = (l + r) // 2
        return self.op(self.query_rec(i * 2, l, m, s, e), self.query_rec(i * 2 + 1, m + 1, r, s, e))

    def update(self, i: int, x: int):
        self.update_rec(1, 0, self.n - 1, i, x)

    def update_rec(self, i: int, l: int, r: int, j: int, x: int):
        if l == r:
            self.data[i] = x
            return
        m = (l + r) // 2
        if m >= j:
            self.update_rec(i * 2, l, m, j, x)
        else:
            self.update_rec(i * 2 + 1, m + 1, r, j, x)
        self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

    def __str__(self):
        return str(self.data)


# Iterative Segment Tree Solution
class SegmentTree2:
    def __init__(self, A: List[int], op: callable, e: int):
        self.n = len(A)
        self.op = op
        self.e = e
        self.data = [e] * (4 * self.n)
        self.build(1, 0, self.n - 1, A)

    def build(self, i: int, l: int, r: int, A: List[int]):
        while l < r:
            m = (l + r) // 2
            self.build(i * 2, l, m, A)
            self.build(i * 2 + 1, m + 1, r, A)
            self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])
            i *= 2

    def query(self, l: int, r: int) -> int:
        return self.query_rec(1, 0, self.n - 1, l, r)

    def query_rec(self, i: int, l: int, r: int, s: int, e: int) -> int:
        if s <= l and r <= e:
            return self.data[i]
        if e < l or r < s:
            return self.e
        m = (l + r) // 2
        return self.op(self.query_rec(i * 2, l, m, s, e), self.query_rec(i * 2 + 1, m + 1, r, s, e))

    def update(self, i: int, x: int):
        self.update_rec(1, 0, self.n - 1, i, x)

    def update_rec(self, i: int, l: int, r: int, j: int, x: int):
        if l == r:
            self.data[i] = x
            return
        m = (l + r) // 2
        if m >= j:
            self.update_rec(i * 2, l, m, j, x)
        else:
            self.update_rec(i * 2 + 1, m + 1, r, j, x)
        self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

    def __str__(self):
        return str(self.data)


# BINARY INDEXED TREE Solution
class BIT:
    def __init__(self, A: List[int]):
        self.n = len(A)
        self.data = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i + 1, A[i])

    def update(self, i: int, x: int):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    def __str__(self):
        return str(self.data)
