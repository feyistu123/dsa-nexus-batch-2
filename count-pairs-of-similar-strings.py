class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                set1 = set(words[i])
                set2 = set(words[j])
                if set1 == set2:
                    count += 1
        return count
                

        
