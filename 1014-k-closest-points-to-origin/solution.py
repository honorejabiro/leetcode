class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = [(-(x**2 + y**2), x, y) for x, y in points]
        
        # Keep a min heap of size k
        print(distances)
        heap = []

        for point in distances:
            heapq.heappush(heap, point)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [(x, y) for _, x, y in heap]

