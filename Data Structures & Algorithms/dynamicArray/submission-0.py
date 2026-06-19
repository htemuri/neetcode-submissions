class DynamicArray:
    def __init__(self, capacity: int):
        self.curSize = 0
        self.cap = capacity
        self.mem = [None] * capacity

    def get(self, i: int) -> int:
        return self.mem[i]

    def set(self, i: int, n: int) -> None:
        self.mem[i] = n

    def pushback(self, n: int) -> None:
        if self.curSize == self.cap:
            self.resize()
        self.mem[self.curSize] = n
        self.curSize += 1

    def popback(self) -> int:
        t = self.mem[self.curSize - 1]
        self.mem[self.curSize - 1] = None
        self.curSize -= 1
        return t

    def resize(self) -> None:
        self.cap = self.cap * 2
        newMem = [None] * self.cap
        for i, v in enumerate(self.mem):
            newMem[i] = v
        self.mem = newMem

    def getSize(self) -> int:
        return self.curSize

    def getCapacity(self) -> int:
        return self.cap
