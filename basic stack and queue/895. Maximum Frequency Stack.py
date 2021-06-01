import heapq


class FreqStack1:

    def __init__(self):
        self.stack = []
        self.freqMap = {}
        self.counter = 0

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val, 0) + 1
        self.counter += 1
        heapq.heappush(self.stack, (-self.freqMap[val], -self.counter, val))

    def pop(self) -> int:
        if self.stack:
            freq, _, val = heapq.heappop(self.stack)
            self.freqMap[val] = self.freqMap[val] - 1
            return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class FreqStack:

    def __init__(self):
        self.freqMap = {}
        self.stackMap = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val, 0) + 1
        self.maxFreq = max(self.maxFreq, self.freqMap[val])
        self.stackMap[self.freqMap[val]].append(val)

    def pop(self) -> int:
        val = self.stackMap[self.maxFreq].pop()
        if not self.stackMap[self.maxFreq]: self.maxFreq -= 1
        self.freqMap[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()