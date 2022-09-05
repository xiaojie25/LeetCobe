class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start_index = 0
        cache = {}
        for i, item in enumerate(s):
            if item not in cache or cache[item] < start_index:
                cache[item] = i
                cur = i - start_index + 1
                res = max(res, cur)
            else:
                start_index = cache[item] + 1
                cache[item] = i
        return res



if __name__ == '__main__':
    a = Solution()
    result = a.lengthOfLongestSubstring("tmmzuxt")
    print(result)