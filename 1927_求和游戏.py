class Solution:
    def sumGame(self, num: str) -> bool:  # 前一半的sum等于后一半的sum，bob获胜 -> False
        n = list(num)
        total1 = 0
        total2 = 0
        c1 = 0
        c2 = 0
        for s in n[:len(n) // 2]:
            if s == '?':
                c1 += 1
            else:
                total1 += int(s)
        for s in n[len(n) // 2:]:
            if s == '?':
                c2 += 1
            else:
                total2 += int(s)
        if (c1 + c2) % 2 == 1:
            return True
        if c1 == c2:
            return total1 != total2
        if c1 > c2 and total1 >= total2:
            return True
        if c1 < c2 and total1 <= total2:
            return True
        if c1 > c2:
            tar = c1 - c2
            return total2 - total1 > tar // 2 * 9 or total2 - total1 < tar // 2 * 9
        if c1 < c2:
            tar = -c1 + c2
            return total1 - total2 > tar // 2 * 9 or total1 - total2 < tar // 2 * 9


if __name__ == '__main__':
    solution = Solution()
    result = solution.sumGame('25??')
    print(result)
