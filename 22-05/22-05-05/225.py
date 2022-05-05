# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.num = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.num += 1

    def pop(self) -> int:
        i = 0
        while i < self.num - 1:
            self.q2.append(self.q1.pop(0))
            i += 1
        num = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        self.num -= 1
        return num

    def top(self) -> int:
        i = 0
        while i < self.num - 1:
            self.q2.append(self.q1.pop(0))
            i += 1
        num = self.q1.pop(0)
        self.q2.append(num)
        self.q1, self.q2 = self.q2, self.q1
        return num

    def empty(self) -> bool:
        return self.q1 == []


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push('x')
obj.push('y')
param_3 = obj.top()
print(obj.q1)
obj.pop()
param_2 = obj.pop()
param_4 = obj.empty()

print(param_4, param_3, param_2)
