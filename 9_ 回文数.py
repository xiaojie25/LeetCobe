class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True



if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(10))