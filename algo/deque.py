class Deque:

    def __init__(self, size):
        self.size = size
        self.deq = [0] * (size + 1)
        self.head = 0
        self.tail = 0

    def pushback(self, value):
        self.deq[self.tail] = value
        self.tail +=1
        if self.tail > self.size:
            self.tail = 0

    def pushfront(self, value):
        self.head -= 1
        if self.head < 0:
            self.head = self.size - 1
        self.deq[self.head] = value
    
    def popback(self):
        self.tail -= 1
        if self.tail < 0:
            self.tail = self.size - 1
        return self.deq[self.tail]

    def popfront(self):
        value = self.deq[self.head]
        self.head += 1
        if self.head > self.size - 1:
            self.head = 0
        return value

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def clear(self):
        self.tail = 0
        self.head = 0s