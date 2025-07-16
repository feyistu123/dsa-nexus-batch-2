class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        for i in range(m - n + 1):
            if needle == haystack[i:i+n]:
                return i
                break
        else:
            return -1
