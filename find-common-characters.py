class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        my_list = []
        n = len(words) 
        for k in range(n):
            words[k] = list(words[k])
        k=0
        while k < n-1:
            temp_list = []
            for i in range(len(words[k])):
                for j in range(len(words[k+1])):
                    if words[k][i] == words[k+1][j]:
                        temp_list.append(words[k][i])
                        words[k+1].remove(words[k+1][j])
                        i -= 1
                        break
            words[k+1] = temp_list            
            k += 1
        
        if n > 0:
            return words[-1]
        else:
            return []
       
