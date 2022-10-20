from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) -1
        while left < right:
            cache = (right - left) * min(height[left], height[right])
            res = cache if cache > res else res
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxArea([1,1])
    print(result)