INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automation:
    def __init__(self):
        self.state = 'start'
        self.ans = 0
        self.sign = 1
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '-' or c == '+':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c: str):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            # 无法分配给条件表达式
            # self.sign = 1 if c == '+' else self.sign = -1
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s):
        automation = Automation()
        for c in s:
            automation.get(c)
        return automation.ans * automation.sign


if __name__ == '__main__':
    a = Solution()
    result = a.myAtoi("912123123123123123   ")
    print(result)
    # 问题得到解决，使用了自动机（状态机）

