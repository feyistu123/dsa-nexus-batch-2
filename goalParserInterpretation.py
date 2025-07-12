class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result = result + 'G'
                i += 1
            elif command[i:i+2] == '()':
                result = result + 'o' 
                i += 2
            elif command[i:i+4] == '(al)':
                result = result + 'al'
                i += 4
            else: 
                i += 1
        return result
        
        
