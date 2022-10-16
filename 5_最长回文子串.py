class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = []
        res_len = 0

        for item_index, item in enumerate(s):
            mid = item_index
            while mid < len(s) and s[mid] == item:
                right = mid
                mid += 1
            # print(right)
            left, right = item_index, right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            if right - left - 1 > res_len:
                res_len = right - left - 1
                longest = s[left+1: right]
        return longest


if __name__ == '__main__':
    a = Solution()
    result = a.longestPalindrome("babad")
    print(result)