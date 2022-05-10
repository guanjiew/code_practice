class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        print(self.stack)
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            print(self.stack)
            if isinstance(top, int):
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False

NestedIterator([[1,1],2,[1,1]])
