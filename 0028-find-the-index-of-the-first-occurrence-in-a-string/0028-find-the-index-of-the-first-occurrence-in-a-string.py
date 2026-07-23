class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)

        for l in range(m - n + 1):
            temp = haystack[l:l + n]

            if temp == needle:
                return l

        return -1