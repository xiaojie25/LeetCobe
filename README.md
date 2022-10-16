# 16_最接近的三数之和

* python 双指针（对冲指针）

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # 求解矩形的面积
            l = right - left
            h = min(height[left], height[right])
            area = l*h
            # 需要不断维持更新最大值
            result = max(result, area)
            # 应该使得 较低直线的高度尽可能的高
            # 当left指向的直线高度较低，向右移动
            if height[left] < height[right]:
                left += 1
            # 当right指向的直线高度较低，向左移动
            else:
                right -= 1
        return result
```
