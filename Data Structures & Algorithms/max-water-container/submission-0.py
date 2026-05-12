class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f = 0
        b = len(heights) - 1
        maxA = 0

        while f < b:
            base = b - f
            area = min(heights[f], heights[b]) * base
            if area > maxA:
                maxA = area

            if heights[f] > heights[b]:
                b = b - 1
            else:
                f = f + 1
            
        return maxA

            
