class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) -1

        area = 0
        while left < right:
            width = (right + 1) - (left+1) 
            length = min(heights[left], heights[right])
            current_area = width * length

            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
            
            if current_area > area:
                area = current_area
        
        return area