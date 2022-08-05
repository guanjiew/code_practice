from sortedcontainers import SortedDict


class Calendar:
    def __init__(self):
        self.calendars = SortedDict()

    def book(self, start, end):
        prev = self.calendars.bisect_left(start)
        if prev and self.calendars[prev] > start:
            return False
        nxt = self.calendars.bisect_right(start)
        if nxt and self.calendars[nxt] < end:
            return False
        self.calendars[start] = end
        return True
