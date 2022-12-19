class ArrayQueue:
    Default_Capacity = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.Default_Capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def Is_empty(self):
        return self._size == 0

    def first(self):
        if self.Is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.Is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # Helps garbage collector
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        space_available = (self._front + self._size) & len(self._data)
        self._data[space_available] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned


Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
print(Q.dequeue())
print(Q.Is_empty())
print(Q.dequeue())
print(Q.Is_empty())
print(Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
Q.enqueue(4)
print(len(Q))
print(Q.dequeue())

