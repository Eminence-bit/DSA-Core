class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] > height[j]:
                temp = height[j] * (j - i)
                j -= 1
            else:
                temp = height[i] * (j - i)
                i += 1
            if temp > max_area:
                max_area = temp
        return max_area