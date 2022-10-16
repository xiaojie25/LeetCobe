from typing import List

# 1 4 6 10
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        # special.sort()
        bottom = bottom - 1
        top = top + 1
        more_floor = 0  # 最大连续数楼层
        move = 1  # 移动指针
        # for move in special:
        special.append(bottom)
        special.append(top)
        special.sort()
        while move < len(special):
            num_floor = special[move] - special[move - 1] - 1
            move += 1
            more_floor = num_floor if num_floor > more_floor else more_floor

        return more_floor



if __name__ == '__main__':
    a = Solution()
    result = a.maxConsecutive(6, 8, [7, 6, 8])
    print(result)