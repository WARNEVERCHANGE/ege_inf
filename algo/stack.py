class Stack:
    
    def __init__(self, n):
        self.stck = [0] * (n + 1)
        self.sp = 0
        self.n = n

    
    def push(self, value):
        self.stck[self.sp] = value
        self.sp += 1
    
    def pop(self):
        if self.sp == 0:
            return None
        else:
            self.sp -= 1
            return self.stck[self.sp]
    
    
    def empty(self):
        if self.sp == 0:
            return True
        return False
    
    
    def contain(self, value):
        for i in range(len(self.stck)):
            if self.stck[i] == value:
                return True
        return False
    
    
    def clear(self):
        self.stck = (self.n + 1) * [0]
        self.sp = 0

    def copyto(self, start, mas):
        for i in range(start, self.sp):
            mas.append(self.stck[i])

a = Stack(10)
print(a.empty())
for i in range(1, 7):
    a.push(i)
print(a.stck)
print(a.pop())
print(a.stck)
a.push(666)
print(a.stck)
print(a.pop())
a.push(777)
print(a.stck)
print(a.contain(777))
x = []
a.copyto(2, x)
print(x)
print(a.stck)
a.clear()
print(a.empty())
print(a.stck)