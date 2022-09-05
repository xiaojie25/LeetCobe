class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000,
                 "IV": 4,
                 "IX": 9,
                 "XL": 40,
                 "XC": 90,
                 "CD": 400,
                 "CM": 900}
        res = 0
        move_str = s[0]
        move_index = 0
        while move_str is not None:
            if s[move_index + 1] is not None:
                if cache[s[move_index]] < cache[s[move_index + 1]] or s[move_index + 1] is None:
                    res += cache[(s[move_index] + s[move_index + 1])]
                    move_index += 2
                    move_str = s[move_index]
                else:
                    res += cache[move_str]
                    move_index += 1
                    move_str = s[move_index]

        return res




if __name__ == '__main__':
    a = Solution()
    res = a.romanToInt("III")
    print(res)