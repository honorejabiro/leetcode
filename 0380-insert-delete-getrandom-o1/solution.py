class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = self.length
        self.list.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        idx = self.dict[val]

        last = self.list[-1]
        self.list[idx] = last
        self.dict[last] = idx

        self.list.pop()
        del self.dict[val]
        self.length -= 1

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

