class Solution:
    def reverse(self, x: int) -> int:

        if x in range(-9, 10):
            return x

        res = 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x = abs(x)
        while x > 0:
            res = res * 10 + x % 10
            x //= 10

        if res in range(-2**31, 2**31):
            return res * flag
        else:
            return 0


if __name__ == '__main__':
    a = Solution()
    result = a.reverse(10)
    print(result)