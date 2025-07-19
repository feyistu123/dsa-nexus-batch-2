class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0           #time O(n)  space O(1)
        for c in s + t:
            res ^= ord(c)
        return chr(res)

        '''for char in t:        #time O(n^2)- for loop and count method 
            if char not in s or t.count(char) != s.count(char):
                return char'''
