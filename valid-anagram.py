class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)   #time comp O(n) space O(1)

        '''if len(s) == len(t):     #time comp O(nlogn) space O(n)
            sortedS = sorted(s)
            sortedT = sorted(t)
            if sortedS == sortedT:
                return True
            else:
                return False
        else:
            return False'''
