class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(s):
            if ptr2 < len(spaces) and ptr1 == spaces[ptr2]:
                result.append(" ")
                ptr2 += 1
            result.append(s[ptr1])
            ptr1 += 1
           
        return "".join(result)
        
