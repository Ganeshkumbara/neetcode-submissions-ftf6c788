class Solution:
    def trap(self, height: List[int]) -> int:
        
        # area = 0
        # n = len(height)
        # for i in range(1, n - 1):
        #     max_left_height = max(height[:i])
        #     max_right_height = max(height[i+1:])
        #     wall = min(max_left_height, max_right_height)
        #     trapped = wall - height[i]
        #     print(height[i], max_left_height, max_right_height, wall, trapped)
            
        #     if trapped > 0:
        #         area += trapped
        # return area
                
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left +=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max -  height[right]
                right -=1
        
        return water