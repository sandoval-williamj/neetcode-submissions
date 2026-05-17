import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        largest = []
        for i in range(self.k):
            largest.append(-heapq.heappop(self.heap))

        r_v = largest[-1]

        for num in largest:
            heapq.heappush(self.heap, -num)

        return r_v
