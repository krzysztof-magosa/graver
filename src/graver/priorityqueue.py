from itertools import count
from heapq import heapify
from heapq import heappush
from heapq import heappop


class PriorityQueue:
    REMOVED = '<removed item marker>'

    def __init__(self):
        self.data = []
        self.mapping = {}
        self.index = count()

        heapify(self.data)

    def push(self, item, prio=0):
        if item in self.mapping:
            self.remove(item)

        entry = [prio, next(self.index), item]
        heappush(self.data, entry)
        self.mapping[item] = entry

    def remove(self, item):
        entry = self.mapping.pop(item)
        entry[-1] = self.REMOVED

    def __bool__(self):
        return len(self.mapping) > 0

    def __contains__(self, item):
        if item not in self.mapping:
            return False

        if self.mapping[item][-1] is self.REMOVED:
            return False

        return True

    def pop(self):
        while self.data:
            prio, index, item = heappop(self.data)
            if item is not self.REMOVED:
                del self.mapping[item]
                return item

        raise IndexError("Queue is empty")
