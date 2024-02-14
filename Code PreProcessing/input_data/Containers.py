def calculate_area(height, l, r):
    return min(height[l], height[r]) * (r - l)


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1

        best_area = -999

        while l < r:
            area = calculate_area(height, l, r)

            if area > best_area:
                best_area = area

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return best_area
