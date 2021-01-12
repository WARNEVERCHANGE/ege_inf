class Queue:

    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.size = size
        self.que = [0] * (size + 1)

    def enqueue(self, value):
        if self.count + 1 >= self.size:
            return 'queue overflow'
        else:
            self.que[self.tail] = value
            self.tail += 1
            if self.tail > self.size - 1:
                self.tail = 0

    def dequeue(self):
        if self.count == 0:
            return 'empty queue'
        else:
            value = self.que[self.head]
            self.head += 1
            if self.head > self.size - 1:
                self.head = 0
            return value
        
    def count(self):
        if self.tail > self.head:
            return self.tail -self.head
        else:
            return self.tail + self.size - self.head
    
    def empty(self):
        if self.head == self.tail:
            return True
        return False

    def peek(self):
        if self.count > 0:
            return self.head

    def clear(self):
        self.head = 0
        self.tail = 0

    def contains(self, value):
        if self.head < self.tail:
            for i in range(self.head, self.tail):
                if self.que[i] == value:
                    return True
        else:
            for i in range(self.tail, self.size+1):
                if self.que[i] == value:
                    return True
            for i in range(self.head + 1):
                if self.que[i] == value:
                    return True
        return False

    