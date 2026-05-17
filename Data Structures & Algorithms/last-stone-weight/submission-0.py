import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        num_stones = len(stones)
        stone_heap = []

        # Add stones into max heap
        for stone in stones:
            heapq.heappush(stone_heap, -stone)

        while stone_heap and len(stone_heap) > 1:
            x = -heapq.heappop(stone_heap)
            y = -heapq.heappop(stone_heap)

            if y < x:
                new_stone = x - y
                heapq.heappush(stone_heap, -new_stone)

        if stone_heap:
            return -stone_heap[0]
        else:
            return 0
