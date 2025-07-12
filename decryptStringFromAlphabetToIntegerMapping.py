class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                ans += chr(ord('a') + num - 1) 
                i -=3
            else:
                num = int(s[i])
                ans += chr(ord('a') + num - 1) 
                i -= 1
        return ans[::-1]
                
