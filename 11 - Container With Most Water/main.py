class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        begin = 0
        end = len(height) - 1
        
        while (begin < end):
            if height[begin] <= height[end]:
                if height[begin] * (end - begin) > max_:
                    max_ = height[begin] * (end - begin)
                begin = begin + 1
            else:
                if height[end] * (end - begin) > max_:
                    max_ = height[end] * (end - begin)
                end = end - 1
        return max_
