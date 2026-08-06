class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (min(height[left],height[right])) * (right - left)
            if height[left] < height[right]:
                left +=1 
            elif height[left] > height[right]:
                right -= 1
            elif height[left] == height[right]:
                left +=1 
                right -= 1
            
            if area > max_area:
                max_area= area
        return max_area