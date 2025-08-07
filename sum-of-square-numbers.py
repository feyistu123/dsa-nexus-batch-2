class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)
        sum_square = 0
        while a <= b:
            sum_square = a**2 + b**2
            if sum_square == c:
                return True
            elif sum_square < c:
                a += 1
            else:
                b -= 1
        return False
