class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 2:
            return height[0] if height[0] <= height[1]  else height[1]
        
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
