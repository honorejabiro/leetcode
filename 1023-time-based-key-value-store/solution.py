class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        idx = self.bisect_left(arr, timestamp)

        if idx == -1:
            return ""

        return arr[idx][1]

    def bisect_left(self, arr, target):

        l, r = 0, len(arr)

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid][0] <= target:
                l = mid + 1
            else:
                r = mid

        return l - 1


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

