class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in brackets: 
                stack.append(char)
            elif len(stack) > 0 and char == brackets.get(stack[-1]):
                stack.pop() 
            else:
                return False
        return len(stack) == 0 
