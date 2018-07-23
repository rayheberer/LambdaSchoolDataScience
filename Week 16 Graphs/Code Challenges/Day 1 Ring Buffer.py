"""
Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method returns all of the elements in the buffer.

The class's constructor and the method signatures are correct, but the constructor has not been filled in for you. You'll need to implement it yourself. 

Example:
buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()        # should return ['a', 'b', 'c']

buffer.append('d')  

buffer.get()        # should return ['b', 'c', 'd']

buffer.append('e')
buffer.append('f')

buffer.get()        # should return ['d', 'e', 'f']
"""

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.ticker = 0

    def append(self, item):
        """append an element to the end of the RingBuffer"""
        self.storage[self.ticker] = item
        self.ticker = (self.ticker + 1) % self.capacity

    def get(self):
        """Return all the elements from the oldest to the newest"""
        return [item for item in self.storage if item]