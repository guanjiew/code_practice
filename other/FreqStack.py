from collections import deque


class FreqStack:

    def __init__(self):
        # Define fs as a mapping between the frequency k to a stack Lk
        self.fs = {}
        # Define nf as a mapping between the item to the frequency seen so far in the list
        self.nf = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.nf[val] + 1 if val in self.nf else 1
        self.nf[val] = freq
        self.max_freq = max(self.max_freq, freq)
        if freq not in self.fs:
            self.fs[freq] = deque()
        self.fs[freq].append(val)

    def pop(self) -> int:
        top_freq_stack = self.fs[self.max_freq]
        if not top_freq_stack:
            self.fs.pop(self.max_freq)
            self.max_freq -= 1
            top_freq_stack = self.fs[self.max_freq]
        item = top_freq_stack.pop()
        self.nf[item] -= 1
        return item


obj = FreqStack()
obj.push(12)
obj.push(14)
obj.push(12)
obj.push(13)
obj.push(14)
obj.push(13)
obj.push(12)
obj.push(14)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
