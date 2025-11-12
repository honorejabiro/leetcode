class MedianFinder:

    def __init__(self):
        self.left = [] # small
        self.right = [] # large

    def addNum(self, num: int) -> None:
        # Push to small heap
        heapq.heappush(self.left, -num)

        # Push largest left to large heap
        largest_left = heapq.heappop(self.left)
        heapq.heappush(self.right, -largest_left)   

        # Maintain size property
        if len(self.left) < len(self.right):
            smallest_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -smallest_right)

    def findMedian(self) -> float:

        if len(self.left) == len(self.right):
            m1 = -self.left[0]
            m2 = self.right[0]
            return (m1 + m2) / 2
        
        else:
            return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
