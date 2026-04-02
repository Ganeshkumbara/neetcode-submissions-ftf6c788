class Solution:
    def trap(self, height: List[int]) -> int:
        
        area = 0
        n = len(height)
        for i in range(1, n - 1):
            max_left_height = max(height[:i])
            max_right_height = max(height[i+1:])
            wall = min(max_left_height, max_right_height)
            trapped = wall - height[i]
            
            if trapped > 0:
                area += trapped
        return area
                