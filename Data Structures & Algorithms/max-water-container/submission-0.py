class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 
        i = 0
        j = len(heights) - 1
        while (i < j):
            if heights[i] < heights[j]:
                newArea = heights[i]*(j-i)
                i += 1
            else:
                newArea = heights[j]*(j-i)
                j -= 1
            if newArea > area:
                area = newArea
        return area
            


        