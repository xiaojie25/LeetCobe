class Solution:
    def convert(self, s: str, numRows: int) -> str:

        cache = [i for i in range(numRows)] + [i for i in range(1, numRows - 1)[::-1]]
        res = [""] * numRows
        for i, c in enumerate(s):
            res[cache[i%len(cache)]] += c
        return "".join(res)


if __name__ == '__main__':
    a = Solution()
    result = a.convert("PAYPALISHIRING", 4)
    print(result)