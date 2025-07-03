class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number= x
        reversed_number= 0
        if x<0:     
            return False
        while (x>0):
            remainder= x%10
            reversed_number= (reversed_number*10) + remainder
            x//=10
        return original_number == reversed_number 
            
        
